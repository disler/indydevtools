import typer
from indy_dev_tools.commands import thumbnails, titles, script, descriptions
from indy_dev_tools.models import IdtConfig
from indy_dev_tools.modules.file_util import get_path_to_files_with_sound
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

import typer

app = typer.Typer()

import inquirer


@app.command()
def input():
    # Raw string input using Typer
    questions = [
        inquirer.List(
            "size",
            message="What size do you need?",
            choices=[
                "Jumbo",
                "Large",
                "Standard",
                "Medium",
                "With our in-depth discussion and demonstration, you'll see firsthand how this tool not only simplifies the metadata generation process but also enhances your content's visibility and engagement by intelligently optimizing every aspect of your video's metadata. By automating these critical tasks, we provide you with more time to focus on what truly matters - creating amazing content.",
                "In the digital age, automation is not just a luxury; it's a necessity. Specifically, for YouTube creators, managing the SEO research, brainstorming titles, creating thumbnails, and iterating descriptions consumes a vast amount of time. That's where we step in. This video unveils the future of content creation - a multi-agent YouTube automation metadata generator that's about to change everything.",
            ],
        ),
        # inquirer.inquirer.inquirer.prompt(
        #     "what size do you need?",
        # ),
    ]

    answers = inquirer.prompt(questions)
    typer.echo(f"You selected: {answers}")


@app.command()
def config():
    print(config_file.model_dump_json(indent=2))


@app.command()
def gen_meta2():

    operating_dir = config_file.yt.output_dir

    # Generate the list of audio or video files
    path_to_movie_or_audio_files = get_path_to_files_with_sound(operating_dir)
    file_choices = [file for file in path_to_movie_or_audio_files]

    if not len(file_choices or []):
        print(f"No audio or video files found in: {operating_dir}")
        return

    questions = [
        inquirer.List(
            "file_path",
            message="Select the path to the audio or video file",
            choices=file_choices,
        ),
        inquirer.Text("rough_draft_title", message="Rough draft title"),
        inquirer.Text(
            "seo_keywords", message="SEO keywords comma separated", default=""
        ),
        inquirer.Text("count", message="Count", default="3"),
    ]

    get_references = True

    if get_references:
        questions.append(inquirer.Text("references", message="References", default=""))

    answers = inquirer.prompt(questions)

    if not answers:
        print("No input provided.")
        return

    print("answers", answers)

    path_to_audio_or_video = answers["file_path"]
    rough_draft_title = answers["rough_draft_title"]
    references = answers["references"]
    seo_keywords = answers["seo_keywords"]
    count = int(answers["count"])

    # required: path_to_audio_or_video, rough_draft_title, seo_keywords, count
    if not path_to_audio_or_video:
        print("Path to audio or video is required.")
        return

    if not rough_draft_title:
        print("Rough draft title is required.")
        return

    if not seo_keywords:
        print("SEO keywords are required.")
        return

    if not count:
        print("Count is required.")
        return

    # Print everything
    print(
        f"Path to audio or video: {path_to_audio_or_video}\n"
        f"Rough draft title: {rough_draft_title}\n"
        f"References: {references}\n"
        f"SEO keywords: {seo_keywords}\n"
        f"Count: {count}"
    )

    # gen_meta(
    #     path_to_audio_or_video=path_to_audio_or_video,
    #     rough_draft_title=rough_draft_title,
    #     thumbnail_prompt=thumbnail_prompt,
    #     seo_keywords=seo_keywords,
    #     count=count,
    # )


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
