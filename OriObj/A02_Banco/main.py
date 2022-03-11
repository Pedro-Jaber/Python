from os import system
import funcoes_main
# system('cls')
print("")

status = True

while status:
    evento = funcoes_main.bem_vindo()
    if evento == "parar":  #fazer para outros menus
        status = False
        pass
    elif evento == "1":
        print("")
        funcoes_main.entrar_conta()
        pass
    elif evento == "2":
        print("")
        funcoes_main.criar_conta()
        pass

    #system('cls') #limpa a tela
    print("")




