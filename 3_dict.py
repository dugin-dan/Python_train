#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
month = int(input("Введите номер месяца (от 1 до 12): "))
season = {1:'зима',2:'зима',3:'весна',4:'весна',5:'весна',6:'лето',7:'лето',8:'лето',9:'осень',10:'осень',11:'осень',12:'зима'}
if (month < 0 or month > 12):
  print('Неправильно введён номер месяца')
else: print(season.get(month - 1)) 