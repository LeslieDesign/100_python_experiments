print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
your_bill = 0

if size == "S":
    your_bill = 15
    if pepperoni == "Y":
        your_bill += 2
elif size == "M":
    your_bill = 20
    if pepperoni == "Y":
        your_bill += 3
elif size == "L":
    your_bill = 25
    if pepperoni == "Y":
        your_bill += 3
if extra_cheese == "Y":
    your_bill += 1
print(f"Your final bill is: ${your_bill}.")