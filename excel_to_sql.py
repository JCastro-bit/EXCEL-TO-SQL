import pandas as pd
from sqlalchemy import create_engine

def excel_to_sql(file_path, db_connection_string, table_names):
    # Lee el archivo xlsx
    df = pd.read_excel(file_path)

    # Limpia los espacios extra en los nombres de las columnas
    df.columns = df.columns.str.strip()

    # Crear la conexión a la base de datos
    engine = create_engine(db_connection_string)

    # Sube los DataFrames a la base de datos
    for table_name in table_names:
        if table_name in df.columns:
            df[[table_name]].drop_duplicates().to_sql(table_name, con = engine, if_exists = 'replace', index = False)
        df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)

# Uso del método:
excel_to_sql('ruta/a/tu/archivo.xlsx', 'mysql+pymysql://root:0000@localhost:3306/base-de-datos', ['tabla1', 'tabla2', 'tabla3'])
