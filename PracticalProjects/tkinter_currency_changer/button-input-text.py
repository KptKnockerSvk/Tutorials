from tkinter import *

# Window
window = Tk()
window.minsize(500, 500)
window.iconbitmap("icon.ico")
window.title("Currency changer")
window.resizable(False, False)
window.config(bg="black")

# Label
currency = Label(window, text="Eurs!", bg="black", fg="white", font=("Cambria", 25, "bold"), borderwidth=5, relief="sunken")
#currency.pack(ipady= 50) padx / pady - vonkajšie ,,,, ipady/y vnútorné ---pre rám
currency.pack()

#currency2 = Label(window, text="CZK", font=("Cambrie", 20, "bold"), bg="black", fg="white")
#currency2.pack()

# Buttons
def change_text():
    currency["text"] = input_1.get()
    input_1.delete(0, END)

button_1 = Button(text="Click at me", command=change_text, font=("Cambria", 12, "bold"))
button_1.pack()

# Input
input_1 = Entry(width=50, font=("Cambria", 12, "bold"))
input_1.insert(0, string="Ahojda")
input_1.focus()
input_1.pack()
#input_1.get()

# Text field
# text_field = Text(width=40, height=10)
# text_field.focus()
# text_field.pack()
# text_field.get("1.0", END)

# Main cycle
window.mainloop()