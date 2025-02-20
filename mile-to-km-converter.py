from tkinter import *

def convertor():
    x = round(float(entry.get()) * 1.609, 2)
    km_value_label.config(text=str(x))


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

#Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

#Label
km_value_label = Label(text="0")
km_value_label.grid(column=1, row=1)

#Entry
entry = Entry()
entry.grid(column=1, row=0)

#Button
button = Button(text="Click Me", command=convertor)
button.grid(column=1, row=2)















window.mainloop()