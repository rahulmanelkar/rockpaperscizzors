from entity import Entity
from collections import namedtuple


class Rules:
    def __init__(self):
        self.__Logic_3_entities = namedtuple('Logic_3_entities',['win','lose'])
        self._rule_dict = {Entity.ROCK: self.__Logic_3_entities(Entity.SCISSORS,Entity.PAPER),
                           Entity.PAPER: self.__Logic_3_entities(Entity.ROCK,Entity.SCISSORS),
                           Entity.SCISSORS: self.__Logic_3_entities(Entity.PAPER,Entity.ROCK)}

    @property
    def rule_dict(self):
        return self._rule_dict
    
    @rule_dict.setter
    def rule_dict(self,new_rules):
        if not isinstance(new_rules,dict):
            raise TypeError("Need to pass in rule dictionary")
        self._rule_dict=new_rules

    
        

if __name__=="__main__":
    rule = Rules()
    print(rule.rule_dict)


