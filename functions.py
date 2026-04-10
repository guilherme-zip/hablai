lista = []
def op1List():
    print("Posição;Reclamação")
    for i in range(len(lista)):
        item = lista[i]  # Acessamos o valor pelo índice
        print (f"{i+1};{item}")
    
def op2Add():
    while True:
        entrada = input("Digite a reclamação: ").strip().lower()
        if entrada:
            lista.append(entrada)
            index = len(lista) - 1  # posição do item
            print( f"{entrada} adicionada na posição {index+1} da lista.")
            print("Reclamações:")
            op1List()
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
            print (f"A reclamação mais recente da lista foi {lista[ultimo_indice]}")
        elif insert == 2:
            print (f"A reclamação mais antiga da lista foi{lista [0]}")
        elif insert == 3:
            posi_indice = int(input("Digite qual posição você quer"))
            print (f"A reclamação{posi_indice}º é : {lista[posi_indice]}")
        else:print ("Valor inválido")
    except ValueError:
            return "Você digitou algum valor inválido"
def op4Update():
    op1List()#Exibir lista atual
    perg = int(input("Digite a posição: "))
    if 0 < perg <= len(lista):#Verifica se o intervalo é válido 
            novo_item = input("Digite a nova reclamação: ").strip()
            lista[perg-1] = novo_item
    else:
        return ("Posição inválida")
    
    op1List()#Exibir lista pós atualização
def op5Remove():
    print("Código;Item")
    for i in range(len(lista)):
        print(f"{i+1};{lista[i]}")
    perg=int(input("Digite qual comentário você quer remover.Utilize a posição para encontrar: "))
    if 0 <= perg < len(lista):
        item = lista.pop(perg)
        print(f"Você acabou de remover {item} ")
    else:
        print("Item não registrado")
print("Agora sua lista está :")
op1List()
def op6Total():
 return (f"Total de reclamações: {len(lista)}")