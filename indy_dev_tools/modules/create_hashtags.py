from typing import List
from indy_dev_tools.models import IdtConfig
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.llm import prompt_json_response
from indy_dev_tools.modules.prompts import ULTIMATE_YT_CREATOR_INSTRUCTION

config: IdtConfig = load_config()

HASHTAGS_PROMPT = """{ULTIMATE_YT_CREATOR_INSTRUCTION}

You are an expert in social media marketing. Given a rough draft title and a list of SEO keywords, generate a list of relevant hashtags. The hashtags should be a comma-separated list and should be relevant to the content described by the title and keywords.

Rough draft title: {rough_draft_title}
SEO keywords: {seo_keywords}

Generate the hashtags:
"""

def create_hashtags(
    rough_draft_title: str,
    seo_keywords: str,
) -> List[str]:
    # Split the title and keywords into a list of words, remove duplicates, and format as hashtags
    prompt = HASHTAGS_PROMPT.format(
        ULTIMATE_YT_CREATOR_INSTRUCTION=ULTIMATE_YT_CREATOR_INSTRUCTION,
        rough_draft_title=rough_draft_title,
        seo_keywords=seo_keywords
    )

    response = prompt_json_response(
        prompt,
        openai_key=config.yt.openai_api_key,
        instructions="Generate a comma-separated list of hashtags."
    )

    # Assuming the response JSON structure contains a field 'hashtags' with the comma-separated list
    hashtags_list = response['hashtags'].split(',')
    hashtags = [hashtag.strip() for hashtag in hashtags_list if hashtag.strip()]

    # Write the hashtags to a file if a path is provided
    if config.yt.hashtags_file_path:
        with open(config.yt.hashtags_file_path, "w") as file:
            print(f"Writing hashtags to {config.yt.hashtags_file_path}")
            file.write("\n".join(hashtags))

    return hashtags
