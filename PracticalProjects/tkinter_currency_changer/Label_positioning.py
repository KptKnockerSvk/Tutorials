from tkinter import *

# Window
window = Tk()
window.title("Currency changer")
window.minsize(500, 500)
window.resizable(False, False)

# Label
# pack = málo variabilný
# place = x,y
# grid = aj aj
label_1 = Label(text="First one", font=("Helvetica", 20))
label_1.grid(row=0, column=0)
# label_1.place(x=0, y=0)
# label_1.pack(side="bottom")

label_2 = Label(text="Second one", font=("Helvetica", 20))
# label_2.place(x=200, y=200)
# label_2.pack(side="left")

label_3 = Label(text="Third one", font=("Helvetica", 20))
label_3.place(x=300, y=300)
# label_3.pack(side="right")



# Main loop
window.mainloop()