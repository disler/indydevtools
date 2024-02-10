import typer

from .commands import youtube
from .modules import idt_config
from .models import IdtConfig

app = typer.Typer()
app.add_typer(youtube.app, name="yt")


def main():
    config: IdtConfig = idt_config.load_config()

    if config.yt.openai_api_key is None:
        typer.echo("No OpenAI API key configured.")
        typer.echo("Please run the following command to configure the API key:")
        typer.echo("indy_dev_tools yt config")
        raise typer.Exit(code=1)

    if config.yt.output_dir is None:
        typer.echo("No output directory configured.")
        typer.echo(
            "Please run the following command to configure the output directory:"
        )
        typer.echo("indy_dev_tools yt config")
        raise typer.Exit(code=1)

    print(f"Loaded config: {config.model_dump_json(indent=2)}")

    app()


if __name__ == "__main__":
    main()
