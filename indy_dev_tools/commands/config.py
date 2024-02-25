import typer
from ..modules import idt_config
from ..models import IdtConfig

app = typer.Typer()

@app.command()
@app.command(name="")
def main():
    """
    Display the current configuration.
    """
    config: IdtConfig = idt_config.load_config()
    typer.echo(config.model_dump_json(indent=2))
