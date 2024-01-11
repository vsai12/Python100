from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

km_value = Label(text="0")
km_value.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)


def convert():
    miles = int(miles_input.get())
    km = round(miles * 1.609)
    km_value.config(text=km)


calc_button = Button(text="Calculate", command=convert)
calc_button.grid(row=2, column=1)

window.mainloop()
