
list = []


def verifica_conteudo():
    conteudo = True
    if list == []:
        print("[Lista Vazia]")
        conteudo = False
    return conteudo


def menu():
    print("/-/-/-/MENU\-\-\-\ ")
    print(f"\n"
          f"[C] - Creat \n"
          f"[R] - Read  \n"
          f"[U] - Update\n"
          f"[D] - Delete\n"
          f"[E] - Exit")
    opt = input("Opção: ")
    opt.lower()
    return opt


def creat():
    print("/-/-/-/CREAT\-\-\-\ ")
    add = input("Nome: ")
    add = add.capitalize()
    list.append(add)


def read(m=False,n=False):
    if m == True:
        print("/-/-/-/READ\-\-\-\ ")
    if n == True:
        print("Nova Lista: ")

    if verifica_conteudo():
        print("INDEX - NOME")
        for index,nome in enumerate(list):
            print(f"{index:5d} - {nome}")
        print("-------------")

    print("")


def update():
    print("/-/-/-/UPDATE\-\-\-\ ")

    if verifica_conteudo():
        read()
        try:
            index = int(input("Qual o Index que deseja substituir? "))
            nome  =     input("Nome substituto: ")
            nome = nome.capitalize()

            subst = list[index]

            opt = input(f"\nSubstituir {subst} por {nome}? [S/N]\n")
            opt.lower()

            if opt == 's':
                print(f"'{subst}' foi substituido por {nome} na Lista\n")
                list[index] = nome
            elif opt == 'n':
                print(f"'{subst}' NÂO foi substituido por {nome} na Lista\n")
            else:
                print("Comando não encontrado\n")

            read(False,True)

        except IndexError as e:
            print("Error IndexError (O numero indicado NÃO esta na Lista):\n", e)
        except Exception as e:
            print("Error Exception (minha msg2):\n", e)
        print("")

    print("")


def delet():
    print("/-/-/-/DELET\-\-\-\ ")

    if verifica_conteudo():
        read()
        try:
            index = int(input("Qual o Index que deseja DELETAR? "))

            remover = list[index]

            opt = input(f"Remover {remover}? [S/N]")
            opt.lower()

            if opt == 's':
                print(f"'{remover}' foi removido da Lista\n")
                list.pop(index)
            elif opt == 'n':
                print(f"'{remover}' NÂO foi removido da Lista\n")
            else: print("Comando não encontrado\n")

            read(False,True)

        except IndexError as e:
            print("Error IndexError (O numero indicado NÃO esta na Lista):\n", e)
        except Exception as e:
            print("Error Exception (minha msg2):\n", e)
        print("")

    print("")


if __name__ == '__main__':
    while True:
        opt = menu()
        if   opt == 'c':
            print("")
            creat()
        elif opt == 'r':
            print("")
            read(True)
        elif opt == 'u':
            print("")
            update()
        elif opt == 'd':
            print("")
            delet()
        elif opt == 'e':
            print("")
            break
        else: print("Comando não encontrado")
