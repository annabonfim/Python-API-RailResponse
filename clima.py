import requests
import os


def consultar_clima(cidade="Sao Paulo", pais="BR"):
    api_key = os.getenv("OPENWEATHER_KEY")
    cidade_formatada = cidade.replace(" ", "%20")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade_formatada},{pais}&appid={api_key}&units=metric&lang=pt_br"

    response = requests.get(url)
    if response.status_code != 200:
        print("[ERRO] Falha ao consultar clima:", response.text)
        return None

    dados = response.json()
    temperatura = dados["main"]["temp"]
    descricao = dados["weather"][0]["description"]
    condicao_bruta = dados["weather"][0]["main"].lower()

    print(f"☀️ {cidade}: {temperatura}°C, {descricao}")
    return {
        "cidade": cidade,
        "temperatura": temperatura,
        "descricao": descricao.lower(),
        "condicao": condicao_bruta
    }