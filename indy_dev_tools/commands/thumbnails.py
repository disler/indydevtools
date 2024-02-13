import typer
import openai

from openai.types.images_response import ImagesResponse
import os
import requests
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.resize_image import resize_image
from indy_dev_tools.modules.create_thumbnail import create_thumbnail
from indy_dev_tools.models import IdtConfig

app = typer.Typer()
config: IdtConfig = load_config()


@app.command()
def create_prompt():
    """
    Create a prompt for generating a thumbnail.
    """
    print("Creating a prompt for generating a thumbnail.")
    print("Prompt created.")


@app.command()
def create(
    prompt: str = typer.Option(
        ..., "--prompt", "-p", help="The prompt to create thumbnail with."
    ),
    count: int = typer.Option(
        1, "--count", "-c", help="The number of thumbnails to create."
    ),
):
    """
    Create an image with the specified prompt and download it.
    """
    print(f"Creating {count} image(s) with prompt: {prompt}")
    create_thumbnail(prompt, count)


@app.command()
def rescale(
    image_file_path: str = typer.Option(
        ..., "--image_file_path", "-f", help="The path to the input image file."
    ),
    width: int = typer.Option(
        1280, "--width", "-w", help="The width to rescale the image to."
    ),
    height: int = typer.Option(
        720, "--height", "-h", help="The height to rescale the image to."
    ),
    output_file: str = typer.Option(
        None, "--output", "-o", help="The path to the output image file."
    ),
):
    """
    Rescale an image to the specified width and height.
    """
    if not output_file:
        base, ext = os.path.splitext(image_file_path)
        output_file = f"{base}_resized{ext}"

    resize_image(image_file_path, width, height, output_file)

    print(f"Image rescaled to {width}x{height} and saved to {output_file}")


@app.command()
def iterate(item: str):
    print(f"Iterating on thumbnail... : {item}")


if __name__ == "__main__":
    app()
