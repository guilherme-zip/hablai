"""Description 
Equipe.Iteligência ArtificialT3:
-Guilherme Souto Rodrigues
-Raul Ramsés 
-Isabel Luiza
---
Hablai:Sistema de Ouvidoria para registro e gerenciamento de reclamações
---
1.Listar reclamações registradas;
2.Registrar uma nova reclamação;
3.Pesquisar uma reclamação pelo código;
4.Atualizar uma reclamação existente;
5.Remover uma reclamação pelo código;
6.Mostrar a quantidade total de reclamações cadastradas;
7.Opção para sair do sistema.
"""
lista = []
#==Início da definição de funções======
def op1List():
    print("Posição,Reclamação")
    for i in range(len(lista)):
        item = lista[i]  # Acessamos o valor pelo índice
        print (f"{i+1},{item}")
def op2Add():
    while True:
        entrada = input("Digite a reclamação: ").strip().lower()
        if entrada:
            lista.append(entrada)
            index = len(lista) - 1  # posição do item
            print( f"{entrada} adicionada na posição {index+1} da lista.")
        else:print ("Entrada vazia.") 
        try:
            op = int(input(
                "\nDigite 1 para adicionar outra reclamação\n"
                "Digite 2 para voltar ao lobby\n"
                "Opção: "
            ))

            if op == 1:continue
            elif op == 2:break
            else:print("Opção inválida.")
        except ValueError: print("Digite 1 ou 2.")  
def op3Pesq():
    try:
        insert = int(input("Digite\n1-Para pesquisar a reclamação mais recente\n2-Para a reclamação mais antiga\n3-Para uma posição em específico: "))
        if insert == 1:
            ultimo_indice = len(lista) - 1
            print (lista[ultimo_indice])
        elif insert == 2:
            print (lista [0])
        elif insert == 3:
            posi_indice = int(input("Digite qual posição você quer"))
            print (lista[posi_indice])
        else:print ("Valor inválido")
    except ValueError:
            return "Você digitou algum valor inválido"
def op4Update():
    #1.exibe a tabela atual
    for i in range(len(lista)):
        print(f"Índice{i+1},{lista[i]}")
        break
    perg=int(input("Digite qual comentário você quer atualizar.Utilize a posição para encontrar"))
    if 0 <= perg < len(lista):
        nova_lista= lista.append(perg)
    else:
        print( "Item não registrado")
    for i in range(len(nova_lista)):
        print(f"Índice {i+1},{nova_lista[i]}")
def op5Remove():
    for i in range(len(lista)):
        print("Código,Item")
        print({i+1}, {lista[i]})
    perg=int(input("Digite qual comentário você quer remover.Utilize a posição para encontrar"))
    if 0 <= perg < len(lista):
        item = lista.pop(perg)
        print(f"Você acabou de remover {item} ")
    else:
        print("Item não registrado")
    for i in range(len(lista)):
        print("Agora sua lista está \nPosição,Reclamação")
        print({i+1}, {lista[i]})
def op6Total():
    return f"Sua lista tem um total de {len(lista)} elementos."
#==Fim da definição de funções=========
print("Bem vindo ao Hablai...")
while True: #Menu
        try:
            op_menu= int(input("\nEscolha um número referente a opção que desejas:\n1.Listar reclamações registradas\n2.Registrar uma nova \n3.Pesquisar uma reclamação pelo posição\n4.Atualizar uma reclamação existente\n5.Remover uma reclamação pelo código\n6.Mostrar a quantidade total de reclamações cadastradas\n7.Opção para sair do sistema :\n"))
            if op_menu == 1:
                print(f"Estamos executando Listar reclamações registradas:\n")
                print(op1List())
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
                print(f"Estamos executando Mostrar a quantidade total de reclamações cadastradas:\n")
                op6Total()
            elif op_menu == 7:
                print(f"Hasta la vista baby!")
                break
            else:print("Opção inválida,escolha uma opção entre 1 e 7 !")
        except ValueError:
            print("Escolha uma opção válida,deve ser digitado um número entre 1 e 7")
            break