from interfacee.interface import *

def cadastrarNome(a):

    nome = input("Escreva o nome que deseja cadastrar: ").strip()

    if nome.isdigit():
        print("Isso é um número inteiro, por favor escreva apenas nomes!")
        return
            
    if not nome:
        print("Nome vazio")
        return
               
    a.append(nome)
    print(a)

        
def controleMenu():

    lista = []

    try:
  
        while True:

            a = menuPrincipal()

            match a:

                case "1":
                    cadastrarNome(lista)

                case "2"
    
    except KeyboardInterrupt:
        print("Interrompendo Sistema.")