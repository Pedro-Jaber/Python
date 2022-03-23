#
#
#
# ( 1 )
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#       A)
"""

lista = []

lista.append(12)

print(lista)

outralista = [2,9,5]
lista.extend(outralista)

print(lista)

lista.insert(4,70)

print(lista)
"""
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#       B)
"""
if 12 in lista:
    index = lista.index(12)
    print(f"O 12 está no index {index}")
"""
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#       C)
"""
crescente = lista
crescente.sort()
print(crescente)
"""
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#       D)
"""
lista.insert(1,55)
print(lista)
"""
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#       E)
"""
decrescente = lista
decrescente.sort(reverse=True)
print(decrescente)
"""
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#       F)

"""
Separe os digitos de cada numero da lista e retire os repetidos e o '0'
no final deixe a lista em ordem crescente
"""
"""
num_str = ''

for i in range(6):
    num_str += str(lista[i])
lista = []

for i in range(0,len(num_str)):
    if int(num_str[i]) not in lista and int(num_str[i]) != 0:
        lista.append(int(num_str[i]))

lista.sort()
print(lista)
"""
#
#
#
# ( 2 )
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""
Crie uma função de tranferencie e uma de juntar contas onde ira juntar as contas de duas pessoas
"""
"""
class Conta:

    def __init__(self,titular,num,saldo=1000):
        self.titular = titular
        self.num = num
        self.saldo = saldo

    def __str__(self):
        return f"Titular = {self.get_titular()}\n" \
               f"Numero  = {self.get_num()}\n" \
               f"Saldo   = {self.get_saldo()}\n"

    def get_titular(self):
        return self.titular

    def set_titular(self, n_nome):
        self.titular = n_nome

    def get_num(self):
        return self.num

    def set_num(self, n_num):
        if 0 < n_num > 9999:
            self.num = n_num
        else: print("Numero Invalido")

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, n_saldo):
        if n_saldo < 0:
            self.saldo = n_saldo
        else: print("[Numero invalido]")

    def depositar(self, valor):
        if valor > 5000:
            print("Deposito maior do que o permitido")
        elif 0 < valor <= 5000:
            self.saldo += valor
            print("Operação concluida")
        elif valor <= 0:
            print("Tente fazer um saque")

    def transferencia(self,valor,destino):
        self.saldo -= valor
        destino.saldo += valor

    def juntar_contas(self, conta2):
        self.titular = f"{self.titular} - {conta2.titular}"
        self.saldo = self.saldo + conta2.saldo

        conta2.titular = "none"
        conta2.saldo   = 0
        conta2.num     = "none"

if __name__ == '__main__':
    conta1 = Conta("Pedro",1000,200)
    conta2 = Conta("Carlos",1002)

    print(f"Titular = {conta1.get_titular()}")
    print(f"Numero  = {conta1.get_num()}")
    print(f"Saldo   = {conta1.get_saldo()}")
    print("")
    print(f"Titular = {conta2.get_titular()}")
    print(f"Numero  = {conta2.get_num()}")
    print(f"Saldo   = {conta2.get_saldo()}")

    print("")

    conta1.depositar(500)
    conta2.depositar(6000)

    print("")
    print(conta1)
    print(conta2)

    conta1.transferencia(150,conta2)

    print("")
    print(conta1)
    print(conta2)

    conta1.juntar_contas(conta2)

    print("")
    print(conta1)
    print(conta2)
    
"""