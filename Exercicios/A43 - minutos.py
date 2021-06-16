





def hora_min(hora, min):
    hora *= 60
    return hora + min

def ler():
    a = int(input("digite: "))
    return a

def texto():
    print("ola mundo")

#def ler2():


if __name__ == '__main__':
    h = ler() #int(input("Horas: "))
    m = ler() #int(input("Mins: "))
    temp1 = hora_min(h, m)
    print(f"{h:02d}:{m:02d} em minutos é {temp1}")

    h2 = ler()
    m2 = ler()
    temp2 = hora_min(h2, m2)
    print(f"{h2:02d}:{m2:02d} em minutos é {temp2}")

    print("------------------------------")
    print(f"A diferença é de {abs(temp1 - temp2):5d} minutos")
    print("------------------------------")















