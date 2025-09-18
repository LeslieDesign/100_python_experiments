print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
myAge = int(input("How old are you? "))

if height >= 120:
    if myAge < 12:
        print ("Your ticket will be $5.00")
    elif myAge < 18:
        print ("Your ticket will be $8.00")
    elif myAge > 18:
        print("Your ticket will be $12.00")
else:
    print("Sorry you have to grow taller before you can ride.")
