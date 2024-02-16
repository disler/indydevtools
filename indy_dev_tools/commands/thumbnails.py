import typer
import openai

from openai.types.images_response import ImagesResponse
import os
import requests
from indy_dev_tools.modules.compose_thumbnail import compose_thumbnail
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.resize_image import resize_image
from indy_dev_tools.modules.create_thumbnail import (
    create_thumbnail,
    create_thumbnail_from_generated_prompt,
)
from indy_dev_tools.models import IdtConfig
from indy_dev_tools.modules.create_thumbnail import create_thumbnail
from indy_dev_tools.modules.create_thumbnail_prompt import create_thumbnail_prompt

app = typer.Typer()
config: IdtConfig = load_config()


@app.command(help="Compose the final thumbnail for a video.")
def compose():
    compose_thumbnail()


@app.command(help="Create thumbnails from a generated prompt.")
def create_from_prompt(
    count: int = typer.Option(
        1,
        "--count",
        "-c",
        help="The number of thumbnails to create from a selected prompt.",
    ),
):
    create_thumbnail_from_generated_prompt(count)


@app.command(help="Create a prompt for generating a thumbnail.")
def create_prompt(
    rough_draft_title: str = typer.Option(None, "-r", "--rough-draft-title"),
    seo_keywords: str = typer.Option(
        None,
        "--seo-keywords",
        "-k",
        help="SEO keywords to be included in the thumbnail prompt.",
    ),
    count: int = typer.Option(
        1, "--count", "-c", help="The number of thumbnail prompts to create."
    ),
    art_style: str = typer.Option(
        None, "--art-style", "-a", help="The art style to be used in the thumbnail."
    ),
):
    create_thumbnail_prompt(count, rough_draft_title, seo_keywords, art_style)


@app.command(help="Create an image with the specified prompt and download it.")
def create(
    prompt: str = typer.Option(
        ..., "--prompt", "-p", help="The prompt to create thumbnail with."
    ),
    count: int = typer.Option(
        1, "--count", "-c", help="The number of thumbnails to create."
    ),
):
    print(f"Creating {count} image(s) with prompt: {prompt}")
    create_thumbnail(count, prompt)


@app.command(
    help="Rescale an image to the specified width and height. Defaults to youtube thumbnail size"
)
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
    if not output_file:
        base, ext = os.path.splitext(image_file_path)
        output_file = f"{base}_resized{ext}"

    resize_image(image_file_path, width, height, output_file)

    print(f"Image rescaled to {width}x{height} and saved to {output_file}")


@app.command(help="Iterate over user data (unimplemented).")
def iterate(prompt: str, thumbnail_file_path: str):
    raise NotImplementedError("This command is not yet implemented.")


if __name__ == "__main__":
    app()
