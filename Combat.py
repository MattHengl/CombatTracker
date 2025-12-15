from Combatant import Combatant
import tkinter as tk

class NewCombat:
    def __init__(self, combat_name, combatants=None):
        self.combat_name = combat_name
        self.combatants: list[Combatant] = combatants

'''class CombatGUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.combat_label = tk.Label(self, text="Combat", justify="center", pady=5)
        self.combat_label.pack()'''

def combat(root, new_combat: NewCombat):
    new_combat.combatants.sort(key=lambda combatant: combatant.initiative, reverse=True)
    combat_frame = tk.Frame(root, name="combat_frame")
    combat_frame.pack()

    combat_name_label = tk.Label(combat_frame, text=f"{new_combat.combat_name}", justify="center", pady=5)
    combat_name_label.pack()

    for x in range(len(new_combat.combatants)):
        combat_info_frame = tk.Frame(combat_frame, bd=2, relief="groove", pady=5, padx=5,
                                     name=f"combatant_info_frame_{new_combat.combatants[x].combatant_name}")
        combat_info_frame.pack(pady=5, fill="x")

        combatant_name_label = tk.Label(combat_info_frame, text=f"{new_combat.combatants[x].combatant_name}",
                                        justify="left", pady=2, anchor="w", wraplength=100)
        combatant_name_label.grid(row=x, column=0, sticky="w", padx=2, pady=2)

        health_string_var = tk.StringVar()
        health_string_var.set(f"Health: {new_combat.combatants[x].health}")
        combatant_health_label = tk.Label(combat_info_frame, textvariable=health_string_var)
        combatant_health_label.grid(row=x, column=1, padx=2, pady=2)

        combatant_damage_label = tk.Label(combat_info_frame, text=f"Damage: ")
        combatant_damage_label.grid(row=x, column=2, sticky="e", padx=2, pady=2)

        combatant_damage_entry = tk.Entry(combat_info_frame, width=10)
        combatant_damage_entry.grid(row=x, column=3, sticky="e", padx=2, pady=2)

        combat_info_frame.columnconfigure(0, weight=1)
        combat_info_frame.columnconfigure(1, weight=0)
        combat_info_frame.columnconfigure(2, weight=0)
        combat_info_frame.columnconfigure(3, weight=0)

        combatant_damage_entry.bind('<Return>', lambda event,
                                    hsv=health_string_var,
                                    comb=new_combat.combatants[x],
                                    entry=combatant_damage_entry,
                                    frame=combat_info_frame:
                                    update_health_label(hsv, comb,
                                                        entry, new_combat.combatants,
                                                        frame))

def update_health_label(health_string_var, combatant: Combatant, damage_entry: tk.Entry, combatant_list: list[Combatant], combatant_frame: tk.Frame):
    damage_text = damage_entry.get()
    if damage_text.isdigit():
        damage = int(damage_text)
        new_health = combatant.health - damage
        combatant.set_health(new_health)
        if combatant.health <= 0:
            combatant_list.remove(combatant)
            combatant_frame.pack_forget()
        else:
            health_string_var.set(f"Health: {combatant.health}")
        damage_entry.delete(0, tk.END)