from Combatant import Combatant
import tkinter as tk
from config import config


def update_health_label(health_string_var, combatant: Combatant, damage_entry: tk.Entry,
                        combatant_list: list[Combatant], combatant_frame: tk.Frame):
    try:
        incoming_damage = [damage_entry.get()[0], int(damage_entry.get()[1:])]
        if incoming_damage[0] == '+':
            new_health = combatant.health + int(incoming_damage[1])
        else:
            new_health = combatant.health - int(incoming_damage[1])
        config.log(f"-----Updating health from {combatant.health} to {new_health}-----")
        combatant.set_health(new_health)
        if combatant.health <= 0:
            combatant_list.remove(combatant)
            combatant_frame.pack_forget()
        else:
            health_string_var.set(f"Health: {combatant.health}")
        damage_entry.delete(0, tk.END)
    except Exception as e:
        config.log("-----Error updating health-----")
        config.log(f"-----{e}-----")