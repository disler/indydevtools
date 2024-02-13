from typing import List
from indy_dev_tools.models import IdtConfig
from indy_dev_tools.models import IdtConfig, HashTagItems
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.llm import prompt_json_response
from indy_dev_tools.modules.prompts import ULTIMATE_YT_CREATOR_INSTRUCTION

config: IdtConfig = load_config()

HASHTAGS_PROMPT = """{ULTIMATE_YT_CREATOR_INSTRUCTION}

You are an expert in social media marketing. Given a rough draft title and a list of 10 SEO keywords, generate a list of relevant hashtags. 
The hashtags should be a comma-separated list and should be relevant to the content described by the title and keywords.
Place the list in this simple two key value string json structure: { "hashtags": "hashtag1, hashtag2, hashtag3, ...", "top_three": "#hashtag1 #hashtag2 #hashtag3"}.
Place the list of 10 items in a raw string inside of "hashtags" comma separated. These items have NO hashtags in front of them: "hashtag1, hashtag2, hashtag3, ...".
Place the most important 3 hashtags for SEO in "top_three" in youtube hashtag format: #hashtag1 #hashtag2 #hashtag3.

Rough draft title: {rough_draft_title}
SEO keywords: {seo_keywords}

Generate the hashtags:
"""


def create_hashtags(
    rough_draft_title: str,
    seo_keywords: str,
) -> List[str]:
    # Split the title and keywords into a list of words, remove duplicates, and format as hashtags
    prompt = HASHTAGS_PROMPT.replace(
        "{ULTIMATE_YT_CREATOR_INSTRUCTION}", ULTIMATE_YT_CREATOR_INSTRUCTION
    )

    prompt = prompt.replace("{rough_draft_title}", rough_draft_title)
    prompt = prompt.replace("{seo_keywords}", seo_keywords)

    response = prompt_json_response(
        prompt,
        openai_key=config.yt.openai_api_key,
        instructions="You are an expert in social media marketing. Given a rough draft title and a list of SEO keywords, generate a list of relevant hashtags. The hashtags should be a comma-separated list and should be relevant to the content described by the title and keywords.",
    )

    # Assuming the response JSON structure contains a field 'hashtags' with the comma-separated list
    parsed_response = HashTagItems.model_validate_json(response)

    # Write the hashtags to a file if a path is provided
    if config.yt.hashtags_file_path:
        with open(config.yt.hashtags_file_path, "w") as file:
            print(f"Writing hashtags to {config.yt.hashtags_file_path}")
            file.write(parsed_response.model_dump_json(indent=2))
