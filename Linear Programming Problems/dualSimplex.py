import gradio as gr
import lippy as lp

def solve_lp(c_vec, a_matrix, b_vec):
    c_vec = [float(i) for i in c_vec.split(',')]
    a_matrix = [[float(num) for num in row.split(',')] for row in a_matrix.split('\n')]
    b_vec = [float(i) for i in b_vec.split(',')]
    
    c_vec, a_matrix, b_vec = lp.primal_to_dual_lp(c_vec, a_matrix, b_vec)
    simplex = lp.SimplexMethod(c_vec, a_matrix, b_vec)
    solution, func_value = simplex.solve()
    return solution, func_value

iface = gr.Interface(
    fn=solve_lp,
    inputs=[
        gr.Textbox(label="Enter c vector (comma-separated)", value="6, 6, 6"),
        gr.Textbox(label="Enter A matrix (rows comma-separated, new line for new row)", value="4, 1, 1\n1, 2, 0\n0, 0.5, 4"),
        gr.Textbox(label="Enter b vector (comma-separated)", value="5, 3, 8")
    ],
    outputs=[
        gr.Textbox(label="Solution"),
        gr.Textbox(label="Objective Function Value")
    ],
    title="Linear Programming Solver"
)

iface.launch()
