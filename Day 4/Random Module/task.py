import random
rand_num = random.randint(1,10)
print(rand_num)

if rand_num % 2 == 1:
    print("Tails")
else:
    print("Heads")