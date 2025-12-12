from Combatant import Combatant
import tkinter as tk

class NewCombat:
    def __init__(self, combat_name, combatants=None):
        self.combat_name = combat_name
        self.combatants: list[Combatant] = combatants

class CombatGUI(tk.Frame):
    def __init__(self, parent, combat=None):
        super().__init__(parent)

        parent.pack_forget()
        combat_label = tk.Label(self, text="Combat", justify="center", pady=5)
        combat_label.pack()



