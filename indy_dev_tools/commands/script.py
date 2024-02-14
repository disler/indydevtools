import typer
import openai

from openai.types.images_response import ImagesResponse
import os
import requests
from indy_dev_tools.models import IdtConfig, Transcription
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.create_transcription import create_transcription

app = typer.Typer()
config: IdtConfig = load_config()


@app.command()
def transcribe(
    file: str = typer.Option(
        ..., "--file", "-f", help="The path to the video file to transcribe."
    ),
    create_json_file: bool = typer.Option(
        False, "--json", "-j", help="Create a JSON file with the transcript."
    ),
    duration_limit_in_sec: str = typer.Option(
        None, "--seconds", "-s", help="The maximum seconds to process."
    ),
):

    duration_limit = (
        int(duration_limit_in_sec) if duration_limit_in_sec is not None else None
    )
    Transcription = create_transcription(
        file,
        duration_limit_in_seconds=duration_limit,
        create_json_file=create_json_file,
    )
