from indy_dev_tools.models import (
    HashTagItems,
    IdtConfig,
)
from indy_dev_tools.modules.idt_config import load_config
import inquirer


def compose_hashtags():

    print(f"compose_hashtags()")

    config_file: IdtConfig = load_config()

    with open(config_file.yt.hashtags_file_path, "r") as file:
        hashtags = HashTagItems.model_validate_json(file.read())

    with open(config_file.yt.final_hashtags_file_path, "w") as file:
        file.write(hashtags.hashtags)

    print(f"Hashtags copied to /final directory.")
