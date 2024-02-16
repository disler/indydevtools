from typing import Dict
import openai
import sys

import requests
from openai.types.images_response import ImagesResponse


def make_cap_refs(prompt: str, refs: Dict[str, str]) -> str:
    """
    Attach capitalized references to the prompt.
    """

    for key, value in refs.items():
        prompt += f"\n\n{key.upper()}\n\n{value}"

    return prompt


def prompt_json_response(
    prompt: str,
    openai_key: str,
    model: str = "gpt-4-0125-preview",
    instructions: str = "You are a helpful assistant.",
) -> str:
    """
    Generate a response from a prompt using the OpenAI API.

    Example:
        res = llm.prompt_json_response(
            f"You're a data innovator. You analyze SQL databases table structure and generate 3 novel insights for your team to reflect on and query.
            Generate insights for this this prompt: {prompt}.
            Format your insights in JSON format. Respond in this json format [{{insight, sql, actionable_business_value}}, ...]",
        )
    """

    if not openai_key:
        sys.exit(
            """
ERORR: OpenAI API key not found. Please export your key to OPENAI_API_KEY
Example bash command:
    export OPENAI_API_KEY=<your openai apikey>
            """
        )

    openai.api_key = openai_key
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": instructions,  # Added instructions as a system message
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        response_format={"type": "json_object"},
    )
    return response.choices[0].message.content


def prompt_image(
    prompt: str,
    openai_key: str,
    file_path: str,
    model: str = "dall-e-3",
    size: str = "1792x1024",
    quality: str = "standard",
):
    """
    Generate an image from a prompt using the OpenAI API and save it to the specified file path.
    """
    openai.api_key = openai_key

    response: ImagesResponse = openai.images.generate(
        model=model,
        prompt=prompt,
        n=1,
        size=size,
        quality=quality,
    )

    image_data = response.data[0]
    image_url = image_data.url

    with requests.get(image_url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
