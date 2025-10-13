import uuid
from src.config.colors import*
from src.model.db.DbConnect import Db_connect
class Users:

    def __init__(self):
        pass

    class Create:
        @staticmethod
        def user(name, login, password, salary, salary_day):
            print(cyan('[Banco de dados] ') + 'Registrando novo usuário...')
            db = Db_connect()
            cur = db.conn.cursor()
            id = str(uuid.uuid4())
            cur.execute("""
                INSERT INTO usuarios (id, nome, login, senha_hash, salario, salario_dia)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (id, name, login, password, salary, salary_day))
            db.conn.commit()
            cur.close()
            db.conn.close()

    class Read:
        @staticmethod
        def user_by_login(login):
            # Implementar lógica de busca por login
            pass
        @staticmethod
        def all_users():
            # Implementar lógica de busca de todos os usuários
            pass

    class Update:
        @staticmethod
        def user(id, **kwargs):
            # Implementar lógica de atualização de usuário
            pass

    class Delete:
        @staticmethod
        def user(id):
            # Implementar lógica de remoção de usuário
            pass