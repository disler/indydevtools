import os
import shutil
from indy_dev_tools.models import (
    HashTagItems,
    HighQualityTitles,
    IdtConfig,
)
from indy_dev_tools.modules.idt_config import load_config
import inquirer


def compose_thumbnail():

    print(f"compose_thumbnail()")

    config_file: IdtConfig = load_config()

    draft_dir = config_file.yt.draft_dir_path
    final_dir = config_file.yt.final_dir_path

    # get thumbnail*.png files
    thumbnail_files = [
        f
        for f in os.listdir(draft_dir)
        if f.startswith("thumbnail") and f.endswith(".png")
    ]

    # use inquirer to prompt user to select a thumbnail
    thumbnail_question = [
        inquirer.Checkbox(
            "thumbnail", message="Select a thumbnail", choices=thumbnail_files
        ),
    ]

    # Prompt the user to select a thumbnail
    selected_thumbnail = inquirer.prompt(thumbnail_question).get("thumbnail", [])

    # Copy these items into the final directory
    for thumbnail in selected_thumbnail:
        thumbnail_file_path = os.path.join(draft_dir, thumbnail)
        final_thumbnail_file_path = os.path.join(final_dir, thumbnail)
        shutil.copyfile(thumbnail_file_path, final_thumbnail_file_path)

    print(f"Thumbnails copied to /final directory.")

    pass
