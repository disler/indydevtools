from indy_dev_tools.models import IdtSimplePromptSystem, IdtSimplePromptTemplate
import typer

def get_prompt_template_by_alias(sps_config: IdtSimplePromptSystem, alias: str) -> IdtSimplePromptTemplate:
    for template in sps_config.templates:
        if template.alias == alias:
            return template
    typer.echo(f"No template found with alias '{alias}'.")
    raise typer.Exit(code=1)
