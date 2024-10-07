import os

print("""
𝙎𝙖𝙗𝙤𝙧 𝙀𝙭𝙥𝙧𝙚𝙨𝙨
""")

print("1. Cadastrar Restaurante")
print("2. Listar Restaurante")
print("3. Ativar Restaurante")
print("4. Sair\n")

opcao_escolhida = int(input("Escolha uma opção: "))

def finish_app():
    os.system("cls")
    print("Encerrando o programa\n")

if opcao_escolhida == 1:
    print("Cadastrar restaurante")
elif opcao_escolhida == 2:
    print("Listar restaurantes")
elif opcao_escolhida == 3:
    print("Ativar restaurante")
else:
    finish_app()