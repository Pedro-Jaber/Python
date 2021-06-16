'''
print("Equação Ax + B = 0")
a = int(input("A:"))
b = int(input("B:"))

if a == 0:
    print("Não é possivel dividir por zero")
else:
    x = ((-b) / a)
    print(f"A raiz é: {x}")
'''




import math
a =float(input("a:"))
if a == 0:
    print("Não é possivel dividir por zero")
else:
    b =float(input("b:"))
    c =float(input("c:"))
    delta = b**2-4*a*c
    if delta < 0:
        print("Não existe rais nos reais")
    else:
        x1 = (-b + (math.sqrt(delta))) / (2 * a)
        x2 = (-b - (math.sqrt(delta))) / (2 * a)

        if delta == 0:
            print("Duas raizes iguais")
            print(f"As raizes são: x1 = {x1:.4f}, x2 = {x2:.4f} ")

        elif delta > 0:
            print(f"As raizes são: x1 = {x1:.4f}, x2 = {x2:.4f} ")

        else: print("erro")









