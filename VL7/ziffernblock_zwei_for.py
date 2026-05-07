import tkinter as tk
haupt_fenster = tk.Tk()
# erstelle Buttons von 1 bis 9 
# 1 2 3
# 4 5 6
# 7 8 9 

def erstelle_button(fenster, zahl, zeile, spalte):
    button = tk.Button(fenster, text=str(zahl), height = 5, width = 10)
    button.grid(row=zeile, column=spalte)

for i in range(3):
    for j in range(3): 
        erstelle_button(haupt_fenster, i*3 + j + 1, i, j) 

haupt_fenster.mainloop()