
a = float(input("Lado A = "))
b = float(input("Lado B = "))
c = float(input("Lado C = "))

if a >= (b + c): print("lado A muito grande")
elif b >= (c + a): print("lado B muito grande")
elif c >= (a + b): print("lado C muito grande")
else:
    if a == b == c:
        print("O triangulo é Equilatero")
    elif a == b or b == c or c == a:
        print("O triangulo é isósceles")
    elif a != b != c:
        print("O triangulo é Escaleno")
    else:
        print("erro")
