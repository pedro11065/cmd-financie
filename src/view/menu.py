from src.model.classes.user import *
import os

class Menu:

    def __init__(self):
        
        self.logged = False

        self.user = User()


    def main_menu(self):

        os.system("cls")
        print("\n--- Menu Principal ---\n")
        print("1. Login")
        print("2. Criar Conta")
        print("3. Sair")

        choice = input("\nEscolha uma opção: ")
        os.system("cls")

        if choice == '1':
            self.user.login()

        elif choice == '2':
            self.user.create()

        # if self.user.id:
        #     self.logged = True
        #     self.user.dashboard()
            

        
        
    
                

    