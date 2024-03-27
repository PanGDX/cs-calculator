import sympy as sp
import tkinter as tk
from tkinter import Frame, Entry, TOP, messagebox
from latex2sympy2 import latex2sympy

def solve_lagrange_multiplier(f, g, vars):
	"""
	Solves the Lagrange multiplier problem for a given function f with constraint g.

	Args:
	f (sympy expression): The function to be maximized or minimized.
	g (sympy expression): The constraint function.
	vars (list): List of sympy symbols in f and g.

	Returns:
	List: Solutions of the Lagrange multiplier problem.
	"""
	# Introduce the Lagrange multiplier
	lamda = sp.symbols('lamda')
	
	# Lagrange function L = f - λ*g
	L = f - lamda * g

	# Calculate the gradients
	grad_L = [sp.diff(L, var) for var in vars]
	grad_L.append(g)  # Adding the constraint equation

	solutions = sp.solve(grad_L, vars + [lamda], dict=True)

	solutions_fraction = [{var: sp.nsimplify(sol[var]) for var in sol} for sol in solutions]

	return solutions_fraction



class LagrangeApp:
	def __init__(self, root):
		self.root = root
		root.title("Lagrange Multiplier Solver")
		self.create_interface()
	
	def create_interface(self):
		# Input fields
		input_frame = Frame(self.root)
		input_frame.pack(side=tk.TOP, padx="5px", pady="10px")

		tk.Label(input_frame, text="Function f (in LaTeX): ",font=("Helvetica 13")).pack(side=tk.TOP)
		self.f_entry = Entry(input_frame, width=30 ,font=("Helvetica 13"))
		self.f_entry.pack(side=tk.TOP)

		tk.Label(input_frame, text="Constraint g (in LaTeX): ",font=("Helvetica 13")).pack(side=tk.TOP)
		self.g_entry = Entry(input_frame, width=30,font=("Helvetica 13"))
		self.g_entry.pack(side=tk.TOP)

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
		g_latex = self.g_entry.get()
		variables = self.vars_entry.get()

		try:
			f_sympy = latex2sympy(f_latex)
			g_sympy = latex2sympy(g_latex)
			vars_sympy = list(sp.symbols(variables))

			print(f_sympy)
			print(g_sympy)
			print(vars_sympy)
			solutions = solve_lagrange_multiplier(f_sympy, g_sympy, vars_sympy)[0]

			print(solutions)
			print(type(solutions))
			for key in solutions:
				print(f"{key}, {type(key)}, {solutions[key]}, {type(solutions[key])}")



		except Exception as e:
			messagebox.showerror("Error", f"An error occurred: {e}")
		
		self.on_latex(solutions)

	def on_latex(self, solutions):
		
		latex_text=""
		for sol in solutions:
			if "**" in str(solutions[sol]):
				calculated = solutions[sol].evalf()
				latex_text += f"{str(sol)} = {str(solutions[sol])} = {calculated}\n"
			else:
				latex_text += f"{str(sol)} = {str(solutions[sol])}\n"

		print(latex_text)
		self.answer_label.config(text = latex_text,font=("Helvetica 15"))



if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("700x500")
	app = LagrangeApp(root)
	
	root.mainloop()

"""
{x^{1/3}}{y^{2/3}}
3x+2y-12
x y
"""