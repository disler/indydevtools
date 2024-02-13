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
        descriptions = HighQualityDescriptions.model_validate(file.read())

    # hashtags
    with open(config_file.yt.hashtags_file_path, "r") as file:
        hashtags = HashTagItems.model_validate(file.read())

    # references
    with open(config_file.yt.formatted_references_file_path, "r") as file:
        references = ReferenceItems.model_validate(file.read())

    # Prepare the options for the inquirer checkbox prompt
    hook_options = [
        f"hook: {desc.hook}" for desc in descriptions.high_quality_descriptions
    ]
    first_para_options = [
        f"first_para: {desc.first_paragraph}" for desc in descriptions.high_quality_descriptions
    ]
    second_para_options = [
        f"second_para: {desc.second_paragraph}" for desc in descriptions.high_quality_descriptions
    ]

    # Create inquirer checkbox prompts for each section of the description
    hook_question = [
        inquirer.Checkbox('hook', message="Select a hook", choices=hook_options),
    ]
    first_para_question = [
        inquirer.Checkbox('first_paragraph', message="Select the first paragraph", choices=first_para_options),
    ]
    second_para_question = [
        inquirer.Checkbox('second_paragraph', message="Select the second paragraph", choices=second_para_options),
    ]

    # Prompt the user to select one hook, one first paragraph, and one second paragraph
    selected_hook = inquirer.prompt(hook_question)
    selected_first_para = inquirer.prompt(first_para_question)
    selected_second_para = inquirer.prompt(second_para_question)

    # Extract the selected descriptions
    final_hook = selected_hook['hook'][0].split(": ", 1)[1] if selected_hook['hook'] else ""
    final_first_para = selected_first_para['first_paragraph'][0].split(": ", 1)[1] if selected_first_para['first_paragraph'] else ""
    final_second_para = selected_second_para['second_paragraph'][0].split(": ", 1)[1] if selected_second_para['second_paragraph'] else ""

    # TODO: Implement the logic to use the selected description parts
    # This could involve writing to a file, returning the values, or further processing

