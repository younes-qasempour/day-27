from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 16, "bold"))
my_label.config(text="New Text", padx=10, pady=10)
my_label.grid(column=0, row=0)


#Button
button = Button(text="Click Me", command=button_clicked)
button.config(padx=10, pady=10)
button.grid(column=1, row=1)


#Button
button_2 = Button(text="Click Me", command=button_clicked)
button_2.config(padx=10, pady=10)
button_2.grid(column=2, row=0)


#Entery
input = Entry(width=15)
print(input.get())
input.grid(column=3, row=2)



window.mainloop()