from datetime import date
data_atual = date.today()
ano_atual = data_atual.strftime('%Y')
ano_nasc = int(input("Digite seu ano de nascimento: "))

idade = int(ano_atual) - ano_nasc

if (idade <= 9):
   print("de acordo com sua idade {} Sua categoria é MIRIM! ".format(idade))
elif (idade > 9 and idade <= 14):
   print("De acordo com sua idade {} sua categoria é INFANTIL".format(idade))
elif (idade > 14 and idade <= 19):
   print("De acordo com sua idade {} sua categoria é JUNIOR".format(idade))
elif (idade == 20):
   print("De acordo com sua idade {} sua categoria é SÊNIOR".format(idade))
else:
   print("De acordo com sua idade {} sua categoria é MASTER".format(idade))
