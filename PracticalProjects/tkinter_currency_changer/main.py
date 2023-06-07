from tkinter import *

# Win
window = Tk()
window.title("Currency changer")
window.minsize(300, 200)
window.resizable(False, False)
window.config(bg="#061856")
window.iconbitmap("icon.ico")

# Funcs
def count_currency():
    amount_eur = float(amount_input.get()) / 24.58
    result_label["text"] = round(amount_eur, 2)

# Label
czk_label = Label(text="CZK", font=("Helvetica", 15), bg="#061856", fg="white")
czk_label.grid(row=0, column=1)

result_label = Label(text="0", font=("Helvetica", 15), bg="#061856", fg="white")
result_label.grid(row=1, column=0)

eur_label = Label(text="Eur", font=("Helvetica", 15), bg="#061856", fg="white")
eur_label.grid(row=1, column=1)


# Button
count_button = Button(text="Recount", font=("Helvetica", 15), command=count_currency)
count_button.grid(row=0, column=2, padx=10, pady=10)

# Input
amount_input = Entry(width=10, font=("Helvetica", 15))
amount_input.grid(row=0, column=0, padx=10, pady=10)


# M.L.
window.mainloop()