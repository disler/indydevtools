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
    text_only_file: bool = typer.Option(
        False, "--text-only", "-t", help="Only output the text of the transcript."
    ),
):

    transcript: Transcription = transcribe_file(file)

    output_dir = config.yt.output_dir
    file_base_name = os.path.splitext(os.path.basename(file))[0]
    output_json_file = os.path.join(output_dir, file_base_name + ".json")
    output_text_file = os.path.join(output_dir, file_base_name + "_script_only.txt")

    # write the transcript to a file
    with open(output_json_file, "w") as f:
        f.write(transcript.model_dump_json())
        print(f"Transcription json written to {output_json_file}")

    if text_only_file:
        with open(output_text_file, "w") as f:
            f.write(transcript.entire_script)
            print(f"Transcription text written to {output_text_file}")
