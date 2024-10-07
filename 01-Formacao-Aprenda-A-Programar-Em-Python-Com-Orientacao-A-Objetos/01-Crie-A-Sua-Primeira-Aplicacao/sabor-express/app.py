import os


def exibir_nome_do_programa():
    print("""
𝙎𝙖𝙗𝙤𝙧 𝙀𝙭𝙥𝙧𝙚𝙨𝙨
""")


def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair\n")


def finish_app():
    os.system("cls")
    print("Encerrando o programa\n")


def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))

    if opcao_escolhida == 1:
        print("Cadastrar restaurante")
    elif opcao_escolhida == 2:
        print("Listar restaurantes")
    elif opcao_escolhida == 3:
        print("Ativar restaurante")
    else:
        finish_app()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()