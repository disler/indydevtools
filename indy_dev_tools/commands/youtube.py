import typer
from indy_dev_tools.commands import (
    thumbnails,
    titles,
    script,
    descriptions,
    references,
    hashtags,
)
from indy_dev_tools.models import IdtConfig, GenerateMetadataInput
from indy_dev_tools.modules.file_util import get_path_to_files_with_sound
from indy_dev_tools.modules.generate_metadata_flow import generate_metadata_flow
from indy_dev_tools.modules.idt_config import load_config
import inquirer


config_file: IdtConfig = load_config()

app = typer.Typer()
app.add_typer(
    thumbnails.app,
    name="thumb",
    help="Subcommands to generate thumbnails for your content.",
)
app.add_typer(titles.app, name="titles", help="Subcommands to generate video titles.")
app.add_typer(script.app, name="script", help="Subcommands to transcribe videos.")
app.add_typer(
    descriptions.app, name="desc", help="Subcommands to generate video descriptions."
)
app.add_typer(
    references.app, name="refs", help="Subcommands to format references for videos."
)
app.add_typer(
    hashtags.app, name="tags", help="Subcommands to generate tags for videos."
)


@app.command(help="Dump your config file to console.")
def config():
    print(config_file.model_dump_json(indent=2))


@app.command(help="Generate youtube metadata using a step by step interface")
def gen_meta_auto(
    get_references: bool = typer.Option(
        False,
        "-r",
        "--get-references",
        help="Collect references (links) for the video.",
    ),
):

    operating_dir = config_file.yt.operating_dir

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
        inquirer.Confirm(
            "skip_transcription", message="Skip transcription?", default=False
        ),
        inquirer.Text(
            "transcription_length",
            message="Transcription length (in seconds)",
            default="120",
        ),
    ]

    if get_references:
        questions.append(inquirer.Editor("references", message="References"))

    answers = inquirer.prompt(questions)

    if not answers:
        print("No input provided.")
        return

    path_to_audio_or_video = answers.get("file_path")
    rough_draft_title = answers.get("rough_draft_title")
    references = answers.get("references", "")
    seo_keywords = answers.get("seo_keywords")
    count = int(answers.get("count", 0) or 0)
    skip_transcription = answers.get("skip_transcription", False)
    transcription_length = int(answers.get("transcription_length", 120) or 120)

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

    generate_metadata_flow(
        GenerateMetadataInput(
            path_to_audio_or_video=path_to_audio_or_video,
            rough_draft_title=rough_draft_title,
            references=references,
            seo_keywords=seo_keywords,
            count=count,
            skip_transcription=skip_transcription,
            transcription_length=transcription_length,
        )
    )


@app.command(help="Generate youtube metadata using cli flags")
def gen_meta(
    path_to_audio_or_video: str = typer.Option(
        ..., "--file", "-f", help="Path to the audio or video file."
    ),
    rough_draft_title: str = typer.Option(..., "-r", "--rough-draft-title"),
    references: str = typer.Option(
        None, "--references", "-rf", help="Links for watchers to reference."
    ),
    seo_keywords: str = typer.Option(None, "-k", "--seo-keywords"),
    count: int = typer.Option(3, "-c", "--count"),
    skip_transcription: bool = typer.Option(False, "-st", "--skip-transcription"),
    transcription_length: int = typer.Option(120, "-tl", "--transcription-length"),
):
    typer.echo("Generating meta data")

    generate_metadata_flow(
        GenerateMetadataInput(
            path_to_audio_or_video=path_to_audio_or_video,
            rough_draft_title=rough_draft_title,
            references=references,
            seo_keywords=seo_keywords,
            count=count,
            skip_transcription=skip_transcription,
            transcription_length=transcription_length,
        )
    )


if __name__ == "__main__":
    app()
