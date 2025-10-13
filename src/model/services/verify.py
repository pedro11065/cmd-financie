import re
from src.model.db.DbController import *

class Verify:

    def __init__(self):
        
        self.user = Verify.User()

    class User:

        def __init__(self):
            self.db = Db()

        def fullname(fullname):
                
            if " " in fullname:
                return True, ""
            
            else:
                print("Nome inválido!")
                return False, ""
            

        def login(self, login, password_hash):

            user = self.db.users.Read.user_by_login(login)
            
            if user and user.password_hash == password_hash:
                return True
            return False
            

        def password(password):

            if len(password) >= 8:

                if re.search(r'\d', password):
                    if re.search(r"[a-zA-Z]", password):
                        return True, ""
                    return False , "A senha precisa ter no mínimo uma letra."
                return False , "A senha precisa ter no mínimo um número."
            
        def salary(salary):

            try: 
                float(salary)
                return True, ""
            except:
                return False , "Salário inválido."

        def salary_day(salary_day):

            try: 
                int(salary_day)
                if salary_day <= 31:
                    return True, ""
            except:
                return False , "Data de pagamento inválida."

                    




            
            

            

