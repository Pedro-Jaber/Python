from B09_ClassPessoa import Pessoa





if __name__ == '__main__':
    pessoa1 = Pessoa("Carlos", "Pereira", 23)
    pessoa2 = Pessoa("Maria", "Souza", 21)
    #print(pessoa1)
    print(pessoa1)
    print(pessoa2)

    #pessoa1.mostrar_dados()
    #pessoa2.mostrar_dados()

    print("-----------------------------------------\n")

    print(f"Nome: {pessoa1.get_nome()}")
    pessoa1.set_nome("Eduardo")
    print(f"Idade: {pessoa1.get_idade()}")
    pessoa1.set_idade(35)

    print("-----------------------------------------\n")

    print(pessoa1)
    #pessoa1.mostrar_dados()

    print("-----------------------------------------\n")

    pessoa1.mais_velho(pessoa2)


