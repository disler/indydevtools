from indy_dev_tools.modules.llm import make_cap_refs, prompt_json_response
from indy_dev_tools.models import IdtConfig, ReferenceItems
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.prompts import ULTIMATE_YT_CREATOR_INSTRUCTION


config: IdtConfig = load_config()

FORMAT_REFERENCES_PROMPT = """{ULTIMATE_YT_CREATOR_INSTRUCTION}

You formats references for YouTube video descriptions. Respond in a '<emoji> <title>\\n<link>' format for each reference. Primarily rely on the reference link to determine what the emoji and title should be, but also use supporting material like the rough draft title and SEO keywords if available.

Respond in this json format: { "references": "<formatted references>" }

Here are the references:

{references}

Example:

🔗 AI Coding Assistant
https://aider.chat/

💻 Learn to code faster
https://www.codementor.io/

📚 Python Programming
https://www.python.org/
"""


def create_formatted_references(
    references: str,
    rough_draft_title: str,
    seo_keywords: str,
):
    cap_refs = {
        "rough_draft_title": rough_draft_title,
        "seo_keywords": seo_keywords,
    }

    prompt = FORMAT_REFERENCES_PROMPT.replace("{references}", references)
    prompt = prompt.replace(
        "{ULTIMATE_YT_CREATOR_INSTRUCTION}", ULTIMATE_YT_CREATOR_INSTRUCTION
    )

    prompt = make_cap_refs(prompt, cap_refs)

    response = prompt_json_response(
        prompt,
        openai_key=config.yt.openai_api_key,
        instructions="Format the references in a title and link format.",
    )

    parsed_response = ReferenceItems.model_validate_json(response)

    # Write the formatted references to a file
    if config.yt.formatted_references_file_path:
        with open(config.yt.formatted_references_file_path, "w") as file:
            print(
                f"Writing formatted references to {config.yt.formatted_references_file_path}"
            )
            file.write(parsed_response.references)
