from Combatant import Combatant

class Combat:
    def __init__(self, combat_name):
        self.combat_name = combat_name
        self.combatants: list[Combatant] = []

