from sqlalchemy import text
from ETL.src.infra.database_conector import DatabaseConnector


class SQLExecutor:

    def __init__(self):
        self.engine = DatabaseConnector.get_engine()

    def execute_file(self, file_path: str):

        with open(file_path, "r", encoding="utf-8") as file:
            query = file.read()

        self.engine.dispose()
        
        with self.engine.connect() as conn:
            result = conn.execute(text(query))

            if result.returns_rows:
                rows = result.fetchall()
                for row in rows:
                    print(dict(row._mapping))