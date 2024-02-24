from indy_dev_tools.models import IdtSimplePromptSystem
import typer

def sps_list(sps_config: IdtSimplePromptSystem):
    for template in sps_config.templates:
        typer.echo(f"Alias: {template.alias}")
        typer.echo(f"Name: {template.name}")
        typer.echo(f"Description: {template.description}")
        typer.echo(f"Template: {template.prompt_template}")
        typer.echo("Variables:")
        for variable in template.variables:
            typer.echo(f"  {variable.name} (default: {variable.default}) - {variable.description}")
        typer.echo("---")
from indy_dev_tools.models import IdtSimplePromptSystem
import typer

def sps_list(sps_config: IdtSimplePromptSystem):
    for template in sps_config.templates:
        typer.echo(f"Alias: {template.alias}")
        typer.echo(f"Name: {template.name}")
        typer.echo(f"Description: {template.description}")
        typer.echo(f"Template: {template.prompt_template}")
        typer.echo("Variables:")
        for variable in template.variables:
            typer.echo(f"  {variable.name} (default: {variable.default}) - {variable.description}")
        typer.echo("---")
