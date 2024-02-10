import typer
import openai

from openai.types.images_response import ImagesResponse
import os
import requests
from indy_dev_tools.models import IdtConfig, Transcription
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.transcribe import transcribe_file

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
    transcript: Transcription = transcribe_file(
        file,
        duration_limit_in_seconds=duration_limit,
    )
    output_dir = config.yt.output_dir
    file_base_name = os.path.splitext(os.path.basename(file))[0]
    output_json_file = os.path.join(output_dir, file_base_name + ".json")
    output_text_file = os.path.join(output_dir, "script_" + file_base_name + ".txt")

    # Always write the transcript text to a file
    with open(output_text_file, "w") as f:
        f.write(transcript.entire_script)
        print(f"Transcription text written to {output_text_file}")

    # Only write the transcript to a JSON file if the flag is present
    if create_json_file:
        with open(output_json_file, "w") as f:
            f.write(transcript.model_dump_json())
            print(f"Transcription json written to {output_json_file}")
