import requests
import smtplib
import email.message

# pegar a informação que quero
requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['USDBRL']['bid'])
print(cotacao)

# enviar um aviso
def enviar_email(cotacao):
    corpo_email = f'''
    <p>Dólar está abaixo de R$5,20. Cotação atual: R${cotacao}</p>
    '''

    msg = email.message.Message()
    msg['Subject'] = 'Hoje o dólar está abaixo de R$5,20!'
    msg['From'] = 'fabio20101234567@gmail.com'
    msg['To'] = 'fabio201012345@hotmail.com'
    password = 'senha' # precisa ser uma senha específica para este código
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Credenciais de login para enviar o email
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('UTF-8'))
    print('Email enviado!')

if cotacao < 5,20:
    enviar_email(cotacao)

# deploy - heroku
