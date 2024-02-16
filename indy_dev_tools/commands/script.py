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
        False,
        "--json",
        "-j",
        help="Create an additional JSON file of the transcript with segments and word timestamps.",
    ),
    duration_limit_in_seconds: str = typer.Option(
        120, "--seconds", "-s", help="The maximum seconds to process."
    ),
):
    create_transcription(
        file,
        duration_limit_in_seconds=duration_limit_in_seconds,
        create_json_file=create_json_file,
    )
