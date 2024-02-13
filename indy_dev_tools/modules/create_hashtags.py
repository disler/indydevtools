from typing import List
from indy_dev_tools.models import IdtConfig
from indy_dev_tools.modules.idt_config import load_config

config: IdtConfig = load_config()

def create_hashtags(
    rough_draft_title: str,
    seo_keywords: str,
) -> List[str]:
    # Split the title and keywords into a list of words, remove duplicates, and format as hashtags
    combined_keywords = f"{rough_draft_title}, {seo_keywords}"
    keywords_list = [keyword.strip() for keyword in combined_keywords.split(',') if keyword.strip()]
    hashtags = [f"#{keyword.replace(' ', '')}" for keyword in keywords_list]

    # Write the hashtags to a file if a path is provided
    if config.yt.hashtags_file_path:
        with open(config.yt.hashtags_file_path, "w") as file:
            print(f"Writing hashtags to {config.yt.hashtags_file_path}")
            file.write("\n".join(hashtags))

    return hashtags
