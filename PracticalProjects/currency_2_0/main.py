from tkinter import *
import requests

#Colors
main_color = "#14085f"

#window
window = Tk()
window.minsize(400, 120)
window.resizable(False, False)
window.title("Curr changer 2.0")
window.config(bg=main_color)

#Funx
def count():
    currency_from = drop_down_from.get()
    currency_to = drop_down_to.get()
    ammount = int(user_input.get())

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={ammount}"

    payload = {}
    headers = {
        "apikey": "XAfdvgw7c3hIAaaYGls7TcBHYuxlu7Ee"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response.raise_for_status()
    data_result = response.json()
    result_label.config(text=data_result["result"])

#User input
user_input = Entry(width=20, font=("Arial", 12), justify=CENTER)
user_input.insert(0, "0")
user_input.grid(row=0, column=0, padx= 10, pady =(10, 0))

#Roleta
drop_down_from = StringVar(window)
drop_down_from.set("CZK")
drop_down_from_options = OptionMenu(window, drop_down_from, "EUR", "USD", "CZK")
drop_down_from_options.grid(row=0, column=1, padx=10, pady=(10, 0))

#Roleta - choose curr
drop_down_to = StringVar(window)
drop_down_to.set("EUR")
drop_down_to_options = OptionMenu(window, drop_down_to, "EUR", "USD", "CZK")
drop_down_to_options.grid(row=1, column=1, padx=5, pady=(10, 0))

#button
count_button = Button(text="Recount", font=("Arial", 12), command=count)
count_button.grid(row=0, column=2, padx=10, pady=(10, 0))

#Label
result_label = Label(text="0", bg=main_color, fg="white", font=("Arial", 12))
result_label.grid(row=1, column=0)
#Main ckl
window.mainloop()