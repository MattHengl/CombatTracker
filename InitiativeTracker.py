class InitiativeTracker:
    def __init__(self):
        self.initiatives = []

    def add_initiative(self, combatant):
        self.initiatives.append(combatant)
        self.initiatives.sort(key=lambda x: x.initiative, reverse=True)