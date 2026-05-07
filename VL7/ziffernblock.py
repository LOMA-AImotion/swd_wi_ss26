import tkinter as tk
haupt_fenster = tk.Tk()
# erstelle Buttons von 1 bis 9 
# 1 2 3
# 4 5 6
# 7 8 9 

def erstelle_button(fenster, zahl, zeile, spalte):
    button = tk.Button(fenster, text=str(zahl), height = 5, width = 10)
    button.grid(row=zeile, column=spalte)

for i in range(9): 
    zeile = i // 3 # Ganzzahldivision
    spalte = i % 3 # Rest bei Div durch 3
    erstelle_button(haupt_fenster, i+1, zeile, spalte) 

haupt_fenster.mainloop()