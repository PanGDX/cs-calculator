from latex2sympy2 import latex2sympy, latex2latex

tex = r"\frac{d}{dx}(x^{2}+x)"
# Or you can use '\mathrm{d}' to replace 'd'
print(latex2sympy(tex))
# => "Derivative(x**2 + x, x)"
print(latex2latex(tex))
# => "2 x + 1"