






"""
for dado in range (1,6+1):
    print("lado ", dado)
"""

ct = 0

print("Dado1 - Dado2")
for dado1 in range(1,6+1):
    print("\n")
    for dado2 in range(1,6+1):
        if dado1 + dado2 <= 5:
            ct += 1
            print(dado1, " - ", dado2, end="  ")