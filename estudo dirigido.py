
def numeros_legais(x) :
    if isinstance(x , int):
        numero1 = 1
    while numero1 <= x:
        numero2 = 1
        texto = ''
        while numero2 <= x:
            texto += str(numero2) + '\t'
            numero2 += 1
        print(texto)
        numero1 += 1


x = int(input("coloque o numero escolhido"))

numeros_legais(x)

print("=" * 30)
print("=" * 30)
print("parte 2")
print("=" * 30)
print("=" * 30)
def Ferb (Z) :
    F = str(Z)
    if len(F) > 1:
        if F[0] == '0' :
            return len(F) - 1
        else :
            return len(F)
    return len(F)

Z = int(input("coloque um numero"))

print(Ferb(Z))

print("=" * 30)
print("=" * 30)
print("parte 3")
print("=" * 30)
print("=" * 30)

A = int(input("me de um numero inteiro"))

B = int(input("agora me de outro numero"))

conta = (A / B)

print(conta)

print("=" * 30)
print("=" * 30)
print("FIM")
print("=" * 30)
print("=" * 30)

