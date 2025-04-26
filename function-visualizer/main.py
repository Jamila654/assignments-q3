#type:ignore
import time
import numpy as np
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table
from math import sin


console = Console()

def basic_quadratic(x):
    """A basic quadratic function: y = x^2 + 2x + 1"""
    return x**2 + 2*x + 1

sine_lambda = lambda x: sin(x)
def apply_function(func, inputs):
    """Applies a function to a list of inputs and returns the results."""
    return [func(x) for x in inputs]

def factorial(n):
    """Calculates the factorial of a number."""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
def timing_decorator(func):
    """A decorator that measures the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        console.print(f"[cyan]{func.__name__} took {end_time - start_time:.4f} seconds[/cyan]")
        return result
    return wrapper

@timing_decorator
def visualize_functions():
    """Visualize different function outputs in terminal and plot"""
    x_values = np.linspace(-10, 10, 100)
    
    quadratic_outputs = apply_function(basic_quadratic, x_values)
    sine_outputs = apply_function(sine_lambda, x_values)
    
    table = Table(title="Function Outputs")
    table.add_column("X", style="magenta")
    table.add_column("Quadratic (x^2 + 2x + 1)", style="green")
    table.add_column("Sine (sin(x))", style="blue")
    
    for i in range(5):
        table.add_row(
        f"{x_values[i]:.2f}",
        f"{quadratic_outputs[i]:.2f}", 
        f"{sine_outputs[i]:.2f}"
        )
    console.print(table)
    
    console.print(f"[yellow]Factorial of 5: {factorial(5)}[/yellow]")
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, quadratic_outputs, label="Quadratic: x^2 + 2x + 1", color="green")
    plt.plot(x_values, sine_outputs, label="Sine: sin(x)", color="blue")
    plt.title("Function Visualizer")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.savefig("function_plot.png")
    console.print("[green]Plot saved as 'function_plot.png'[/green]")

def main():
    
    console.print("[bold red]Welcome to the Colorful Function Visualizer![/bold red]")
    console.print("This project demonstrates function concepts in Python.\n")
    
    console.print("[bold cyan]1. Basic Function[/bold cyan]: Quadratic function (x^2 + 2x + 1)")
    console.print("[bold cyan]2. Lambda Function[/bold cyan]: Anonymous sine function")
    console.print("[bold cyan]3. Higher-Order Function[/bold cyan]: Applies a function to inputs")
    console.print("[bold cyan]4. Recursive Function[/bold cyan]: Calculates factorial")
    console.print("[bold cyan]5. Decorator[/bold cyan]: Times function execution\n")
    
    
    visualize_functions()

if __name__ == "__main__":
    main()
