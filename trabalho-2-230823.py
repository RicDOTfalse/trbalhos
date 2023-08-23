X = float(input("ensina o ano : "))

ano = (X % 4 == 0) or (X % 100 == 0) or (X % 400 == 0)

print(ano)