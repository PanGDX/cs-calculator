from tkinter import *
from PIL import ImageTk
import os




class AppLatexConvert:
	'''Application to convert latex math-mode code to a .png file.

This python application will convert LaTeX (math-mode) code to a png image file.
It depends on the ImageTk package (not included in standard python distribution). Other python dependencies (os, Tkinter) are included in a standard python distribution, so the user need not worry about these.

The script takes input from the user via a text box. The input is already enclosed by math-mode tags, and includes {amsmath,amssymb,amsthm} in the preamble. To move to a new line, use '\\'.

The script will crop your text appropriately, but cannot handle more than 1 page. Its main limitation is the platform dependence: the 'latex' command (line 102) works in linux, but not windows. It also depends on the dvipng package (only available for linux) to convert the .dvi file to a .png file.
'''

	def __init__(self, parent:Tk, latex, dpiLess:int=500):  # parent instead of master
		if __name__ == "__main__":
			abspath = os.path.abspath(__file__)
			dname = os.path.dirname(abspath)
			os.chdir(dname)

		self.latex = latex
		self.dpiLess=dpiLess

		self.tPreamble=r'''\usepackage{amssymb,amsmath,amsthm}'''

		self.tex()


	def tex(self):

		code=str(self.latex)
		preamble=self.tPreamble

		# Prepare filename for .png output
		output_name='image'
		output_name=output_name.rstrip('png')
		output_name=output_name.rstrip('.')

		
		if os.path.exists('temp.tex')==True:
			os.remove('temp.tex')
		filename='temp'

		temp=open('%s.tex' %filename, 'w')
		temp.write(r'''\documentclass[12pt]{article}
\pagestyle{empty}
''')
		temp.write(preamble)
		temp.write(r'''
\begin{document}
$\displaystyle \\
''')
		temp.write(code)
		temp.write(r'''$
\end{document}''')
		temp.close()

		os.system('latex %s.tex' %filename)

		# Requires package dvipng: converts dvi to png.
		# -D 500 sets resolution to 500 dpi, 
		# -O -1in,-1in sets offset (cut margins),
		# -o %s.png is the output filename
		dpi=str(self.dpiLess)
		os.system('dvipng -D %s -o %s.png -O -1in,-1in %s.dvi' %(dpi,output_name,filename))
		os.remove('%s.tex' %filename) # clean-up
		os.remove('%s.aux' %filename)
		os.remove('%s.log' %filename)
		os.remove('%s.dvi' %filename)

		# Requires ImageTk package:
		ImageTk.PhotoImage(file=output_name+'.png')
	
		print("File saved as '%s.png' in current directory." %(output_name))



if __name__ == "__main__":
	root = Tk()
	app=AppLatexConvert(parent=root, latex=r"1234\newline 111")