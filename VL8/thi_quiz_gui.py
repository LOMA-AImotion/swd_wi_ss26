import tkinter as tk

def get_main_window():
    main_window = tk.Tk()
    main_window.title("THI Quiz")
    main_window.geometry("800x600")
    canvas = tk.Canvas(main_window, width=800, height=600)
    canvas.grid(row=0, column=0, rowspan=4, columnspan=2)
    testfrage = "Wie heißt die Hauptstadt von Bayern?"
    label = tk.Label(main_window, text=testfrage, font=("Arial", 14))
    label.grid(row=1, column=0, columnspan=2)
    testantworten = ["München", "Nürnberg", "Augsburg", "Ingolstadt"]
    for i, antwort in enumerate(testantworten):
        button = tk.Button(main_window, text=antwort)
        button.grid(row=i // 2 + 2, column=i % 2)
    return main_window

if __name__ == "__main__":
    print("Starting the quiz gui test ...")
    main_window = get_main_window()
    main_window.mainloop()
