a = float(input("insira A"))

b = float(input("insira B"))

c = float(input("insira C"))

delta = (b**2) - (4*a*c)

if a == 0:
    print("OPA OPA OPA! isso ta errado")
elif delta == 0 or delta <= 0:
    print("para isso ta errado")
else:
    print("a equação pode ser feita")
    ra1 = ((-1 * b) + (delta ** 0.5)) / (2*a)
    ra2 = ((-1 * b) - (delta ** 0.5)) / (2*a)
    print("as raizes são" , ra1 , ra2)