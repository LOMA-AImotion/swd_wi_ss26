"""

Implements a small GUI in tkinter that fills a dictionary.
"""

import tkinter
from tkinter import messagebox


def add_entry():
    key = entry_key.get()
    value = entry_value.get()
    dictionary[key] = value

    # Delete text from position 0 until end 
    entry_key.delete(0, 'end')
    entry_value.delete(0, 'end')

def show_content():
    messagebox.showinfo("Result", str(dictionary))
    main_win.destroy()

dictionary = {}

main_win = tkinter.Tk()
main_win.title("SWD Assignment 07")

label_enter_key = tkinter.Label(main_win, text="Enter key")
label_enter_key.pack()

entry_key = tkinter.Entry(main_win)
entry_key.pack()

label_enter_value = tkinter.Label(main_win, text="Enter value")
label_enter_value.pack()

entry_value = tkinter.Entry(main_win)
entry_value.pack()

# Frame is used to keep both buttons together in one line 
button_frame = tkinter.Frame(main_win)
button_frame.pack()

stop_button = tkinter.Button(button_frame, text='Stop entering', command=show_content)
stop_button.pack(side='left')

add_button = tkinter.Button(button_frame, text='Add', command=add_entry)
add_button.pack(side='left')

print("before main")
main_win.mainloop()
print("after main")
