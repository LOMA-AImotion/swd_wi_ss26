from tkinter import messagebox
class Feedbacker:

    def positive(self):
        pass 

    def negative(self):
        pass


class PrintFeedbacker(Feedbacker):

    def positive(self):
        print("Positive feedback")

    def negative(self):
        print("Negative feedback")


class TkinterFeedbacker(Feedbacker):
    def positive(self):
        messagebox.showinfo("THI", "Richtig beantwortet")
    
    def negative(self):
        messagebox.showerror("THI", "Falsch beantwortet")

def create_feedbacker() -> Feedbacker:
    if input("Verwende Tkinter (j|n)") == "j":
        return TkinterFeedbacker()  
    else:        
        return PrintFeedbacker()

if __name__ == "__main__":
    feedbacker: Feedbacker = None

    feedbacker:Feedbacker = create_feedbacker()
    feedbacker.positive()
    feedbacker.negative()