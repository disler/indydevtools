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
    path_to_audio_or_video = typer.prompt("Path to the audio or video file")
    if not path_to_audio_or_video or len(path_to_audio_or_video) < 5:
        typer.echo("Invalid input for the file path.")
        raise typer.Abort()

    rough_draft_title = typer.prompt("Rough draft title")
    if not rough_draft_title or len(rough_draft_title) < 5:
        typer.echo("Invalid input for the rough draft title.")
        raise typer.Abort()

    thumbnail_prompt = typer.prompt("Prompt for generating the thumbnail")
    if not thumbnail_prompt or len(thumbnail_prompt) < 5:
        typer.echo("Invalid input for the thumbnail prompt.")
        raise typer.Abort()

    seo_keywords = typer.prompt("SEO keywords", default="")
    if seo_keywords and len(seo_keywords) < 5:
        typer.echo("Invalid input for SEO keywords.")
        raise typer.Abort()

    count = typer.prompt("Count", default="3", type=int)

    gen_meta(
        path_to_audio_or_video=path_to_audio_or_video,
        rough_draft_title=rough_draft_title,
        thumbnail_prompt=thumbnail_prompt,
        seo_keywords=seo_keywords,
        count=count,
    )


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
