import re

class Verify:

    def __init__(self):
        
        self.user = self.User()

    class User:

        def fullname(fullname):
                
            if " " in fullname:
                return True, ""
            
            else:
                print("Nome inválido!")
                return False, ""
            
        def login(login):

            None
            return True, ""

        def password(password):

            if len(password) >= 8:

                if re.search(r'\d',password):
                    if re.search(r"[a-zZ-A]", password):
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
                return False , "Data de pagam,ento inválida."

                    




            
            

            

