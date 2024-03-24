import sympy as sp

def perform_partial_differentiation(expression, variable):
    """
    Performs partial differentiation of a given expression with respect to a specified variable.

    Args:
    expression (str): The expression to be differentiated, as a string.
    variable (str): The variable with respect to which the expression is to be differentiated.

    Returns:
    sympy expression: The result of the partial differentiation.
    """
    # Convert the string inputs to sympy expressions
    expr = sp.sympify(expression)
    var = sp.symbols(variable)

    # Perform partial differentiation
    partial_derivative = sp.diff(expr, var)

    return partial_derivative

if __name__ == '__main__':
    result = perform_partial_differentiation("x**2 + x*y**2 + z**2", "x")
    print(result)