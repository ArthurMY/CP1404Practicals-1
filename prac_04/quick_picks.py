import random

quick_pick_number = int(input("How many quick picks?"))
for i in range(0, quick_pick_number):
    random_numbers = []
    for j in range(0, 6):
        number = random.randint(1, 45)
        random_numbers.append(number)
    print(str(random_numbers)[1:-1].replace(",", " "))

