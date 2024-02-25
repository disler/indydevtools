import typer
from ..modules import idt_config

app = typer.Typer()


@app.command()
def view(
    only_print: bool = typer.Option(
        False,
        "--only-print",
        "-p",
        help="Only print the configuration file to the console, do not open in editor",
    )
):
    """
    View the configuration file in the console.

    Input:
        -p: Only print the configuration file to the console, do not open in editor
    Output:
        - The configuration file is printed to the console.
    """
    idt_config.view_config(only_print)
