from src.model.services.verify import *
from src.model.db.DbController import *

class User:

    def __init__(self):

        self.verify = Verify()
        self.db = Db()

        self.id : str 
        
        self.fullname : str = " "
        self.firstname : str = self.fullname.split(" ")[0]
        self.lastname :str = self.fullname.split(" ")[-1]
        self.login : str 
        self.password_hash : str 

        self.salary : float 
        self.salary_day : int 

        self.debtors : list 
        self.to_pay : float 


    def create(self): #O ideal é criar uma função para cada

        print("Criando usuário:\n")

        while True:

            while True:
                fullname = input("Nome completo: ")
                valid, msg = self.verify.user.fullname(fullname)
                if valid:
                    break
                print(msg)
            self.fullname = fullname
            self.firstname = fullname.split(" ")[0]
            self.lastname = fullname.split(" ")[-1]

            while True:
                login = input("Login: ")
                valid, msg = self.verify.user.login(login)
                if valid:
                    break
                print(msg)
            self.login = login

            while True:
                password = input("Senha:")
                valid, msg = self.verify.user.password(password)
                if valid:
                    break
                print(msg)
            self.password_hash = password  # Ideal: hash a senha

            while True:
                salary = input("Salário atual: ")
                valid, msg = self.verify.user.salary(salary)
                if valid:
                    break
                print(msg)
            self.salary = float(salary)

            while True:
                salary_day = input("Data de pagamento: ")
                valid, msg = self.verify.user.salary_day(salary_day)
                if valid:
                    break
                print(msg)
            self.salary_day = int(salary_day)

            self.db.users.Create.user(self.fullname, self.login, self.password_hash, self.salary, self.salary_day)


        


    def login(self):
        
        print("Insira seus dados:\n")

        login = input("Login: ")
        password = input("Senha: ")

        self.login = login
        self.password_hash = password

        if self.verify.user.login(self.login, self.password_hash):
            print("Login successful!")

        else:
            print("Não foi possível fazer login. Verifique seu login e senha.")













