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
def view(open_in_editor: bool = typer.Option(False, "--open-in-editor", "-o", help="Open the configuration file in the default editor")):
    """
    View the configuration file in the console.

    Input:
        - None
    Output:
        - The configuration file is printed to the console.
    """
    config: IdtConfig = idt_config.load_config()
    if open_in_editor and config.yt and config.yt.config_file_path:
        typer.launch(config.yt.config_file_path)
    else:
        typer.echo(config.model_dump_json(indent=2))


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context, open_in_editor: bool = typer.Option(False, "--open-in-editor", "-o", help="Open the configuration file in the default editor")):
    """
    Print the configuration file to the console.

    Input:
        - None
    Output:
        - The configuration file is printed to the console.
    """
    if ctx.invoked_subcommand is None:
        config: IdtConfig = idt_config.load_config()
        if open_in_editor and config.yt and config.yt.config_file_path:
            typer.launch(config.yt.config_file_path)
        else:
            typer.echo(config.model_dump_json(indent=2))
