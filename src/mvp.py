import random

def game(choice):
    choice_dict = {"R":1,"P":2,"S":3}
    choice_ai = random.randint(1,3)
    if choice_dict[choice] == 1:
        if choice_ai == 1:
            return "Draw"
        elif choice_ai == 2:
            return "AI wins, Paper beats Rock"
        else:
            return "Player wins, Rock beats Paper"
    elif choice_dict[choice] == 2:
        if choice_ai == 2:
            return "Draw"
        elif choice_ai == 2:
            return "AI wins, Scissors beats Paper"
        else:
            return "Player wins, Paper beats Rock"
    else:
        if choice_ai == 3:
            return "Draw"
        elif choice_ai == 1:
            return "AI wins, Rock beats Paper"
        else:
            return "Player wins, Scissors beats Rock"
    

def main():
    print("This is a quick Rock-Paper-Scissors MVP")
    choice = input("Enter choice, R, P ,S")

    result = game(choice)

    print(result)

if __name__=='__main__':
    main()