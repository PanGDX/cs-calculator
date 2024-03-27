import sympy as sp
import tkinter as tk
from tkinter import Frame, Entry, TOP, messagebox
from latex2sympy2 import latex2sympy
from PIL import Image, ImageTk
import os
try:
	from SaveLatex import AppLatexConvert
except ImportError:
	print("Dependency Structure Error. Ignoring Import")




def perform_partial_differentiation(expression, variable):
	"""
	Performs partial differentiation of a given expression with respect to a specified variable.

	Args:
	expression in sympy string
	variable in list form


	Returns:
	sympy expression: The result of the partial differentiation.
	"""


	# Perform partial differentiation
	partial_derivative = sp.diff(expression, variable)

	return partial_derivative






class PartialDiffApp:
	def __init__(self, root):
		if __name__ == "__main__":
			abspath = os.path.abspath(__file__)
			dname = os.path.dirname(abspath)
			os.chdir(dname)

		self.root = root
		root.title("Partial Differential")
		self.create_interface()
	
	def create_interface(self):
		# Input fields
		input_frame = Frame(self.root)
		input_frame.pack(side=tk.TOP, padx="5px", pady="10px")

		tk.Label(input_frame, text="Function f (in LaTeX) ",font=("Helvetica 13")).pack(side=tk.TOP)
		self.f_entry = Entry(input_frame, width=30 ,font=("Helvetica 13"))
		self.f_entry.pack(side=tk.TOP)


		tk.Label(input_frame, text="Variables (separated by space): ",font=("Helvetica 13")).pack(side=tk.TOP)
		self.vars_entry = Entry(input_frame, width=20,font=("Helvetica 13"))
		self.vars_entry.pack(side=tk.TOP)

		answer_frame = Frame(self.root)
		answer_frame.pack(side=tk.BOTTOM, padx="5px", pady="10px")

		self.button = tk.Button(answer_frame, text = "Solve!", command = self.solve_and_display,font=("Helvetica 13"))
		self.answer_label = tk.Label(answer_frame)

	
		self.answer_label.pack(pady="10px")
		self.button.pack()

		self.root.bind('<Return>', self.solve_and_display)
		

	def solve_and_display(self, event=""):
		
		f_latex = self.f_entry.get()
		variables = self.vars_entry.get()

		try:
			f_sympy = latex2sympy(f_latex)
			try:
				vars_sympy = list(sp.symbols(variables))
			except:
				vars_sympy = sp.symbols(variables)

			print(f_sympy)
			print(vars_sympy)
			solution = perform_partial_differentiation(f_sympy, vars_sympy)
			print(solution)


		except Exception as e:
			messagebox.showerror("Error", f"An error occurred: {e}")
		
		self.on_latex(solution)

	def on_latex(self, solution:str):
		temp = tk.Tk()
		temp.title("IMAGE")
		temp.withdraw()
		AppLatexConvert(temp, latex = solution)
		

		print(os.getcwd())
		image = Image.open(f"{os.getcwd()}/image.png")
		photo = ImageTk.PhotoImage(image)
		self.answer_label.config(image=photo)
		self.answer_label.photo = photo
		print("Opened photo")



if __name__ == '__main__':
	root = tk.Tk()
	root.geometry("700x500")
	app = PartialDiffApp(root)
	
	root.mainloop()

