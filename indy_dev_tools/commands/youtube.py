import typer
from indy_dev_tools.commands import thumbnails, titles, script, descriptions
from indy_dev_tools.models import IdtConfig
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules import (
    create_thumbnail,
    create_title,
    create_transcription,
    create_description,
    resize_image,
)


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
    print(config_file.model_dump_json(indent=2))


@app.command()
def gen_with_user_input():
    typer.echo("Generating meta with user input")


@app.command()
def gen_meta(
    path_to_audio_or_video: str = typer.Option(
        ..., "--file", "-f", help="Path to the audio or video file."
    ),
    rough_draft_title: str = typer.Option(..., "-r", "--rough-draft-title"),
    thumbnail_prompt: str = typer.Option(
        ..., "--thumb-prompt", "-tp", help="Prompt for generating the thumbnail."
    ),
    seo_keywords: str = typer.Option(None, "-k", "--seo-keywords"),
    count: int = typer.Option(3, "-c", "--count"),
):
    typer.echo("Generating meta data")

    # Transcribe 120 seconds to create the script
    create_transcription.create_transcription(
        path_to_audio_or_video, duration_limit_in_seconds=220, create_json_file=True
    )

    # Generate titles
    create_title.create_title(
        count, rough_draft_title, config_file.yt.script_file_path, seo_keywords
    )

    # Generate descriptions
    create_description.create_description(
        count, config_file.yt.script_file_path, seo_keywords
    )

    # Generate thumbnails
    create_thumbnail.create_thumbnail(count, thumbnail_prompt)

    # Assuming there's a function for resizing in create_thumbnails
    for i in range(count):
        resize_image.resize_image(config_file.yt.make_thumbnail_file_path(i))


if __name__ == "__main__":
    app()
