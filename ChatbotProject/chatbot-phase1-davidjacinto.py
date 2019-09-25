f_name = input("What is your first name? ")
l_name = input("What is your last name? ")
time = input("What time of day is it (Morning, Afternoon, Evening): ")
greet = "Good " + time + " " + f_name + " " + l_name[:1]
print(greet)
