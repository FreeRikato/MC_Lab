import gradio as gr
import numpy as np
import matplotlib.pyplot as plt

def plot_lines(a1, b1, c1, a2, b2, c2):
    """
    Plots two lines given by the equations:
    a1*x + b1*y = c1 and a2*x + b2*y = c2
    """
    x = np.linspace(-10, 10, 400)
    plt.figure()

    if b1 != 0:
        y1 = (c1 - a1 * x) / b1
        plt.plot(x, y1, label=f'{a1}x + {b1}y = {c1}')
    if b2 != 0:
        y2 = (c2 - a2 * x) / b2
        plt.plot(x, y2, label=f'{a2}x + {b2}y = {c2}')

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()

    # Return the plot object for Gradio
    return plt.gcf()  # Use plt.gcf() to get the current figure

# Gradio interface setup using the correct component for inputs
with gr.Blocks() as demo:
    gr.Markdown("## Graphical Method in Linear Programming")
    gr.Markdown("Enter the coefficients for two linear equations in the form ax + by = c")

    with gr.Row():
        a1 = gr.Number(label="Coefficient a1", value=1)
        b1 = gr.Number(label="Coefficient b1", value=1)
        c1 = gr.Number(label="Constant c1", value=2)

    with gr.Row():    
        a2 = gr.Number(label="Coefficient a2", value=1)
        b2 = gr.Number(label="Coefficient b2", value=1)
        c2 = gr.Number(label="Constant c2", value=2)

    plot_button = gr.Button("Plot Lines")
    output_plot = gr.Plot()

    plot_button.click(plot_lines, inputs=[a1, b1, c1, a2, b2, c2], outputs=output_plot)

demo.launch()
