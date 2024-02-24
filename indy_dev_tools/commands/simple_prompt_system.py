import typer
from typing import Optional

app = typer.Typer()

@app.command()
def config():
    """
    Dump the config file for the Simple Prompt System so you can view it, open it, and edit it to add your own prompt templates.
    """
    # TODO: Implement the logic to dump the SPS config file
    raise NotImplementedError("The 'config' command is not yet implemented.")

@app.command()
def prompt(
    alias: str = typer.Option(..., "-a", help="The alias for the prompt template"),
    prompt: str = typer.Option(..., "-p", help="The prompt to run"),
    vars: Optional[str] = typer.Option(None, "-v", help="Custom variables in key=value format separated by commas")
):
    """
    Run a prompt using your favorite template with custom variables.
    """
    # TODO: Implement the logic to run a prompt using a template and custom variables
    raise NotImplementedError("The 'prompt' command is not yet implemented.")

@app.command()
def list():
    """
    List all available prompt templates.
    """
    # TODO: Implement the logic to list all prompt templates
    raise NotImplementedError("The 'list' command is not yet implemented.")

@app.command()
def view(
    alias: str = typer.Option(..., "-a", help="The alias for the prompt template")
):
    """
    View the prompt template.
    """
    # TODO: Implement the logic to view a specific prompt template
    raise NotImplementedError("The 'view' command is not yet implemented.")