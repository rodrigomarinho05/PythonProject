from twilio.rest import Client

account_sid = "AC62851070e7bd4b142cf0221ad028af62"
auth_token = "seu_auth_token"
try:
    client = Client(account_sid, auth_token)
    account = client.api.accounts(account_sid).fetch()
    print(f"Autenticação bem-sucedida: {account.friendly_name}")
except Exception as e:
    print(f"Erro de autenticação: {e}")
