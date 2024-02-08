import typer
import openai

from openai.types.images_response import ImagesResponse
import os
import requests
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.resize_image import rescale_image
from indy_dev_tools.models import IdtConfig

config: IdtConfig = load_config()


def create_image(prompt: str):
    openai.api_key = config.yt.openai_api_key

    response: ImagesResponse = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1792x1024",
        quality="standard",  # or 'hd'
    )

    image_url = response.data[0].url

    print(f"Image URL: {image_url}")

    # Download the image
    output_dir = config.yt.output_dir if config.yt and config.yt.output_dir else "."
    image_path = os.path.join(output_dir, f"{prompt.replace(' ', '_')}.png")
    with requests.get(image_url, stream=True) as r:
        r.raise_for_status()
        with open(image_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Image downloaded to {image_path}")
