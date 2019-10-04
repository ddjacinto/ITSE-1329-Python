hours = input('Enter hours: ')
rate = input('Enter rate: ')
try:
    fhours = float(hours)
    frate = float(rate)
    if fhours > 40:
        overtime = (fhours - 40) * (frate * 1.5) 
        regulartime = frate * 40
        pay = overtime + regulartime
        print("Pay:", pay)
    if fhours <= 40:
        pay = fhours * frate
        print("Pay:", pay)
except:
    if rate or hours != float:
        print("Error, please enter numeric input")
        quit()
    
    
    