from interfacee.interface import *

def cadastrarNome(lista):

    nome = input("Escreva o nome que deseja cadastrar: ").strip()

    if nome.isdigit():
        print("Isso é um número inteiro, por favor escreva apenas nomes!")
        return
            
    if not nome:
        print("Nome vazio")
        return
               
    lista.append(nome)
    print("Nome Cadastrado com Sucesso!!!")
    sleep(1)

def removerNome(lista):

    if not lista:
        print("A lista está vazia.")
        sleep(1)
        return
    
    print("Nomes Cadastrados:")
    for i, nome in enumerate (lista, start=1):

        print(f"{i} - {nome}")

    remover = input("Digite o número do nome que deseja remover: ").strip()

    if not remover:
        print("Nenhuma opção foi digitada")
        return

    if not remover.isdigit():
        print("Digite apenas npumeros.")
        return
    
    indice = int(remover) - 1

    if indice < 0 or indice >= len(lista):
        print("Índice inválido")
        return

    removido = lista.pop(indice)
    print(f"Nome {removido} removido com sucesso!")

def listarNome(lista):

    linha()
    print("=== Nomes Cadastrados ===".center(40))
    print(lista)
    linha()


def controleMenu():
    lista = []

    try:
  
        while True:

            a = menuPrincipal()

            match a:

                case "1":
                    cadastrarNome(lista)
                
                case "2":
                    removerNome(lista)

                case "3":
                    listarNome(lista)

                case "0":
                    print("Encerrando Sistema! ")
                    return
                
                case _:
                    print("Opção inválida")
    
    except KeyboardInterrupt:
        print("\nInterrompendo Sistema.")