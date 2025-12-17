import CombatLogic
from Combatant import Combatant
import tkinter as tk

from config import config


class NewCombat:
    def __init__(self, combat_name, combatants=None):
        self.combat_name = combat_name
        self.combatants: list[Combatant] = combatants


def combat(root, new_combat: NewCombat):
    config.log("-----In Combat-----")
    config.log("-----Sorting Combatants-----")
    new_combat.combatants.sort(key=lambda combatant: combatant.initiative, reverse=True)
    combat_frame = tk.Frame(root, name="combat_frame")
    combat_frame.pack()

    menu_bar = root.nametowidget("menu_bar")

    if menu_bar.entrycget(menu_bar.index("end"), "label") != "New Combatant":
        menu_bar.add_command(label="New Combatant", command = lambda: new_combatant_window(root, combat_frame, new_combat))

    combat_name_label = tk.Label(combat_frame, text=f"{new_combat.combat_name}", justify="center", pady=5)
    combat_name_label.pack()

    for x in range(len(new_combat.combatants)):
        config.log("-----Creating Combatant Frame-----")
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
                                    CombatLogic.update_health_label(hsv, comb,
                                                        entry, new_combat.combatants,
                                                        frame))

def new_combatant_window(root, combat_frame, new_combat):
    config.log(f"-----Creating new combat popout window-----")
    new_combatant = tk.Toplevel(root)
    new_combatant.title("New Combatant")
    new_combatant.geometry("250x200")

    new_combatant_frame = tk.Frame(new_combatant)
    new_combatant_frame.pack(pady=20, padx=20, expand=True)

    new_combatant_name = tk.Label(new_combatant_frame, text="Name: ")
    new_combatant_name.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    new_combatant_name_entry = tk.Entry(new_combatant_frame, width=15)
    new_combatant_name_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)

    new_combatant_initiative = tk.Label(new_combatant_frame, text="Initiative: ")
    new_combatant_initiative.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    new_combatant_initiative_entry = tk.Entry(new_combatant_frame, width=15)
    new_combatant_initiative_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

    new_combatant_health = tk.Label(new_combatant_frame, text="Health: ")
    new_combatant_health.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    new_combatant_health_entry = tk.Entry(new_combatant_frame, width=15)
    new_combatant_health_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

    save_button = tk.Button(new_combatant_frame, text="Save", width=10,
                           command=lambda: (save_new_combatant(new_combatant_name_entry.get(),new_combatant_initiative_entry.get(),
                                                               new_combatant_health_entry.get()), new_combatant.destroy()))
    save_button.grid(row=3, column=0, columnspan=2, pady=15)

    def save_new_combatant(name, initiative, health):
        config.log(f"-----Creating now combatant {name, initiative, health}-----")
        new_combat.combatants.append(Combatant(name, int(initiative), int(health)))
        new_combat.combatants.sort(key=lambda combatant: combatant.initiative, reverse=True)
        combat_frame.destroy()
        config.log(f"-----Re-creating combat-----")
        combat(root, new_combat)

