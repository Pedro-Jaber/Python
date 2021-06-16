#
#
#
#
#
#
def fat (a):
    c = 1
    for b in range(1,a + 1):
        c *= b
    return c
if __name__ == '__main__':
    valor = int(input("Digite o valor: "))
    print(f"O fatorial de {valor} = {fat(valor)}")