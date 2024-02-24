import typer
from typing import Optional
from indy_dev_tools.modules.sps_get import sps_get
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.sps_list import list_prompt_templates
from indy_dev_tools.modules.sps_prompt import sps_prompt
from indy_dev_tools.models import IdtConfig, IdtSimplePromptSystem
from indy_dev_tools.modules.idt_config import load_config

app = typer.Typer()

config_file: IdtConfig = load_config()


@app.command()
def config():
    """
    Dump the config file for the Simple Prompt System so you can view it, open it, and edit it to add your own prompt templates.
    """
    print(config_file.json(indent=2))


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
    """
    if config_file.sps:
        list_prompt_templates(config_file.sps)
    else:
        typer.echo("No Simple Prompt System configuration found.")


@app.command()
def view(
    alias: str = typer.Option(..., "-a", help="The alias for the prompt template")
):
    """
    View the prompt template.
    """
    sps_get(config_file.sps, alias)


if __name__ == "__main__":
    app()
