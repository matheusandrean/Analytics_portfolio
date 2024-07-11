import pyodbc
import pandas as pd

def get_top_campaigns():
    server = 'your_server.database.windows.net'
    database = 'your_database'
    username = 'your_username'
    password = 'your_password'
    driver= '{ODBC Driver 17 for SQL Server}'
    
    with pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
        query = """
        SELECT TOP 5 campaign_name, performance_metric
        FROM campaigns
        WHERE date = CAST(GETDATE() AS DATE)
        ORDER BY performance_metric DESC
        """
        df = pd.read_sql(query, conn)
        
    return df
