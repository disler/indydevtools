from indy_dev_tools.models import IdtSimplePromptSystem, IdtSimplePromptTemplate
import typer

def get_prompt_template_by_alias(sps_config: IdtSimplePromptSystem, alias: str) -> IdtSimplePromptTemplate:
    for template in sps_config.templates:
        if template.alias == alias:
            typer.echo(f"Alias: {template.alias}")
            typer.echo(f"Name: {template.name}")
            typer.echo(f"Description: {template.description}")
            typer.echo(f"Template: {template.prompt_template}")
            typer.echo("Variables:")
            for variable in template.variables:
                typer.echo(
                    f"  {variable.name} (default: {variable.default}) - {variable.description}"
                )
            typer.echo("---")
            return template
    raise ValueError(f"No template found with alias '{alias}'.")
