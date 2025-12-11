from Combatant import Combatant

class NewCombat:
    def __init__(self, combat_name, combatants=None):
        self.combat_name = combat_name
        self.combatants: list[Combatant] = combatants

