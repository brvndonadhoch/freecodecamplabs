class GameCharacter:
    def __init__(self, _name):
        self._name = _name
        self._health = 100
        self._mana = 50
        self._level = 1
    
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, health):
        if health < 0:
            self._health = 0
        if health in range(0, 101):
            self._health = health
    
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, mana):
        if mana < 0:
            self._mana = 0
        if mana > 50:
            self._mana = 50
        if mana in range (0, 51):
            self._mana = mana
    
    @property
    def level(self):
        return self._level
    
    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self._level}!")
    
    def __str__(self):
        return(f"""Name: {self.name}
Level: {self.level}
Health: {self.health}
Mana: {self.mana}
        """)

