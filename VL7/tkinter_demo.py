import tkinter 

haupt_fenster = tkinter.Tk()
leinwand = tkinter.Canvas(haupt_fenster, width=800, height=450)
leinwand.grid(row=0, column=0, columnspan=2, rowspan=4)

label = tkinter.Label(haupt_fenster, text="Hallo, WI")

button = tkinter.Button(haupt_fenster, text="Klick mich!", bg="red", fg="white")

button.grid(row=0, column=0)
label.grid(row=1, column=1)

haupt_fenster.mainloop()