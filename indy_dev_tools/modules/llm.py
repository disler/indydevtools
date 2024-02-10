from typing import Dict
import openai
import sys


def make_cap_refs(prompt: str, refs: Dict[str, str]) -> str:
    """
    Loop through refs and attach them to the bottom of prompt after \n\n.
    Upper case the key and then \n\n and then the value.
    Do the same for each key value pair in refs.


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
