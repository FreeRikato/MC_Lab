import gradio as gr
import numpy as np

# Assuming the circular import issue is fixed by renaming or refactoring the BigM module.
# from BigM import BigM
from BigM import BigM
from BigM import graph
from BigM import InputHandling

def solve_big_m(objective, constraints):
    """
    Process and solve linear programming using the BigM method.
    """
    lp = [objective] + constraints.split(',')
    formatted_input = np.array(InputHandling.formatUserInput(lp))
    results = BigM().runBigM(formatted_input)

    return str(results)

iface = gr.Interface(
    fn=solve_big_m,
    inputs=[
        gr.Textbox(label="Objective Function (e.g., 'Max Z = x + 5y')", placeholder="Max Z = x + 5y"),
        gr.Textbox(label="Constraints (separate by commas)", placeholder="6x+5y<=60, x+2y<=14, x<=9")
    ],
    outputs="text",
    title="BigM Method Solver",
    description="Enter the objective function and constraints."
)

iface.launch()