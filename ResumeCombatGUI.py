from tkinter import *


def resume_combat_button_click(menu_frame,resume_combat_frame, display_warning):
    display_warning("Functionality now implemented yet. Sorry.")

    menu_frame.pack_forget()
    resume_combat_frame.pack(expand=True, fill="both")

    resume_combat_label = Label(resume_combat_frame, text="Combat name: ", justify="center", pady=5)
    resume_combat_label.pack()

    resume_combat_entry = Entry(resume_combat_frame, width=30)
    resume_combat_entry.pack(pady=5)

    resume_combat_button = Button(resume_combat_frame, text="Resume", width=15, command="")
    resume_combat_button.pack(pady=5)