import typer
from ..modules import idt_config

app = typer.Typer()


@app.command(
    help="View the configuration file in the console. Use the --only-print flag to only print the configuration file to the console, do not open in editor."
)
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


@app.command()
@app.command(
    help="Edit the configuration file in the default editor. (Same as view command)"
)
def edit(
    only_print: bool = typer.Option(
        False,
        "--only-print",
        "-p",
        help="Only print the configuration file to the console, do not open in editor",
    )
):
    """
    Edit the configuration file in the default editor.

    Output:
        - The configuration file is opened in the default editor.
    """
    idt_config.view_config(only_print)


@app.command()
def dir(
    help="Open the directory where the configuration file is stored in the default file manager.",
):
    """
    Open the directory where the configuration file is stored.

    Output:
        - The directory where the configuration file is stored is opened.
    """
    idt_config.view_config_dir()
