import random
import json
import datetime


lado = int(input("coloque o numnero de lados  "))

dado = 100

numero_dado = int(input("coloque o numero que vocêq quer"))

roll = []

for i in range (0 , dado):
    faces = random.randint(1, lado)
    roll.append(faces)

count_num = roll.count(numero_dado)

print(roll)
print(count_num)

print("=" * 10)
print("json")
print("=" * 10)

#import json ja tá la em cima


json_string = '''
    {
        “1234”: {
            “nome”: “André Guimarães”,
            “e-mail”: “andre.guim@gmail.com”
        },
        “5678”: {
            “nome”: “Vanessa Barboza”,
            “e-mail”: “vbarboza@yahoo.com”
        },
        “9012”: {
            “nome”: “Renato Amorim”,
            “e-mail”: “ream@hotmail.com”
        },
    }'''

data = json_string

with open("arquivo2.json" , "w") as f:
    json.dumps(data)


print("=" * 10)
print("datatime")
print("=" * 10)

year = int(input('me de um ano  '))
month = int(input('me de um mês  '))
day = int(input('me de um dia  '))
date1 = datetime.date(year, month, day)
data = date1.strftime('%d/%m/%Y')

print(data)

mes = ("int" , "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")

def imprime_escrito() :
    while True:
        if month >= 0 and month <= 13:
            print("Dia", day, "do mês",mes[month], "de", year )
            break
        else:
            print("ERROR")    

imprime_escrito()

##aviso! foi-se colocado "int", pois por algum motivo o codigo estava dando o mes somado com 1, e eu não achei uma maneira de ajeitar
##caso exista, ela seria bem vinda, abraços, Ricardo
