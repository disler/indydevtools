import typer
from ..modules import idt_config
from ..models import IdtConfig

app = typer.Typer()


@app.command()
def edit():
    """
    Open the configuration file in your default editor.

    Input:
        - None
    Output:
        - The configuration file is opened in your default editor.
    """
    config: IdtConfig = idt_config.load_config()
    if config.yt and config.yt.config_file_path:
        config_file = config.yt.config_file_path
        typer.launch(config_file)


@app.command()
def view(only_print: bool = typer.Option(
    False,
    "--only-print",
    "-p",
    help="Only print the configuration file to the console, do not open in editor",
)
):
    """
    View the configuration file in the console.

    Input:
        - None
    Output:
        - The configuration file is printed to the console.
    """
    config: IdtConfig = idt_config.load_config()
    if not only_print and config.yt and config.yt.config_file_path:
        typer.launch(config.yt.config_file_path)
    else:
        typer.echo(config.model_dump_json(indent=2))
