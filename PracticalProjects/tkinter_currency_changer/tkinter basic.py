import tkinter

#Screen
window = tkinter.Tk()
window.title("Window of Origin")
window.minsize(width=500, height=400)
window.resizable(False, False )
window.iconbitmap("icon.ico")
window.config(bg="red")

window2 = tkinter.Tk()
window2.title("Window of copyright")
#window2.minsize(width=500, height=400)
window2.geometry("300x400+100+200")
window2.iconbitmap("icon.ico")
window2.resizable(False, False )
window2.config(bg="blue")

# Label
greet_label = tkinter.Label(window, text="Hello there!", bg="black", fg="white", font=("Helvetica", 18, "bold")) #italic - kurzíva
greet_label.pack(side="top")

#Main cycle
window.mainloop()