from twilio.rest import Client

# Configurações
account_sid = "AC62851070e7bd4b142cf0221ad028af62"
auth_token = "seu_auth_token"
client = Client(account_sid, auth_token)

# Enviando mensagem
message = client.messages.create(
    to="whatsapp:+557197375445",
    from_="whatsapp:+14155238886",
    body="Mensagem de teste via Twilio"
)

print(f"Mensagem enviada! SID: {message.sid}")
