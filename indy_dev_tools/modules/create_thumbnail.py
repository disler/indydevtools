import typer
import openai

from openai.types.images_response import ImagesResponse
import os
import requests
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.resize_image import resize_image
from indy_dev_tools.models import IdtConfig, HighQualityThumbnailPrompts
import inquirer

config: IdtConfig = load_config()


def create_thumbnail_from_generated_prompt(count: int):

    print(f"create_thumbnail_from_generated_prompt(count={count})")

    with open(config.yt.thumbnail_prompt_file_path, "r") as file:
        thumbnail_prompts = HighQualityThumbnailPrompts.model_validate_json(file.read())

    prompt_choices = [
        prompt.thumbnail_prompt
        for prompt in thumbnail_prompts.high_quality_thumbnail_prompts
    ]
    questions = [
        inquirer.List(
            "selected_prompt",
            message="Select a thumbnail prompt",
            choices=prompt_choices,
        ),
    ]
    selected_prompt = inquirer.prompt(questions)["selected_prompt"]
    create_thumbnail(count, selected_prompt)


def create_thumbnail(count: int, prompt: str):

    print(f"create_thumbnail(count={count}, prompt={prompt})")

    openai.api_key = config.yt.openai_api_key

    for i in range(count):
        image_path = config.yt.make_thumbnail_file_path(i)

        response: ImagesResponse = openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1792x1024",
            quality="standard",  # or 'hd'
        )

        image_data = response.data[0]
        image_url = image_data.url

        with requests.get(image_url, stream=True) as r:

            r.raise_for_status()

            with open(image_path, "wb") as f:

                for chunk in r.iter_content(chunk_size=8192):

                    f.write(chunk)

        print(f"Image downloaded to {image_path}")
