import tkinter as tk
from tkinter import Frame, Button, BOTTOM
from latex2sympy2 import latex2sympy
import pyperclip
from functions.LagrangeMultiplier import LagrangeApp

class CalculatorApp(tk.Tk):
    def __init__(self, root):
        self.root = root
        self.items = [
            "Lagrange Multiplier", 
            "Partial Differentiation", 
            "Multi-variable integration", 
            "Chain Rule", 
            "curl", 
            "div", 
        ]
        self.create_main_interface()



    def create_main_interface(self):
        search_frame = Frame(self.root)
        search_frame.pack(pady = "5px")

        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self.update_list)

        search_message = tk.Label(search_frame, text="Search Here",font=("Helvetica 13"))
        search_message.pack(pady="5px")

        self.entry = tk.Entry(search_frame, textvariable=self.search_var, font=("Helvetica 13"), width = 30)
        self.entry.pack(pady = "10px")

        self.listbox = tk.Listbox(search_frame, font=("Helvetica 13"), height = 8, width = 40)
        self.listbox.pack()


        self.update_list()

        button_frame = Frame(self.root)
        button_frame.pack(side=BOTTOM, pady="10px", padx="10px")

        run_calculation_button = Button(button_frame, text="Select Operation", command=self.run_calculation, width=15, height=2, font=("Helvetica 13"))
        run_calculation_button.pack(pady="10px", padx="5px")



    def update_list(self, *args):
        search_term = self.search_var.get().lower()
        self.listbox.delete(0, tk.END)
        for item in self.items:
            if search_term in item.lower():
                self.listbox.insert(tk.END, item)


    def run_calculation(self):
        current_selection = self.listbox.curselection()

        if current_selection:
            match self.listbox.get(current_selection):
                case "Lagrange Multiplier":
                    sub_page = tk.Tk()
                    sub_page.geometry("700x500")
                    app = LagrangeApp(sub_page)

                case _:
                    print("None")

 
if __name__ == '__main__':
    root = tk.Tk()

    root.geometry("500x400")
    root.title("ULTIMATE CALCULATOR")

    app = CalculatorApp(root)
    root.mainloop()
