import typer
from indy_dev_tools.commands import thumbnails, titles, script, descriptions
from indy_dev_tools.models import IdtConfig
from indy_dev_tools.modules.idt_config import load_config

config_file: IdtConfig = load_config()

app = typer.Typer()
app.add_typer(
    thumbnails.app, name="thumb", help="Generate thumbnails for your content."
)
app.add_typer(titles.app, name="titles", help="Generate video titles.")
app.add_typer(script.app, name="script", help="Transcribe videos.")
app.add_typer(descriptions.app, name="desc", help="Generate video descriptions.")


@app.command()
def config():

    # dump config file
    print(config_file.model_dump_json(indent=2))


if __name__ == "__main__":
    app()
