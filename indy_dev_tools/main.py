import typer

from .commands import youtube
from .commands import playground
from .commands import simple_prompt_system
from .modules import idt_config
from .models import IdtConfig

app = typer.Typer()
app.add_typer(youtube.app, name="yt")
app.add_typer(playground.app, name="pg")
app.add_typer(simple_prompt_system.app, name="sps")


def main():
    """
    Main entry point for the CLI.
    """
    config: IdtConfig = idt_config.load_config()

    if config.yt.openai_api_key is None:
        typer.echo("No OpenAI API key configured.")
        raise typer.Exit(code=1)

    if config.yt.operating_dir is None:
        typer.echo("No output directory configured.")
        raise typer.Exit(code=1)

    app()


if __name__ == "__main__":
    main()
