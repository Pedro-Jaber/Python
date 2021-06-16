





import random
print("numeros aleatorios")
soma = 0
ct1 = 0
ct2 = 0
ct3 = 0
ct4 = 0
ct5 = 0
ct6 = 0


for i in range (1,60+1):
    numRan = random.randint(1, 6)
    soma += numRan
    print(numRan)
    if numRan == 1: ct1 += 1
    if numRan == 2: ct2 += 1
    if numRan == 3: ct3 += 1
    if numRan == 4: ct4 += 1
    if numRan == 5: ct5 += 1
    if numRan == 6: ct6 += 1


print("tabela:"
      f"\n 1: [{ct1}]" #porcentagem
      f"\n 2: [{ct2}]"
      f"\n 3: [{ct3}]"
      f"\n 4: [{ct4}]"
      f"\n 5: [{ct5}]"
      f"\n 6: [{ct6}]")
print("Soma: ", soma)

"""
for i in range (1,8000+1):
    numRan = random.randint(0, 1)
    soma += numRan
    print(numRan, end="")
    if numRan == 1: ct1 += 1
    if numRan == 2: ct2 += 1
    if numRan == 3: ct3 += 1
    if numRan == 4: ct4 += 1
    if numRan == 5: ct5 += 1
    if numRan == 6: ct6 += 1
"""
