import typer
from typing import Optional
from indy_dev_tools.modules.sps_get import sps_get
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.sps_list import sps_list
from indy_dev_tools.modules.sps_prompt import sps_prompt
from indy_dev_tools.models import IdtConfig, IdtSimplePromptSystem
from indy_dev_tools.modules.idt_config import load_config, view_config

app = typer.Typer()

config_file: IdtConfig = load_config()


@app.command(
    help="Dump the config file for the Simple Prompt System so you can view it, open it, and edit it to add your own prompt templates."
)
def config(
    only_print: bool = typer.Option(
        False,
        "--only-print",
        "-p",
        help="Only print the configuration file to the console, do not open in editor",
    )
):
    """
    Dump the config file for the Simple Prompt System so you can view it, open it, and edit it to add your own prompt templates.

    Inputs:
        -p: Only print the configuration file to the console, do not open in editor
    Outputs:
        - The config file in your default editor
    """
    view_config(only_print)


@app.command()
def prompt(
    alias: str = typer.Option(..., "-a", help="The alias for the prompt template"),
    prompt: str = typer.Option(..., "-p", help="The prompt to run"),
    vars: Optional[str] = typer.Option(
        None, "-v", help="Custom variables in key=value format separated by commas"
    ),
):
    """
    Run a prompt using your favorite template with custom variables.

    Inputs:
        -a: The alias for the prompt template
        -p: The prompt to run
        -v: Custom variables in key=value format separated by commas
    Outputs:
        - The result of the prompt printed to the console
    """
    try:
        result = sps_prompt(alias=alias, prompt=prompt, vars=vars)
        typer.echo(result)
    except ValueError as e:
        typer.echo(f"Error: {e}")


@app.command()
def list():
    """
    List all available prompt templates.

    Inputs:
        - None
    Outputs:
        - The list of all available prompt templates
    """
    if config_file.sps:
        sps_list(config_file.sps)
    else:
        typer.echo("No Simple Prompt System configuration found.")


@app.command()
def get(alias: str = typer.Option(..., "-a", help="The alias for the prompt template")):
    """
    Get the prompt template.

    Inputs:
        -a: The alias for the prompt template
    Outputs:
        - The prompt template
    """
    sps_get(config_file.sps, alias)


if __name__ == "__main__":
    app()
