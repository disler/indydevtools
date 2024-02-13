from typing import List
from indy_dev_tools.models import IdtConfig
from indy_dev_tools.modules.idt_config import load_config

config: IdtConfig = load_config()

def create_hashtags(
    count: int,
    rough_draft_title: str,
    seo_keywords: str,
) -> List[str]:
    # Split the title and keywords into a list of words, remove duplicates, and format as hashtags
    words = set(rough_draft_title.split() + seo_keywords.split())
    hashtags = [f"#{word}" for word in words if word]

    # Write the hashtags to a file if a path is provided
    if config.yt.hashtags_file_path:
        with open(config.yt.hashtags_file_path, "w") as file:
            print(f"Writing hashtags to {config.yt.hashtags_file_path}")
            file.write("\n".join(hashtags))

    return hashtags
