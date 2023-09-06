# Salários até R$ 280,00 (incluindo)      Aumento de 20%
 #Salários entre R$ 280,00 e R$ 700,00    Aumento de 15%
 #Salários entre R$ 700,00 e R$ 1500,00   Aumento de 10%
 #Salários de R$ 1500,00 em diante        Aumento de 5%

salario_antes = float(input("coloque aqui seu salario, meu nobre :) /n"))


if salario_antes >= 280.00 :
    salario1 = salario_antes + (salario_antes * 20/100)
    print("o salario antes era de" , salario_antes)
    print("agora após o aumento de 20% o salario  de " , salario1)
elif salario_antes > 280.00 or salario_antes < 700.00 :
    salario2 = salario_antes + (salario_antes * 15/100)
    print("o salario antes era de " , salario_antes)
    print("apos o aumnto de 15% o salario e de" , salario2)
elif salario_antes >= 700.00 or salario_antes <= 1500.00 :
    salario3 = salario_antes + (salario_antes * 10/100) 
    print("o salario antes era de" , salario_antes)
    print("agora após o aumento de 10% o salario  de " , salario3)
elif salario_antes >= 1500.00 :
    salario4 = salario_antes + (salario_antes * 5/100)     
    print("o salario antes era de " , salario_antes)
    print("apos o aumnto de 5% o salario e de" , salario4)
