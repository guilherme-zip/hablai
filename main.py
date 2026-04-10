from functions import *

#==Fim da definição de funções=========
lista = ["Batata","Palha"]
print("Bem vindo ao Hablai...")
while True: #Menu
        try:
            op_menu = int(input(
            "\n1 - Listar reclamações\n"
            "2 - Registrar nova\n"
            "3 - Pesquisar\n"
            "4 - Atualizar\n"
            "5 - Remover\n"
            "6 - Total\n"
            "7 - Sair\n"
            "Opção: "
        ))
            if op_menu == 1:
                print(f"Estamos executando Listar reclamações registradas:\n")
                op1List()
            elif op_menu == 2:
                print(f"Estamos executando Registrar uma nova reclamação:\n")
                op2Add()
            elif op_menu == 3:
                print(f"Estamos executando Pesquisar uma reclamação pelo código:\n")
                op3Pesq()
            elif op_menu == 4:
                print(f"Estamos executando Atualizar uma reclamação existente:\n")
                op4Update()
            elif op_menu == 5:
                print(f"Estamos executando Remover uma reclamação pelo código:\n")
                op5Remove()
            elif op_menu == 6:
                op6Total()
            elif op_menu == 7:
                print(f"Hasta la vista baby!")
                break
            else:print("Opção inválida,escolha uma opção entre 1 e 7 !")
        except ValueError:
            print("Escolha uma opção válida,deve ser digitado um número entre 1 e 7")