import tkinter as tk 
import random

window = tk.Tk()
window.title("Number Guess")
window.geometry("400x400")
var1=tk.IntVar()
var2=tk.IntVar()


def fun():
    def get_value():
        limit = entry1.get()
        n = entry2.get()
        system_guess = random.randint(0,int(limit))
        print(system_guess)
        if int(n) == system_guess:
            lbl = tk.Label(window,text="Your Guess is Correct ")
            lbl.pack()

    frame1 = tk.Frame(window,bg="red",height=200,width=200)
    lbl1 = tk.Label(frame1,text="Enter Upper limit from 0:")
    lbl1.pack()
    entry1 = tk.Entry(frame1,textvariable=var1)
    entry1.pack()
    lbl2 = tk.Label(frame1,text="Enter Your Guess")
    lbl2.pack()
    entry2 = tk.Entry(frame1,textvariable=var2)
    entry2.pack()
    btn = tk.Button(frame1,command = get_value)
    btn.pack()

    frame1.pack()

fun()


window.mainloop()