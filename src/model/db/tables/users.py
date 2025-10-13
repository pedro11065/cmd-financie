import uuid, os
from src.config.colors import*
from src.model.db.DbConnect import Db_connect
class Users:

    def __init__(self):
        pass

    class Create:

        @staticmethod
        def user(name, login, password, salary, salary_day):
            try:

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

                return True

    
            except Exception as e:

                print(cyan('[Banco de dados] ') + red('[Erro] ') + f'Falha ao registrar usuário: {e}')

                os.system("pause")

                return False
            
    class Read:

        @staticmethod
        def user_by_login(login):

            try:
                db = Db_connect()
                cur = db.conn.cursor()

                cur.execute("""
                    SELECT *
                    FROM usuarios
                    WHERE login = %s;
                """, (login,))

                user = cur.fetchone()
                cur.close()
                db.conn.close()

                print(user)
                input()

                return user
            
            except Exception as e:

                print(cyan('[Banco de dados] ') + red('[Erro] ') + f'Falha ao buscar usuário por login: {e}')
                os.system("pause")

                return False
        
            


        @staticmethod
        def all_users():

            try:
                db = Db_connect()
                cur = db.conn.cursor()
                cur.execute("""
                    SELECT id, nome, login, senha_hash, salario, salario_dia
                    FROM usuarios;
                """)

                users = cur.fetchall()

                cur.close()
                db.conn.close()

                return users
            
            except Exception as e:

                print(cyan('[Banco de dados] ') + red('[Erro] ') + f'Falha ao buscar todos os usuários: {e}')

                return False

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