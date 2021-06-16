'''
    for i in range(1, (x + 1)):
        if i == 1:
            print(f"ja repeti {i} vez")
        elif i <= 999:
            print(f"ja repeti {i} vezes")
        elif i == 1000:
            print(f"ja repeti {i} vezes e não vou repetir mais")
'''

x = int(input("Quantas vezes: "))

if x == 0:
    print("Não vou repetir")
elif x == 1:
    for i in range(x): print("so vou repetir 1 vez")
elif x <= 1000:
    for i in range(1, (x + 1)):
        if i == 1:
            print(f"ja repeti {i} vez")
        else:
            print(f"ja repeti {i} vezes")
elif x > 1000:
    i = 1
    while i <= 1000:
        if i == 1:
            print(f"ja repeti {i} vez")
        elif i < 1000:
            print(f"ja repeti {i} vezes")
        elif i == 1000:
            print(f"ja repeti {i} vezes e não vou repetir mais")
        i += 1
