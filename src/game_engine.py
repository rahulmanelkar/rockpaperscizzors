from entity import Entity
import random

class Game:
    def __init__(self, players: list[str]):
        self.players = players

    def get_move(self, player='AI'):
        if player=='AI':
            return 
        return random.choice(list(Entity))
    
    