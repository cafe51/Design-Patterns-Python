class Soldier:
    def __init__(self, level):
        self.level = level

    def attack(self):
        return self.level * 1


class Jedi:
    def __init__(self, level):
        self.level = level

    def attackWithSaber(self):
        return self.level * 100


class StarWarsGame:
    def __init__(self, character):
        self.character = character

    def fight_enemy(self):
        print(f"You caused {self.character.attack()} of damage to the enemy")


class AdaptAttack:
    def __init__(self, character):
      self.character = character

    def attack(self):
        if hasattr(self.character, 'attackWithSaber'):
            return self.character.attackWithSaber()
        else:
            return self.character.attack()

# jedi = Jedi(1)           
        
# print( jedi.attackWisthSaber != None)

StarWarsGame(AdaptAttack(Soldier(5))).fight_enemy()
StarWarsGame(AdaptAttack(Jedi(20))).fight_enemy()
