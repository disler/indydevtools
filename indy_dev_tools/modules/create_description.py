from typing import Optional, List
from indy_dev_tools.modules.llm import make_cap_refs, prompt_json_response
from indy_dev_tools.models import IdtConfig
from indy_dev_tools.modules.idt_config import load_config
import os
from indy_dev_tools.modules.prompts import ULTIMATE_YT_CREATOR_INSTRUCTION


config: IdtConfig = load_config()

CREATE_DESCRIPTION_PROMPT = """{ULTIMATE_YT_CREATOR_INSTRUCTION}

You follow these rules to a tee to deliver the best youtube video descriptions on the planet:

- You focus exclusively on creating the best possible description for your next video.
- Create {count} descriptions for your next video. 
- Respond strictly in this json format: {high_quality_descriptions: [{hook, first_paragraph, second_paragraph, explanation}, ...]}
- The hook, first_paragraph, second_paragraph, and explanation must all be strings.
- Start the first sentence off with a strong, eye catching hook to engage potential viewers.
- The first_paragraph and second_paragraph of reach set should be 3-5 sentences long.
- You create descriptions that focus on the viewer, giving them not only a taste but also sharing key insights the video will provide.
- The explanation is to explain to Mr. Beast the value of each description set and why it will help his video get more views.
- You use the script provided to create the best possible description for your next video.
- You use the information below to create the best possible description for your next video.

"""


def create_description(
    count: int,
    script_file_path: str,
    seo_keywords: Optional[str] = None,
    draft_title: Optional[str] = None,
):
    print(
        f"create_description(count={count}, script_file_path={script_file_path}, seo_keywords={seo_keywords}, draft_title={draft_title})"
    )

    with open(script_file_path, "r") as file:
        script_content = file.read()

    cap_refs = {"script": script_content}

    if seo_keywords:
        print(f"Using SEO keywords: {seo_keywords}")
        cap_refs["seo_keywords"] = seo_keywords

    if draft_title:
        print(f"Using draft title: {draft_title}")
        cap_refs["draft_title"] = draft_title

    prompt = CREATE_DESCRIPTION_PROMPT.replace("{count}", str(count))
    prompt = prompt.replace(
        "{ULTIMATE_YT_CREATOR_INSTRUCTION}", ULTIMATE_YT_CREATOR_INSTRUCTION
    )

    prompt = make_cap_refs(prompt, cap_refs)

    # print(f"Running prompt: {prompt}")

    response = prompt_json_response(
        prompt,
        openai_key=config.yt.openai_api_key,
        instructions="Create a compelling video description",
    )

    if config.yt.description_file_path:
        with open(config.yt.description_file_path, "w") as file:
            print(f"Writing response to {config.yt.description_file_path}")
            file.write(response)
