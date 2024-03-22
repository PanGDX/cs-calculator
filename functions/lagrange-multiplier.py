import sympy as sp
import tkinter as tk
from tkinter import Frame, Entry, TOP, messagebox
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from latex2sympy2 import latex2sympy, latex2latex


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

		tk.Label(input_frame, text="Function f (in LaTeX): ").pack(side=tk.LEFT)
		self.f_entry = Entry(input_frame, width=30)
		self.f_entry.pack(side=tk.LEFT)

		tk.Label(input_frame, text="Constraint g (in LaTeX): ").pack(side=tk.LEFT)
		self.g_entry = Entry(input_frame, width=30)
		self.g_entry.pack(side=tk.LEFT)

		tk.Label(input_frame, text="Variables (separated by space): ").pack(side=tk.LEFT)
		self.vars_entry = Entry(input_frame, width=20)
		self.vars_entry.pack(side=tk.LEFT)

		self.create_matplotlib_interface()

		self.root.bind('<Return>', self.solve_and_display)
	
	def create_matplotlib_interface(self):
		matplotlib.use('TkAgg')

		matplotlib_frame = Frame(self.root)
		matplotlib_frame.pack(side=tk.TOP, padx="5px", fill="both")

		fig = matplotlib.figure.Figure(figsize=(10, 3), dpi=100)
		self.wx = fig.add_subplot(111)
		self.latex_canvas = FigureCanvasTkAgg(fig, master=matplotlib_frame)
		self.latex_canvas.get_tk_widget().pack(side=TOP)
		self.latex_canvas._tkcanvas.pack(side=TOP)

		self.wx.get_xaxis().set_visible(False)
		self.wx.get_yaxis().set_visible(False)
		

	def solve_and_display(self, event):
		# Get user input
		f_latex = self.f_entry.get()
		g_latex = self.g_entry.get()
		variables = self.vars_entry.get()

		try:
			# Convert LaTeX to sympy expressions and split variables
			f_sympy = latex2sympy(f_latex)
			g_sympy = latex2sympy(g_latex)
			vars_sympy = list(sp.symbols(variables))

			print(f_sympy)
			print(g_sympy)
			print(vars_sympy)
			# Solve using the Lagrange multiplier method
			solutions = solve_lagrange_multiplier(f_sympy, g_sympy, vars_sympy)[0]

			# Display solutions on Matplotlib canvas
			print(solutions)
			print(type(solutions))
			for key in solutions:
				print(f"{key}, {type(key)}, {solutions[key]}, {type(solutions[key])}")


			self.display_solutions(solutions)
		except Exception as e:
			messagebox.showerror("Error", f"An error occurred: {e}")

	def display_solutions(self, solutions):
		self.wx.clear()

		latex_text = ""
		for sol in solutions:
			latex_text += fr"\\text{{{sp.latex(sol)}}} = {sp.latex(solutions[sol])}\\\\"

		print(latex_text)

		formatted_latex = r"$"+{latex_text}+r"$"

		self.wx.text(0.5, 0.5, formatted_latex, fontsize=12, ha='center', va='center')

		self.latex_canvas.draw()


if __name__ == "__main__":
	root = tk.Tk()
	app = LagrangeApp(root)
	root.mainloop()
