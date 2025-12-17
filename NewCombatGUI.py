from tkinter import *
import combat_state
from config import config
from Combat import NewCombat
import NewCombatLogic
import Combat


def new_combat_button_click(root, canvas, scrollbar, new_combat_frame, display_warning, intro):
    combatant_frames = []
    config.log("-----In new_combat_button_click method-----")

    new_combat_frame.pack()
    combatant_button_counter = 0

    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.coords(window_id, canvas.winfo_width() // 2, 0)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    window_id = canvas.create_window((200, 0), window=new_combat_frame, anchor="n")
    new_combat_frame.bind("<Configure>", update_scroll_region)
    canvas.bind("<Configure>", update_scroll_region)

    combat_name_label = Label(new_combat_frame, text="Combat name: ", justify="center", pady=5)
    combat_name_label.pack()
    combat_name_entry = Entry(new_combat_frame, width=30)
    combat_name_entry.pack()

    save_combat_button = Button(new_combat_frame, text=f"Save", width=15, command=lambda: save_combat_button_click())
    save_combat_button.pack(pady=15, anchor="s")

    button_container = Frame(new_combat_frame)
    button_container.pack()

    new_combatant_button = Button(button_container, text="Add Combatant", width=15,
                                  command=lambda: (create_combatant_input(), button_click_counter()))
    new_combatant_button.pack(pady=10, padx=10)

    def button_click_counter():
        nonlocal combatant_button_counter
        combatant_button_counter += 1

    def remove_combatant_input(button_info, frame_info):
        config.log("-----Removing a combatant-----")
        frame_info.pack_forget()
        combatant_frames.remove(frame_info)
        nonlocal combatant_button_counter
        print(button_info.winfo_name())

    def create_combatant_input():
        config.log("-----Adding a combatant-----")
        info_frame = Frame(new_combat_frame, name=f"combatant_frame_{combatant_button_counter+1}", bd=2, relief="groove")
        info_frame.pack(pady=5, anchor="w")
        combatant_frames.append(info_frame)

        spacer_label = Label(info_frame, text=f"----------Combatant----------", justify="center", pady=5)
        spacer_label.grid(row=0, column=0, columnspan=2)

        combatant_name_label = Label(info_frame, text="Name: ")
        combatant_name_label.grid(row=1, column=0, sticky="w", padx=2, pady=2)
        combatant_name_entry = Entry(info_frame, width=20, name=f"combatant_name_{combatant_button_counter+1}")
        combatant_name_entry.grid(row=1, column=1, sticky="w", padx=2, pady=2)

        combatant_initiative_label = Label(info_frame, text="Initiative: ")
        combatant_initiative_label.grid(row=2, column=0, sticky="w", padx=2, pady=2)
        combatant_initiative_entry = Entry(info_frame, width=20, name=f"combatant_initiative_{combatant_button_counter+1}")
        combatant_initiative_entry.grid(row=2, column=1, sticky="w", padx=2, pady=2)

        combatant_health_label = Label(info_frame, text="Health: ")
        combatant_health_label.grid(row=3, column=0, sticky="w", padx=2, pady=2)
        combatant_health_entry = Entry(info_frame, width=20, name=f"combatant_health_{combatant_button_counter+1}")
        combatant_health_entry.grid(row=3, column=1, sticky="w", padx=2, pady=2)

        remove_combatant_button = Button(info_frame, name=f"remove_combatant_{combatant_button_counter + 1}",
                                         text="Remove Combatant", width=15,
                                         command=lambda: remove_combatant_input(remove_combatant_button, info_frame))
        remove_combatant_button.grid(row=4, column=0, columnspan=2, pady=10)

        info_frame.columnconfigure(1, weight=1)

    def save_combat_button_click():
        combat_name = combat_name_entry.get()

        for frame in combatant_frames:
            NewCombatLogic.save_button_logic(frame)
        if combat_name:
            if combat_state.combatant_list:
                new_combat = NewCombat(combat_name, combat_state.combatant_list)
                intro.config(text=f"{new_combat.combat_name} has been saved!")
                new_combat_frame.pack_forget()
                canvas.pack_forget()
                scrollbar.pack_forget()
                config.log("-----Moving to combat-----")
                Combat.combat(root, new_combat)
            else:
                display_warning("No valid combatants to add!")
        else:
            display_warning("Combat name cannot be empty!")