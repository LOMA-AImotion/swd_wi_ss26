import tkinter 
from tkinter import messagebox
haupt = tkinter.Tk()

def sag_servus():
    print("Servus WI!")
    messagebox.showwarning("THI SWD", "Servus")

button = tkinter.Button(haupt, text="Sag Servus", command=sag_servus)
button.pack()
haupt.mainloop()