# from tkinter import *
#
# # Window
# window = Tk()
# window.title("Task writer")
# window.minsize(450, 400)
# window.iconbitmap("icon.ico")
# window.resizable(False, False)
#
# # Def of fonts n colors
# main_font = ("Times New Roman", 12)
# main_color = "#dd7f00"
# button_color = "#ffbe66"
# window.config(bg=main_color)
#
# # Fucs
# def add_text():
#     list_box.insert(END, user_input.get())
#     user_input.delete(0, END)
#
# def remove_text_item():
#
#
#
# """Frame""""
# input_frame = Frame(window, bg=main_color)
# text_frame = Frame(window, bg=main_color)
# button_frame = Frame(window, bg=main_color)
# input_frame.pack()
# text_frame.pack()
# button_frame.pack()
#
# # Input frame - content
# user_input = Entry(input_frame, width=35, borderwidth=3, font=main_font)
# user_input.grid(row=0, column=0, padx=5, pady=5)
# add_button = Button(input_frame, text="Add", borderwidth=2, font=main_font, bg=button_color, command=add_text)
# add_button.grid(row=0, column=1, ipadx=10, pady=5)
#
# # Scrollbar
# text_scrollbar = Scrollbar(text_frame)
# text_scrollbar.grid(row=0, columns=1, sticky=NS)
#
# # Text frame - content
# list_box = Listbox(text_frame,height=15, width=45, borderwidth=2, font=main_font, yscrollcommand=text_scrollbar.set)
# list_box.grid(row=0, column=0)
# text_scrollbar.config(command=list_box.yview)
#
# # Button frame - content
# remove_button = Button(button_frame, text="Delete", bg=button_color, borderwidth=2, font=main_font)
# clear_button = Button(button_frame, text="Clear", bg=button_color, borderwidth=2, font=main_font)
# save_button = Button(button_frame, text="Save", bg=button_color, borderwidth=2, font=main_font)
# quit_button = Button(button_frame, text="Quit", bg=button_color, borderwidth=2, font=main_font, command=window.destroy)
#
# remove_button.grid(row=0, column=0, padx=2, pady=10, ipadx=6)
# clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=6)
# save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=8)
# quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=8)
#
# # M.L.
# window.mainloop()