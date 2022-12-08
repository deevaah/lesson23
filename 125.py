from tkinter import *
import random
def Call():
    num = random.randint(1, 6)
    x = random.randint(1, 400)
    y = random.randint(1, 400)
    width= random.randint(1, 200)
    height = random.randint(1, 200)
    label = Label(text=num, font=('Arial 24'))
    label.place(x=x, y=y, width=width, height=height)
    label["bg"] = "grey"
    label["fg"] = "black"

window = Tk()
window.geometry("500x500")
button = Button(text = "Start", command = Call)
button.place(x = 200, y = 100, width = 120, height = 25)
window.mainloop()