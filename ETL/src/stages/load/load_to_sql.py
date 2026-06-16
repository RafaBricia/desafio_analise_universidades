import pandas as pd

from ETL.src.infra.database_conector import DatabaseConnector


class LoadToSQL:

    def __init__(self):
        self.engine = DatabaseConnector.get_engine()

    def load(
        self,
        df: pd.DataFrame,
        table_name: str
    ):

        df.to_sql(
            table_name,
            self.engine,
            if_exists='replace',
            index=False
        )