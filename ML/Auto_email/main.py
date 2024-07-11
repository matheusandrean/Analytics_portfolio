from db_connector import get_top_campaigns
from report_generator import generate_report
from email_sender import send_email

def main():
    # Conectar ao banco de dados e obter as 5 melhores campanhas
    top_campaigns = get_top_campaigns()
    
    # Gerar o relatório
    report = generate_report(top_campaigns)
    
    # Enviar o relatório por e-mail
    send_email(report)

if __name__ == "__main__":
    main()
