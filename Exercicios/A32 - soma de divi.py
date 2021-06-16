





'''
h = 0
numerador = 1
n = int(input("escolha o denominador final: "))

for denominador in range (1,n+1):
    h += numerador/denominador

print(f"H = {h:.5f}")
'''

"""
s = 0
for nume in range (1,10+1):
    deno = nume**2
    s += nume/deno

print("\nS =", s)
"""

s = 0
for nume in range (1,10+1):
    deno = nume**2
    if nume%2 != 0: s+=nume/deno
    elif nume%2 == 0: s-=nume/deno

print(f"\nS = {s:.2f}")