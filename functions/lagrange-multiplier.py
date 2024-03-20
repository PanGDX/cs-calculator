import sympy as sp

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


if __name__ == '__main__':
    x, y = sp.symbols('x y')
    f = (x**(1/3))*(y**(2/3))
    g = 3*x+2*y-12
    vars = [x, y]

    solutions = solve_lagrange_multiplier(f, g, vars)
    print(solutions)