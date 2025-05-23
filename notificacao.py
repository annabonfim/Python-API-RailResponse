from twilio.rest import Client
import os

def enviar_alerta_critica(alerta):
    print(f"[TWILIO] Enviando alerta crítico via WhatsApp: {alerta['mensagem']}")

    # Carrega dados do ambiente
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_TOKEN")
    from_whatsapp = os.getenv("TWILIO_FROM")  # Ex: "whatsapp:+14155238886"
    to_whatsapp = os.getenv("TWILIO_TO")      # Ex: "whatsapp:+55SEUNUMERO"

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


