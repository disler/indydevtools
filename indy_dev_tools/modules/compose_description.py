from indy_dev_tools.models import (
    HashTagItems,
    HighQualityDescriptions,
    IdtConfig,
    GenerateMetadataInput,
    ReferenceItems,
)
from indy_dev_tools.modules.idt_config import load_config
import inquirer


def compose_description():

    config_file: IdtConfig = load_config()

    with open(config_file.yt.description_file_path, "r") as file:
        descriptions = HighQualityDescriptions.model_validate(file.read())

    # hashtags
    with open(config_file.yt.hashtags_file_path, "r") as file:
        hashtags = HashTagItems.model_validate(file.read())

    # references
    with open(config_file.yt.formatted_references_file_path, "r") as file:
        references = ReferenceItems.model_validate(file.read())

    pass
