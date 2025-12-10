from tkinter import *
from Combatant import Combatant

root = Tk()
root.title("Combat Tracker")
root.geometry("400x400")

canvas = Canvas(root)
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

menu_frame = Frame(root)
menu_frame.pack(fill="both", expand=True)
intro = Label(menu_frame, text="Welcome to Combat Tracker", justify="center", pady=10)
intro.pack()

new_combat_frame = Frame(root)

resume_combat_frame = Frame(root)

def new_combat_button_click():
    combatant_list = []

    menu_frame.pack_forget()
    new_combat_frame.pack()
    combatant_button_counter = 0

    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.coords(window_id, canvas.winfo_width() // 2, 0)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    window_id = canvas.create_window((200, 0), window=new_combat_frame, anchor="n")
    #canvas.create_window((0, 0), window=new_combat_frame, anchor="n")
    new_combat_frame.bind("<Configure>", update_scroll_region)
    canvas.bind("<Configure>", update_scroll_region)

    combat_name_label = Label(new_combat_frame, text="Combat name: ", justify="center", pady=5)
    combat_name_label.pack()
    combat_name_entry = Entry(new_combat_frame, width=30)
    combat_name_entry.pack()

    save_combat_button = Button(new_combat_frame, text=f"Save", width=15, command="")
    save_combat_button.pack(pady=15, anchor="s")

    new_combatant_button = Button(new_combat_frame, text="Add Combatant", width=15, command=lambda: (create_combatant_input(), button_click_counter()))
    new_combatant_button.pack(pady=15)

    def button_click_counter():
        nonlocal combatant_button_counter
        combatant_button_counter += 1

    def create_combatant_input():
        combatant_list.append(Combatant("Blank", 0, 0))
        info_frame = Frame(new_combat_frame)
        info_frame.pack(pady=5, anchor="w")

        spacer_label = Label(info_frame, text=f"----------Combatant {combatant_button_counter+1}----------", justify="center", pady=5)
        spacer_label.grid(row=0, column=0, columnspan=2)

        combatant_name_label = Label(info_frame, text="Combatant name: ")
        combatant_name_label.grid(row=1, column=0, padx=2, pady=2)
        combatant_name_entry = Entry(info_frame, width=20)
        combatant_name_entry.grid(row=1, column=1, sticky="w", padx=2, pady=2)

        combatant_initiative_label = Label(info_frame, text="Combatant Initiative: ")
        combatant_initiative_label.grid(row=2, column=0, sticky="w", padx=2, pady=2)
        combatant_initiative_entry = Entry(info_frame, width=20)
        combatant_initiative_entry.grid(row=2, column=1, sticky="w", padx=2, pady=2)

        combatant_health_label = Label(info_frame, text="Combatant Health: ")
        combatant_health_label.grid(row=3, column=0, sticky="w", padx=2, pady=2)
        combatant_health_entry = Entry(info_frame, width=20)
        combatant_health_entry.grid(row=3, column=1, sticky="w", padx=2, pady=2)

        info_frame.columnconfigure(1, weight=1)
        print(f"{combatant_list.__str__()}")

def resume_combat_button_click():
    menu_frame.pack_forget()
    resume_combat_frame.pack(expand=True, fill="both")

    resume_combat_label = Label(resume_combat_frame, text="Combat name: ", justify="center", pady=5)
    resume_combat_label.pack()

    resume_combat_entry = Entry(resume_combat_frame, width=30)
    resume_combat_entry.pack(pady=5)

    resume_combat_button = Button(resume_combat_frame, text="Resume", width=15, command="")
    resume_combat_button.pack(pady=5)

def on_quit():
    root.destroy()

new_combat_btn = Button(menu_frame, text = "Create Combat", width=15,command =new_combat_button_click)
new_combat_btn.pack(pady=5)

resume_combat_btn = Button(menu_frame, text = "Resume Combat", width=15,command =resume_combat_button_click)
resume_combat_btn.pack(pady=5)

quit_btn = Button(menu_frame, text = "Quit", width=15,command =on_quit)
quit_btn.pack(pady=5)

root.mainloop()