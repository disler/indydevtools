import typer
import openai

from openai.types.images_response import ImagesResponse
import os
import requests
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.resize_image import resize_image
from indy_dev_tools.models import IdtConfig, HighQualityThumbnailPrompts
import inquirer
from indy_dev_tools.modules.llm import prompt_image

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

    for i in range(count):
        image_path = config.yt.make_thumbnail_file_path(i)
        prompt_image(prompt, config.yt.openai_api_key, image_path)
        print(f"Image downloaded to {image_path}")
