from src.model.services.verify import *

class User:

    def __init__(self):

        self.verify = Verify()

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
        fullname = input("Nome completo: ")
        login = input("Login: ")
        password = input("Senha:")
        salary = input("Salário atual: ")
        salary_day = input("Data de pagamento: ")


            










