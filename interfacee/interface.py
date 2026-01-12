from time import sleep

def linha():
    print("~" * 40)

def menuPrincipal():

    linha()
    print("Bem Vindo ao Nosso Sistema de Cadastro".center(40))
    linha()
    sleep(1)

    print("====CADASTRO DE NOMES====".center(40))

    print("1 - Cadastrar Pessoa")
    print("2 - Remover Nome")
    print("3 - Listar Nome")
    print("0 - Sair")

    a = input("O que você deseja acessar: ")
    return a