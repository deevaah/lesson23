from tkinter import *
def Call():
    greet = "Hello " + name.get()
    label = Label(window, text=greet, font=('Arial', 12))
    label.pack(pady=10)
    label.place(x=200, y=50, width=120, height=25)
    label["bg"] = "blue"
    label["fg"] = "white"

window = Tk()
window.geometry("500x500")
name = Entry (window, width=50,)
name.pack(padx=10, pady=10)
name.place(x = 200, y = 20, width = 120, height = 25)
button = Button(text = "Start", command = Call)
button.place(x = 200, y = 100, width = 120, height = 25)
window.mainloop()