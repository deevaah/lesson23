from tkinter import *


def Call():
    greet = int(name.get())
    label["text"] = greet


def Era(name):
    name.delete(0, END)


window = Tk()
window.geometry("500x500")
label = Label(window, text=0, font=('Arial', 12))
label.place(x=200, y=50, width=120, height=25)
name = Entry(window, width=50, )
name.pack(padx=10, pady=10)
name.place(x=200, y=20, width=120, height=25)
button = Button(window, text="sum", command=Call)
button.place(x=100, y=100, width=120, height=25)
eraese = Button(window, text="eraese", command=Era)
eraese.place(x=300, y=100, width=120, height=25)
window.mainloop()
