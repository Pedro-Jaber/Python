from B07_ClassCarro import Carro





if __name__ == '__main__':

    carro1 = Carro("HB", 2018, 50000)
    #carro2 = Carro("BMW", 2010, 500000)

    print("Crie seu carro")

    modelo =       input("Modelo: ")
    ano    =   int(input("Ano:    "))

    carro2 = Carro(modelo,ano)

    valor = float(input("Valor:  "))
    carro2.set_valor(valor)


    ###################################################
    carro1.set_valor(45000)
    carro1.set_modelo("TOP_D+")
    ###################################################
    print("\n")

    print("CARRO 1")
    carro1.mostra_info()

    print("\n")

    print("CARRO 2")
    carro2.mostra_info()

    print("\n------------------------------------------\n")


    aument_valor = float(input("Digite o valor para aumentar o preço: "))

    carro2.aumenta_valor(aument_valor)

    print("CARRO 1")
    carro1.mostra_info()

    print("\n")

    print("CARRO 2")
    carro2.mostra_info()

    print("\n")

    carro1.compara_valor(carro2)