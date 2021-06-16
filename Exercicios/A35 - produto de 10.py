import random



"""
mult = 1

for i in range (1,10 + 1):
    n = int(input(f"numero {prod}: "))
    mult *= n

"""



mult = 1
quantidade = int(input("repetir: "))

for i in range (1,quantidade + 1):
    mult *= int(input(f"numero {i}: "))

print(f"multiplicação final: {mult}")


"""
mult = 1
quantidade = int(input("repetir: "))
numRan = random.randint(1,99)

for i in range (1,quantidade + 1):
    mult *= int(numRan)

print(f"multiplicação final: {mult}")
"""








