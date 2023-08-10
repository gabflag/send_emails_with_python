import smtplib
import threading
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from decouple import config


def send_email_erro_api_image(user_email, user_name, tempo_envio):
    def enviar():
        time.sleep(tempo_envio)

        subject = 'Envio de email teste'
        from_email = config('EMAIL_USER')
        recipient_email = user_email

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        email_user = config('EMAIL_USER')
        email_password = config('EMAIL_PASSWORD')

        with open('email_template.html', 'r', encoding='utf-8') as file:
            html_template = file.read()
            
        email = MIMEMultipart()
        email['From'] = from_email
        email['To'] = recipient_email
        email['Subject'] = subject

        email.attach(MIMEText(html_template, 'html', _charset='utf-8'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(email_user, email_password)
            server.sendmail(from_email, recipient_email, email.as_string())
            server.quit()
        except Exception as e:
            print("Erro ao enviar o email:", e)

    # Cria uma thread para executar o envio
    thread = threading.Thread(target=enviar)
    thread.start()


send_email_erro_api_image('exemple@gmail.com', 'Gub Teste', 5)
