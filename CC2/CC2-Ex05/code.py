hours = input('Enter hours: ')
rate = input('Enter rate: ')
if float(hours) > 40 :
    pay = (float(hours) - 40) (float(rate) * 1.5)
if float(hours) <= 40:
    pay = float(hours) * float(rate)
print(pay)
