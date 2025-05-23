from fastapi import FastAPI, Request
from datetime import datetime
import pytz
from alerta_classifier import classificar_alerta
from notificacao import enviar_alerta_critica
from storage_oracle import salvar_no_banco, buscar_todos
from clima import consultar_clima
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
load_dotenv()


app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint de status/boas-vindas
@app.get("/")
def home():
    return {"mensagem": "API RailResponse está online!"}

@app.post("/notificar")
async def notificar_alerta(request: Request):
    data = await request.json()

    br_tz = pytz.timezone("America/Sao_Paulo")
    alerta = {
        "trem": data["trem"],
        "sistema": data["sistema"],
        "mensagem": data["mensagem"],
        "hora": datetime.now(br_tz).isoformat()
    }

    alerta["prioridade"] = classificar_alerta(alerta)
    salvar_no_banco(alerta)

    if alerta["prioridade"] == "Alta":
        enviar_alerta_critica(alerta)

    return {"status": "recebido", "alerta": alerta}

@app.get("/alertas")
def listar_alertas():
    alertas = buscar_todos()
    br_tz = pytz.timezone("America/Sao_Paulo")
    for alerta in alertas:
        if isinstance(alerta.get("hora"), datetime):
            alerta["hora"] = alerta["hora"].astimezone(br_tz).isoformat()
    return alertas

from fastapi import Path
from storage_oracle import atualizar_alerta, deletar_alerta

@app.put("/alertas/{id_alerta}")
async def atualizar(id_alerta: int, request: Request):
    novos_dados = await request.json()
    atualizar_alerta(id_alerta, novos_dados)
    return {"status": "atualizado", "id_alerta": id_alerta}

@app.delete("/alertas/{id_alerta}")
def deletar(id_alerta: int = Path(..., description="ID do alerta a ser deletado")):
    deletar_alerta(id_alerta)
    return {"status": "deletado", "id_alerta": id_alerta}

@app.get("/clima-alerta")
def clima_alerta():
    clima = consultar_clima("Sao Paulo")
    if not clima:
        return {"status": "erro", "mensagem": "Não foi possível obter o clima"}

    alerta = None
    if clima["condicao"] in ["thunderstorm", "tornado", "squall"]:
        alerta = f"🌩️ Alerta de tempestade forte em {clima['cidade']}: {clima['descricao']}"
    elif clima["condicao"] in ["drizzle", "rain"]:
        alerta = f"🌧️ Alerta de chuva em {clima['cidade']}: {clima['descricao']}"
    elif clima["condicao"] in ["fog", "mist", "haze"]:
        alerta = f"🌫️ Neblina densa em {clima['cidade']}, atenção redobrada."
    elif clima["temperatura"] >= 35:
        alerta = f"🔥 Calor extremo: {clima['temperatura']}°C em {clima['cidade']}."
    elif clima["temperatura"] <= 5:
        alerta = f"❄️ Frio intenso: {clima['temperatura']}°C em {clima['cidade']}."

    if alerta:
        enviar_alerta_critica({"mensagem": alerta})
        return {"status": "alerta enviado", "mensagem": alerta}

    return {"status": "ok", "mensagem": f"Sem condições adversas detectadas: {clima['descricao']}"}

from simulador import gerar_alerta_simulado
from alerta_classifier import classificar_alerta
from storage_oracle import salvar_no_banco

scheduler = BackgroundScheduler()

def alerta_simulado():
    alerta = gerar_alerta_simulado()
    br_tz = pytz.timezone("America/Sao_Paulo")
    alerta["hora"] = datetime.now(br_tz).strftime("%Y-%m-%dT%H:%M:%S.%f")
    alerta["prioridade"] = classificar_alerta(alerta)
    salvar_no_banco(alerta)

    if alerta["prioridade"] == "Alta":
        enviar_alerta_critica(alerta)

    print("[SIMULADOR] Alerta gerado e processado:", alerta)

@app.on_event("startup")
def iniciar_agendamentos():
    scheduler.add_job(clima_alerta, "interval", minutes=1)
    scheduler.add_job(alerta_simulado, "interval", minutes=1)
    scheduler.start()