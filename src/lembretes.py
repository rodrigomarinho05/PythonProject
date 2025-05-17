from twilio.rest import Client
import os
import json
from datetime import datetime

def carregar_lembretes():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'lembretes.json')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Erro: Arquivo {file_path} não encontrado.")
        return []

def enviar_mensagem_via_whatsapp(to_number, mensagem):
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    from_number = "whatsapp:+14155238886"  # Número padrão Twilio

    if not account_sid or not auth_token:
        print("Erro: Variáveis de ambiente não estão definidas!")
        return

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            from_=from_number,
            to=f"whatsapp:{to_number}",
            body=mensagem  # Corpo da mensagem personalizada
        )
        print(f"Mensagem enviada com sucesso. SID: {message.sid}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

def gerar_titulo():
    # Data e dia da semana
    data_atual = datetime.now().strftime('%d/%m/%Y')
    dia_semana = datetime.now().strftime('%A')
    # Traduzindo para português
    dias = {
        "Monday": "Segunda-feira",
        "Tuesday": "Terça-feira",
        "Wednesday": "Quarta-feira",
        "Thursday": "Quinta-feira",
        "Friday": "Sexta-feira",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }
    dia_semana = dias.get(dia_semana, dia_semana)
    return f"Lembrete do {data_atual} - {dia_semana}:"

def verificar_lembretes():
    lembretes = carregar_lembretes()
    agora = datetime.now().strftime('%Y-%m-%d %H:%M')

    mensagens = []
    for lembrete in lembretes:
        if lembrete['data_hora'] == agora:
            mensagens.append(f"- {lembrete['mensagem']}")

    if mensagens:
        titulo = gerar_titulo()
        corpo_mensagem = titulo + "\n" + "\n".join(mensagens)
        enviar_mensagem_via_whatsapp("+557197375445", corpo_mensagem)

if __name__ == "__main__":
    verificar_lembretes()
