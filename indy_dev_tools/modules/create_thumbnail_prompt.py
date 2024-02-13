from indy_dev_tools.models import IdtConfig
from indy_dev_tools.modules.idt_config import load_config

def create_thumbnail_prompt(draft_title: str, seo_keywords: str):
    config: IdtConfig = load_config()
    thumbnail_prompt = f"Create a compelling thumbnail for the video titled '{draft_title}' using the following SEO keywords: {seo_keywords}."

    # Write the thumbnail prompt to a file
    if config.yt.thumbnail_prompt_file_path:
        with open(config.yt.thumbnail_prompt_file_path, "w") as file:
            file.write(thumbnail_prompt)
            print(f"Thumbnail prompt written to {config.yt.thumbnail_prompt_file_path}")
