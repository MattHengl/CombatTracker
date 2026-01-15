import combat_state
from Combatant import Combatant
from config import config
import tkinter as tk


def extract_combatant_data(frame):
    combatant_name = ""
    initiative = ""
    health = ""

    for widget in frame.winfo_children():
        if hasattr(widget, 'winfo_name') and hasattr(widget, 'get'):
            widget_name = widget.winfo_name()
            if "combatant_name" in widget_name:
                combatant_name = widget.get()
            elif "combatant_initiative" in widget_name:
                initiative = widget.get()
            elif "combatant_health" in widget_name:
                health = widget.get()
    return {
        'name': combatant_name,
        'initiative': initiative,
        'health': health
    }

def save_button_logic(frame):
    data = extract_combatant_data(frame)
    combatant = validate_and_create_combatant(data['name'], data['initiative'], data['health'])
    if combatant:
        config.log(f"-----Adding {combatant} to combatants-----")
        if any(c.combatant_name.lower() == data['name'].lower() for c in combat_state.combatant_list):
            warning_window = tk.Toplevel(frame)
            warning_window.title("Warning")
            warning_label = tk.Label(warning_window, text="Combatant already exists and cant be added.",
                                     pady=10, padx=10, fg="red")
            warning_label.pack()
            ok_button = tk.Button(warning_window, text="OK", width=10, command=warning_window.destroy)
            ok_button.pack(pady=5)
            config.log(f"-----Could not add combatant {data['name']} because they already exist-----")
        else:
            combat_state.combatant_list.append(combatant)

def validate_and_create_combatant(combatant_name, initiative, health):
    if combatant_name and initiative.isdigit() and health.isdigit():
        config.log(f"-----Combatant: {combatant_name, initiative, health}-----")
        return Combatant(combatant_name, int(initiative), int(health))
    return None