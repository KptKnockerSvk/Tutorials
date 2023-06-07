from tkinter import *
import requests

#window
window = Tk()
window.minsize(700, 400)
window.resizable(False, False)
window.title("ISS")

#Funx
def iss_coordinates():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = (data["iss_position"]["latitude"])
    longitude = (data["iss_position"]["longitude"])
    latitude_label.config(text=f" Latitude of ISS is: {latitude}")
    longitude_label.config(text=f" Longitude of ISS is: {longitude}")


#Canvas creation
canvas = Canvas(window, width=500, height=280)
canvas.pack()
iss_img = PhotoImage(file="giphy.gif")
canvas.create_image(0, 0, anchor="nw", image=iss_img)

#Frame
coordinates_frame = Frame(window)
coordinates_frame.pack()

#Button
recount_button = Button(coordinates_frame, text="Current ISS position", command=iss_coordinates)
recount_button.pack()

#Labels
latitude_label = Label()
latitude_label.pack()

longitude_label = Label()
longitude_label.pack()

#Launch
window.mainloop()

# 1xx = ešte nie je koniex
# 2xx = oke
# 3xx = presmerovanie
# 4xx = chyba na strane uživateľa - zlý url
# 5xx = chyba na strane poskytovateľa - nefunkčný server

#print(data["message"])

# print(latitude + "   /a/   " + longitude)