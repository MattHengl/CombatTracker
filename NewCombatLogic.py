import combat_state
from Combatant import Combatant
from config import config


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
        combat_state.combatant_list.append(combatant)

def validate_and_create_combatant(combatant_name, initiative, health):
    if combatant_name and initiative.isdigit() and health.isdigit():
        config.log(f"-----Combatant: {combatant_name, initiative, health}-----")
        return Combatant(combatant_name, int(initiative), int(health))
    return None