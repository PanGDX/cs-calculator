import sympy as sp
import tkinter as tk
from tkinter import Frame, Entry, TOP, messagebox
from latex2sympy2 import latex2sympy, latex2latex
from PIL import Image, ImageTk
from io import BytesIO

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

		self.button = tk.Button(text = "LaTeX!", command = self.on_latex)
		self.image_label = tk.Label(self.root)

		self.root.bind('<Return>', self.solve_and_display)
		

	def solve_and_display(self, event):
		
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


			self.on_latex(solutions)
		except Exception as e:
			messagebox.showerror("Error", f"An error occurred: {e}")

	def on_latex(self, solutions):
		latex_text = r"$\displaystyle "
		for sol in solutions:
			latex_text += fr"{sp.latex(sol)} = {sp.latex(solutions[sol])},"
		latex_text += r" $"

		print(latex_text)

		f = BytesIO()
		the_color = "{" + self.root.cget('bg')[1:].upper()+"}"
		sp.preview(latex_text, euler = False, 
				   preamble = r"\documentclass{standalone}"
				   	r"\usepackage{pagecolor}"
				   	r"\definecolor{graybg}{HTML}" + the_color +
				   	r"\pagecolor{graybg}"
					r"\usepackage{amsmath}"
					r"\usepackage{amsfonts}"
					r"\usepackage{amssymb}"
				   	r"\begin{document}"
				   ,
				   viewer = "BytesIO", output = "ps", outputbuffer=f)
		f.seek(0)
		#Open the image as if it were a file. This works only for .ps!
		img = Image.open(f)
		#See note at the bottom
		img.load(scale = 10)
		img = img.resize((int(img.size[0]/2),int(img.size[1]/2)),Image.BILINEAR)
		photo = ImageTk.PhotoImage(img)
		self.image_label.config(image = photo)
		self.image_label.image = photo
		f.close()


if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("1500x700")
	app = LagrangeApp(root)
	
	root.mainloop()

"""
{x^{1/3}}{y^{2/3}}
3x+2y-12
x y
"""