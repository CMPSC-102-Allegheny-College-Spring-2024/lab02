"""Calculate the roots of a quadratic equation given values for a, b, and c."""

from rich.console import Console

import typer

from rootfinder import rootfind

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def main(
    a: float = typer.Option(1), b: float = typer.Option(2), c: float = typer.Option(2)
):
    """Calculate the roots of a quadratic equation using the quadratic formula."""
    # create a console for rich text output
    console = Console()
    # Display (by printing out) the debugging output for the program's command-line arguments
    # TODO: display three lines of output following the expected output
    # --> A label describing the output values
    # --> The value of a
    # --> The value of b
    # --> The value of c
    # --> You can display the "star" emoji by using :star:
    # TODO: call the function that performs the calculation of the roots for the quadratic equation
    # TODO: output the values from running the calculation of the quadratic
    # equation's roots with the calculate_quadratic_equation_roots function
    # TODO: display a blank line for separation from the first output segment
    # TODO: display three lines of output following the expected output
    # --> A label describing the output values
    # --> The value of x_one
    # --> The value of x_two
