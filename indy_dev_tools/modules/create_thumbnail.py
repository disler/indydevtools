import typer
import openai

from openai.types.images_response import ImagesResponse
import os
import requests
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.resize_image import resize_image
from indy_dev_tools.models import IdtConfig

config: IdtConfig = load_config()


def create_thumbnail_from_generated_prompt(count: int):

    thumbnail_prompts = []

    config.yt.thumbnail_prompt_file_path


def create_thumbnail(count: int, prompt: str):

    print(f"create_thumbnail()")

    openai.api_key = config.yt.openai_api_key

    for i in range(count):
        response: ImagesResponse = openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1792x1024",
            quality="standard",  # or 'hd'
        )

        image_data = response.data[0]
        image_url = image_data.url

        image_path = config.yt.make_thumbnail_file_path(i)

        with requests.get(image_url, stream=True) as r:

            r.raise_for_status()

            with open(image_path, "wb") as f:

                for chunk in r.iter_content(chunk_size=8192):

                    f.write(chunk)

        print(f"Image downloaded to {image_path}")
