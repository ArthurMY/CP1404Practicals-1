import random

quick_pick_number = int(input("How many quick picks?"))
for i in range(0, quick_pick_number):
    random_numbers = []
    for j in range(0, 6):
        number = random.randint(1, 45)
        random_numbers.append(number)
        filtered_numbers = []
        [filtered_numbers.append(x) for x in random_numbers if x not in filtered_numbers]
        [filtered_numbers.append(random.randint(1, 45)) for x in random_numbers if len(filtered_numbers) < 6]
    print(str(filtered_numbers)[1:-1].replace(",", " "))

