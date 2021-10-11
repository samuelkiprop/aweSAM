import random


def convert_name(name):
    if name == "rock":
        name = 0
    elif name == "paper":
        name = 1
    elif name == "scissors":
        name = 2
    return name


def convert_number(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "paper"
    elif number == 2:
        return "scissors"


def game():
  while True:
    name = input("Rock, Paper, Scissors\n>>").lower()
    number = convert_name(name)
    comp_number = random.randrange(0, 3)
    comp_choice = convert_number(comp_number)
    print(f">>{comp_choice}")

    comp = -int(comp_number)
    play = int(number)
    diff = (comp + play) % 5

    if diff == 1 or diff == 3:
        print("you won!!!")
    elif diff == 0:
        print("draw")
    elif diff == 2 or diff == 4:
        print("you lose!!!")


game()