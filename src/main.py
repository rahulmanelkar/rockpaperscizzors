from entity import Entity
from scoreboard import Scoreboard

def play():
    '''Play the game'''
    print("Playing against AI")
    name=input("What is your name?:")
    print(f'Hello {name}')
    return name

if __name__=="__main__":
    play()