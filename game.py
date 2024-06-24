import random

print("How many pencils would you like to use:")

while True:
    try:
        number = int(input())
        if number > 0:
            break
        else:
            print('The number of pencils should be positive')
    except ValueError:
        print("The number of pencils should be numeric")

print("Who will be the first (Jack, John):")
name = input()
possible_names = ['Jack', 'John']

while name not in possible_names:
    print("Choose between 'Jack' and 'John'")
    name = input()

other_name = [n for n in possible_names if n != name][0]

print(f'{"|" * number}')

turns = 1 if name == possible_names[0] else 0

while number > 0:
    if turns % 2 == 1:
        player = name
    else:
        player = other_name

    if player == "John":
        print("John's turn!")
        take = input()
        while take not in ['1', '2', '3']:
            print("Possible values: '1', '2' or '3'")
            take = input()
        take = int(take)
        if take > number:
            print("Too many pencils were taken")
            take = int(input())
        number -= take
    if player == "Jack":
        print("Jack's turn:")
        if number % 4 == 0:
            take = 3
        elif number == 3:
            take = 2
        elif number % 4 == 0:
            take = 1
        elif (number + 1) % 4 == 0:
            take = 2
        elif number == 1 or number == 2:
            take = 1
        else:
            take = random.randrange(1, 3, 1)
        print(take)
        number -= take
    turns += 1

    if number != 0:
        print(f'{"|" * number}')
    else:
        break

winner = name if turns % 2 == 1 else other_name
print(f"{winner} won!")
