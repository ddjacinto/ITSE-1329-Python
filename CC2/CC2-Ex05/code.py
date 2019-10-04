hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
if hours > 40:
    overtime = (hours - 40) * (rate * 1.5) 
    regulartime = rate * 40
    pay = overtime + regulartime
    print("Pay:", pay)
if hours <= 40:
    pay = hours * rate
    print("Pay:", pay)