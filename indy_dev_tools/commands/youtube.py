import typer
from indy_dev_tools.commands import thumbnails, titles, script

app = typer.Typer()
app.add_typer(
    thumbnails.app, name="thumb", help="Generate thumbnails for your content."
)
app.add_typer(titles.app, name="titles", help="Generate video titles.")
app.add_typer(script.app, name="script", help="Transcribe videos.")


@app.command()
def config():
    typer.echo("Configuring")


if __name__ == "__main__":
    app()
