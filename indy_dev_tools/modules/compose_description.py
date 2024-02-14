from indy_dev_tools.models import (
    HashTagItems,
    HighQualityDescriptions,
    IdtConfig,
    GenerateMetadataInput,
    ReferenceItems,
)
from indy_dev_tools.modules.idt_config import load_config
import inquirer
import inquirer


def compose_description():

    config_file: IdtConfig = load_config()

    with open(config_file.yt.description_file_path, "r") as file:
        descriptions = HighQualityDescriptions.model_validate_json(file.read())

    # hashtags
    with open(config_file.yt.hashtags_file_path, "r") as file:
        hashtags = HashTagItems.model_validate_json(file.read())

    # references
    with open(config_file.yt.formatted_references_file_path, "r") as file:
        references = file.read()

    hook_options = [desc.hook for desc in descriptions.high_quality_descriptions]
    first_para_options = [
        desc.first_paragraph for desc in descriptions.high_quality_descriptions
    ]
    second_para_options = [
        desc.second_paragraph for desc in descriptions.high_quality_descriptions
    ]

    # Create inquirer checkbox prompts for each section of the description
    hook_question = [
        inquirer.Checkbox("hook", message="Select a hook", choices=hook_options),
    ]
    first_para_question = [
        inquirer.Checkbox(
            "first_paragraph",
            message="Select the first paragraph",
            choices=first_para_options,
        ),
    ]
    second_para_question = [
        inquirer.Checkbox(
            "second_paragraph",
            message="Select the second paragraph",
            choices=second_para_options,
        ),
    ]

    # Prompt the user to select one hook, one first paragraph, and one second paragraph
    selected_hook = inquirer.prompt(hook_question).get("hook", "")
    selected_first_para = inquirer.prompt(first_para_question).get(
        "first_paragraph", ""
    )
    selected_second_para = inquirer.prompt(second_para_question).get(
        "second_paragraph", ""
    )

    print("selected_hook", selected_hook)
    print("selected_first_para", selected_first_para)
    print("selected_second_para", selected_second_para)
