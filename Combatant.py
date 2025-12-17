from config import config


class Combatant:
    def __init__(self, combatant_name, initiative, health, death_savings=0, npc=False, boss=False,
                 legendary_resistance=0,legendary_resistance_used=0,
                 legendary_actions=0,legendary_actions_used=0,
                 legendary_savings=0, legendary_savings_used=0,
                 lair_actions=0, lair_actions_used=0):
        self.combatant_name = combatant_name
        self.initiative = initiative
        self.health = health
        self.death_savings = death_savings
        self.npc = npc
        self.boss = boss
        self.legendary_resistance = legendary_resistance
        self.legendary_resistance_used = legendary_resistance_used
        self.legendary_actions = legendary_actions
        self.legendary_actions_used = legendary_actions_used
        self.legendary_savings = legendary_savings
        self.legendary_savings_used = legendary_savings_used
        self.lair_actions = lair_actions
        self.lair_actions_used = lair_actions_used

    def __eq__(self, other):
        if not isinstance(other, Combatant):
            return False
        return (self.combatant_name == other.combatant_name and
                self.initiative == other.initiative and
                self.health == other.health)

    def __repr__(self):
        return f"Combatant(name={self.combatant_name!r}, initiative={self.initiative}, health={self.health})"

    def __str__(self):
        return f"{self.combatant_name} (Init: {self.initiative}, HP: {self.health})"


    def set_health(self, health):
        config.log(f"-----Setting health to: {health}-----")
        self.health = health

    def set_death_savings(self, death_savings):
        self.death_savings = death_savings

    def use_legendary_resistance(self):
        if self.legendary_resistance_used < self.legendary_resistance:
            self.legendary_resistance_used += 1
            return True
        return False

    def use_legendary_actions(self):
        if self.legendary_actions_used < self.legendary_actions:
            self.legendary_actions_used += 1
            return True
        return False

    def use_legendary_savings(self):
        if self.legendary_savings_used < self.legendary_savings:
            self.legendary_savings_used += 1
            return True
        return False

    def use_lair_actions(self):
        if self.lair_actions_used < self.lair_actions:
            self.lair_actions_used += 1
            return True
        return False