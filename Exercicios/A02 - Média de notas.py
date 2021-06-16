

#Média de notas
'''
nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
nota3 = float(input("nota 3: "))
media = ((nota1*1) + (nota2*2) + (nota3*3)) /6
print("\n\n\nMédia =", media)
print("nota 1:", nota1)
print("nota 2:", nota2)
print("nota 3:", nota3)

if media >= 5:
    print("Aluno Aproado")
else:
    print("Aluno Reprovado")
'''


nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
media = (nota1*3 + nota2*5)/8
print("\n\nNota 1:", nota1)
print("Nota 2:", nota2)

if media >= 5:
    print(f"Media: {media:.3f} ", "Aprovado")
else: print (f"Media: {media:.3f} ", "Reprovado")