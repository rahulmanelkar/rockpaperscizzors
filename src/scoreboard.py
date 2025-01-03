from typing import Any

class Scoreboard:
    def __init__(self, points:dict[str,int] | Any = None):
        if points == None:
            self.points: dict[str,int] = dict()
        else:
            self.points: dict[str,int] = points

    def register_player(self,player_name :str):
        self.points.update({player_name:0})

    def update_points(self, player_name: str, increment:int = 0):
        if player_name not in self.points.keys():
            raise KeyError("Missing player name")
        self.points[player_name] += increment 

    def return_score(self):
        return self.points



