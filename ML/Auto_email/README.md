# Email Reporter

Este projeto se conecta a um banco de dados Azure SQL, extrai as 5 melhores campanhas do dia e envia um relatório por e-mail usando uma conta do Gmail.

## Configuração

1. Crie um ambiente virtual e instale as dependências:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

2. Atualize as informações de conexão do banco de dados em `db_connector.py`.

3. Atualize as credenciais de e-mail em `email_sender.py`.

4. Execute o script principal:
    ```sh
    python main.py
    ```

## Estrutura do Projeto

- `main.py`: Script principal que orquestra a execução.
- `db_connector.py`: Conexão e consulta ao banco de dados.
- `report_generator.py`: Geração do relatório a partir dos dados.
- `email_sender.py`: Envio do e-mail com o relatório.
- `requirements.txt`: Dependências do projeto.
- `README.md`: Documentação do projeto.
