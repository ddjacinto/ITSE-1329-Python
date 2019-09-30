usertall = input('What is your height in inches? ')
try :
    if int(usertall) >= 48 :
        print('Welcome aboard, enjoy the ride!')
    elif int(usertall) < 48 :
        print('Sorry, you are not tall enough for this ride')
except : 
    print('That is not a valid number')