genero = input("Para Homem Digite M \nPara Mulher Digite F\nGenero:")
altura = float(input("Digite sua altura: "))
imcH = (72.7 * altura) - 58
imcM = (62.1 * altura) - 44.7

if genero == "m": print(f"Peso Ideal = {imcH:.2f}")
elif genero == "f": print(f"Peso ideal = {imcM:.2f}")
else: print("Erro")