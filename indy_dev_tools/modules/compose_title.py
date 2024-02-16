from indy_dev_tools.models import (
    HashTagItems,
    HighQualityTitles,
    IdtConfig,
)
from indy_dev_tools.modules.idt_config import load_config
import inquirer
import inquirer


def compose_titles():

    print(f"compose_titles()")

    config_file: IdtConfig = load_config()

    with open(config_file.yt.title_file_path, "r") as file:
        titles = HighQualityTitles.model_validate_json(file.read())

    title_options = [title.title for title in titles.high_quality_titles]
    title_question = [
        inquirer.Checkbox("title", message="Select a title", choices=title_options),
    ]

    # Prompt the user to select a title
    selected_titles = inquirer.prompt(title_question).get("title", [])

    final_titles = "\n".join(selected_titles)

    with open(config_file.yt.final_title_file_path, "w") as file:
        file.write(final_titles)

    print(f"Title copied to /final directory.")
