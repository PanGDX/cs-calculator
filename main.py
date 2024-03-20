import tkinter as tk
from tkinter import Frame, Button, Entry, messagebox, TOP, LEFT, BOTTOM
from latex2sympy2 import latex2sympy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pyperclip

class CalculatorApp(tk.Tk):
    def __init__(self, root):
        self.root = root
        self.create_main_interface()

    def create_main_interface(self):
        self.create_matplotlib_interface()


        search_frame = Frame(self.root)
        search_frame.pack(pady = "10px")

        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self.update_list)

        self.entry = tk.Entry(search_frame, textvariable=self.search_var, font=("Helvetica 13"), width = 30)
        self.entry.pack(padx = "15px")

        self.listbox = tk.Listbox(search_frame, font=("Helvetica 13"), height = 8, width = 40)
        self.listbox.pack()

        self.items = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
        self.update_list()

        button_frame = Frame(self.root)
        button_frame.pack(side=BOTTOM, pady="10px", padx="10px")

        run_calculation_button = Button(button_frame, text="Run Calculation", command=self.run_calculation, width=15, height=2, font=("Helvetica 13"))
        run_calculation_button.pack(pady="10px", padx="5px")

        self.root.bind("<Control-c>", self.copy_latex)

    def update_list(self, *args):
        search_term = self.search_var.get().lower()
        self.listbox.delete(0, tk.END)
        for item in self.items:
            if search_term in item.lower():
                self.listbox.insert(tk.END, item)


    def create_matplotlib_interface(self):
        matplotlib.use('TkAgg')

        matplotlib_frame = Frame(self.root)
        matplotlib_frame.pack(side=tk.TOP, padx="5px", fill="both")

        self.latex_entry = Entry(matplotlib_frame, width=70, font=("Helvetica 13"))
        self.latex_entry.pack(side=tk.TOP, pady="30px", padx="150px", fill="x")

        fig = matplotlib.figure.Figure(figsize=(10, 3), dpi=100)
        self.wx = fig.add_subplot(111)
        self.latex_canvas = FigureCanvasTkAgg(fig, master=matplotlib_frame)
        self.latex_canvas.get_tk_widget().pack(side=TOP)
        self.latex_canvas._tkcanvas.pack(side=TOP)

        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)

        self.root.bind('<Return>', self.graph)

    def copy_latex(self, event):
        pyperclip.copy("YES")

    def run_calculation(self):
        # Implement calculation logic here
        pass

    def graph(self, event):
        tmptext = self.latex_entry.get()
        tmptext = "$" + tmptext + "$"
        self.wx.clear()
        try:
            self.wx.text(0.5, 0.5, tmptext, fontsize=13, ha='center', va='center')
            self.latex_canvas.draw()
        except ValueError as e:
            messagebox.showerror("Error", f"Error while parsing the mathematical expression {e}!\n Possibly incorrect Latex format!")

if __name__ == '__main__':
    root = tk.Tk()
    app_width = 1400
    app_height = 700
    root.title("ULTIMATE CALCULATOR")
    root.geometry(f"{app_width}x{app_height}")

    app = CalculatorApp(root)
    root.mainloop()