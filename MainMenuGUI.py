from tkinter import *
from NewCombatGUI import new_combat_button_click
from ResumeCombatGUI import resume_combat_button_click

root = Tk()
root.title("Combat Tracker")
root.geometry("400x400")

canvas = Canvas(root, name="main_canvas")
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview, name="main_scrollbar")
canvas.configure(yscrollcommand=scrollbar.set)

menu_frame = Frame(root, name="menu_frame")
menu_frame.pack(fill="both", expand=True)
intro = Label(menu_frame, text="Welcome to Combat Tracker", justify="center", pady=10)
intro.pack()

menu_bar = Menu(root, name="menu_bar")
menu = Menu(menu_bar, tearoff=0)
menu_bar.add_command(label="Menu", command = lambda:(go_to_main_menu(), intro.config(text="Welcome to Combat Tracker")))

new_combat_frame = Frame(root, name="new_combat_frame")
resume_combat_frame = Frame(root, name="resume_combat_frame")

new_combat_btn = Button(menu_frame, text = "Create Combat", width=15,
                        command=lambda: (menu_frame.pack_forget(), new_combat_button_click(root, canvas, scrollbar,
                                                                new_combat_frame, display_warning, intro)))
new_combat_btn.pack(pady=5)

resume_combat_btn = Button(menu_frame, text = "Resume Combat", width=15,
                           command = lambda: resume_combat_button_click(menu_frame, resume_combat_frame))
resume_combat_btn.pack(pady=5)


def on_quit():
    root.destroy()


quit_btn = Button(menu_frame, text = "Quit", width=15,command =on_quit)
quit_btn.pack(pady=5)

root.config(menu = menu_bar)

def go_to_main_menu():
    canvas.pack_forget()
    scrollbar.pack_forget()
    new_combat_frame.pack_forget()
    resume_combat_frame.pack_forget()
    for widget in new_combat_frame.winfo_children():
        widget.destroy()

    try:
        combat_frame = root.nametowidget("combat_frame")
        combat_frame.pack_forget()
        for widget in combat_frame.winfo_children():
            widget.destroy()
        combat_frame.destroy()
    except KeyError:
        pass
    menu_frame.pack(fill="both", expand=True)

def display_warning(text):
    empty_combatant_warning = Toplevel(root)
    empty_combatant_warning.title("Warning")
    warning_label = Label(empty_combatant_warning, text=f"{text}", pady=10, padx=10, fg="red")
    warning_label.pack()
    ok_button = Button(empty_combatant_warning, text="OK", width=10, command=empty_combatant_warning.destroy)
    ok_button.pack(pady=5)

if __name__ == '__main__':
    root.mainloop()