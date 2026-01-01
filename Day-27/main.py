"""GUI"""
import tkinter


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I Am a Lable", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


add(3, 5, 6 ,7)