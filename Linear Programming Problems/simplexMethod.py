import gradio as gr
# Assuming lippy is correctly installed and imported, if it exists.
import lippy as lp

def solve_simplex(c_vec, a_matrix, b_vec):
    """
    Solve a linear programming problem using the Simplex method from the lippy library.

    Parameters:
    c_vec : list - Coefficients for the objective function.
    a_matrix : list of lists - Coefficient matrix for constraints.
    b_vec : list - Right-hand side values of constraints.

    Returns:
    tuple - Solution vector and the value of the objective function.
    """
    # Convert strings input to proper lists using eval (considering safety and trust in user input)
    c_vec = eval(c_vec)
    a_matrix = eval(a_matrix)
    b_vec = eval(b_vec)

    simplex = lp.SimplexMethod(c_vec, a_matrix, b_vec)
    solution, func_value = simplex.solve()
    return f"Solution: {solution}, Function Value: {func_value}"

iface = gr.Interface(
    fn=solve_simplex,
    inputs=[
        gr.Textbox(label="Objective Function Coefficients (c_vec, e.g., [6, 6, 6])"),
        gr.Textbox(label="Constraint Coefficients Matrix (a_matrix, e.g., [[4, 1, 1], [1, 2, 0], [0, 0.5, 4]])"),
        gr.Textbox(label="Constraints Values (b_vec, e.g., [5, 3, 8])")
    ],
    outputs="text",
    title="Simplex Method Solver",
    description="Enter the coefficients for the objective function, constraints matrix, and constraints values."
)

iface.launch()
