from twilio.rest import Client
import os
from datetime import datetime, timedelta, timezone

def enviar_alerta_critica(alerta):
    print(f"[TWILIO] Enviando alerta crítico via WhatsApp: {alerta['mensagem']}")

    # Carrega dados do ambiente
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_TOKEN")
    from_whatsapp = os.getenv("TWILIO_FROM")  # Ex: "whatsapp:+14155238886"
    to_whatsapp = os.getenv("TWILIO_TO")      # Ex: "whatsapp:+55SEUNUMERO"

    hora = alerta.get("hora", "N/D")
    if hora != "N/D":
        try:
            hora_dt = datetime.fromisoformat(hora)
            hora_br = hora_dt.astimezone(timezone(timedelta(hours=-3)))
            hora_formatada = hora_br.strftime("%d/%m/%Y %H:%M:%S")
        except Exception:
            hora_formatada = hora
    else:
        hora_formatada = "N/D"

    # Envia a mensagem
    client = Client(account_sid, auth_token)
    mensagem = (
        f"🚨 *Alerta Crítico Ferroviário*\n\n"
        f"• Trem: {alerta.get('trem', 'N/D')}\n"
        f"• Linha: {alerta.get('linha', 'N/D')}\n"
        f"• Estação: {alerta.get('estacao', 'N/D')}\n"
        f"• Sistema: {alerta.get('sistema', 'N/D').capitalize()}\n"
        f"• Horário: {hora_formatada}\n"
        f"• Detalhes: {alerta.get('mensagem', '')}\n\n"
        f"⚠️ Encaminhar imediatamente à equipe responsável."
    )

    message = client.messages.create(
        body=mensagem,
        from_=from_whatsapp,
        to=to_whatsapp
    )
    print(f"[TWILIO] Mensagem enviada com SID: {message.sid}")
