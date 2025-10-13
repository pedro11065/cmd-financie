import os, psycopg2
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import logging
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

class Db_connect:
    def __init__(self):
        self.check = False
        self.host = ""
        self.database = ""
        self.user = ""
        self.password = ""
        self.conn = ""
        self.read_db_info()

    def read_db_info(self):
        # Carrega variáveis do .env no root
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        env_path = os.path.join(root_dir, '.env')
        load_dotenv(env_path)
        try:
            self.host = os.getenv('DB_HOST')
            self.database = os.getenv('DB_DATABASE')
            self.user = os.getenv('DB_USER')
            self.password = os.getenv('DB_PASSWORD')
            self.check = True
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
        except Exception as error:
            print(f"Erro: {error}")
            self.check = False

class Base(DeclarativeBase):
    pass
