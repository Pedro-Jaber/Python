






def maiu_minu(l):
    if l.isupper():   # isupper() e islower() verifica se a palavra é maiuscula ou minuscula
        l = l.lower()
        return l
    elif l.islower():
        return l
    else: return "n ta top"

def minu_maiu(l):
    if l.islower():
        return l.upper()
    elif l.isupper():
        return l
    else: return "n ta top"


if __name__ == '__main__':
    a = input("Letra: ")
    print("letra ", minu_maiu(a))