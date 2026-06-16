import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


class DatabaseConnector:

    @staticmethod
    def get_engine():

        return create_engine(
            f"postgresql+psycopg2://"
            f"{os.getenv('POSTGRES_USER')}:"
            f"{os.getenv('POSTGRES_PASSWORD')}@"
            f"{os.getenv('POSTGRES_HOST')}:"
            f"{os.getenv('POSTGRES_PORT')}/"
            f"{os.getenv('POSTGRES_DATABASE')}"
        )