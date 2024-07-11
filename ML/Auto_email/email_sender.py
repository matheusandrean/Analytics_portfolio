import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(report):
    from_email = "your_email@gmail.com"
    to_email = "recipient_email@example.com"
    password = "your_email_password"

    # Configurar a mensagem
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Daily Campaign Report"
    
    # Adicionar o relatório ao corpo do e-mail
    msg.attach(MIMEText(report, 'plain'))
    
    # Enviar o e-mail
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
