from indy_dev_tools.models import (
    HashTagItems,
    HighQualityTitles,
    IdtConfig,
)
from indy_dev_tools.modules.idt_config import load_config
import inquirer


def compose_titles():

    print(f"compose_titles()")

    config_file: IdtConfig = load_config()

    with open(config_file.yt.title_file_path, "r") as file:
        hashtags = HighQualityTitles.model_validate_json(file.read())

    final_titles = ""

    with open(config_file.yt.final_title_file_path, "r") as file:
        file.write(final_titles)
