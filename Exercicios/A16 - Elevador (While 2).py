
'''
x = 0
y = 1000
z = 1
m_l = y*z

while x != m_l:
    x += 1
    if x != y+z:
        print(f"{x} é diferente de {m_l}")
    elif x == 1000:
        z += 1
        print(f"{x} é diferente de {m_l}")
    else: print(f"{x} é igual a {m_l}")
    z += 1

'''


'''
x = int(input("digite um número: "))
y = x
x2 = x%2
while x > 0:
    x /= 2 #//=
    print(x, f"antes era {y}")
'''

       # Primeria Forma #
'''--------------------------'''        '''{

PRECO = 'Digite o preço do produto:'
print("Iniciando nova venda...")
total = 0
preço = int(input(PRECO))
while preço != 0:
    total += preço
    preço = int(input(PRECO))
print("Total da venda:", total)
                                        }'''
       # Segunda Forma #
'''--------------------------'''        '''{

print('Iniciando nova venda...')
total = 0
while True:
    preço = int(input('Digite o preço do produto: '))
    if preço == 0:
        break

    total += preço
print("Total da Venda: ", total)
                                        }'''

         # Exercicio 6-1#
'''----------------------------'''

'''Um elevador pequeno suporta uma carga de até 500 kg. Se a carga for excedida, as normas de segurança não serão
cumpridas e há risco de acidentes. Suponha que o elevador esteja vazio e há várias pessoas na fila. Cada pessoa se
pesa e, caso seja possível, entra no elevador. Se o peso de uma pessoa que deseja entrar exceder o que é possível
transportar, então o elevador fecha as portas para ela e faz o trajeto com as que já estão dentro. Escreva um
algoritmo que simule esta situação. Obs.: você vai digitar os valores do peso das pessoas uma por uma, e quando
a soma atingir ou ultrapassar 500, o programa deve parar avisando que o peso foi excedido.'''

from termcolor import colored
pesoT = 0
while True:
    peso = int(input("Qual seu peso?"))
    pesoT += peso
    if pesoT >= 500:
        print(colored(f"Peso excedido ({pesoT} Kg), não entre", 'red'))
        pesoT -= peso
        break
    print(colored("pode entrar\n", 'green'))

print(f"Peso Total: {pesoT} Kg, fechando portas...")