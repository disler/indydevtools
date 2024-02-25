from typing import Dict
import yaml
from platformdirs import user_data_dir, user_desktop_dir
from pathlib import Path
from dotenv import load_dotenv
import os
from indy_dev_tools.models import (
    IdtConfig,
    IdtSimplePromptSystem,
    IdtSimplePromptTemplate,
    IdtSimplePromptVariable,
    IdtYoutube,
)

APP_NAME = "indy_dev_tools"
APP_AUTHOR = "indy_dev_dan"

# Load environment variables from a .env file
load_dotenv()

# Determine the user data directory using platformdirs
config_dir = Path(user_data_dir(APP_NAME, APP_AUTHOR))
operating_dir = Path(user_desktop_dir())
config_file_path = config_dir / "config.yml"

# Load the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

DEFAULT_CONFIGURATION = IdtConfig(
    yt=IdtYoutube(
        openai_api_key=openai_api_key,
        operating_dir=str(operating_dir),
        config_file_path=str(config_file_path),
    ),
    sps=IdtSimplePromptSystem(
        config_file_path=str(config_file_path),
        openai_api_key=openai_api_key,
        templates=[
            IdtSimplePromptTemplate(
                alias="bash",
                prompt_template="bash: how do I: ",
                description="Ask a question about bash",
                name="Bash Prompt",
            ),
            IdtSimplePromptTemplate(
                alias="pyq",
                prompt_template="How do I: {{prompt}} in python?",
                description="Ask a question about python",
                name="Python Question",
            ),
            IdtSimplePromptTemplate(
                alias="midj",
                prompt_template="""Create a prompt for text to imagine tool midjourney.
Take the prompt below and the ideas in them in a dense, verbose, vivid one paragraph describing an imagine that midjourney will create.
End the prompt with '--ar {{ratio}} --v {{version}}'. Prompt: {{prompt}}""",
                description="Create a prompt for text to imagine tool midjourney",
                name="Midjourney Prompt",
                variables=[
                    IdtSimplePromptVariable(
                        name="ratio",
                        description="The ratio of the image",
                        default="16:9",
                    ),
                    IdtSimplePromptVariable(
                        name="version",
                        description="The version of midjourney to use",
                        default="6",
                    ),
                ],
            ),
        ],
    ),
)

config_in_memory = None


def merge_new_configs(
    existing_config: IdtConfig, default_config: IdtConfig
) -> IdtConfig:
    """Merges the existing configuration with the default configuration, adding any missing keys."""
    for key, value in default_config.dict().items():
        if key not in existing_config:
            existing_config[key] = value
    return IdtConfig(**existing_config)


def load_config() -> IdtConfig:
    """Loads the YAML configuration file."""

    global config_in_memory

    if config_in_memory:
        return config_in_memory

    try:

def load_config() -> IdtConfig:
    """Loads the YAML configuration file."""
    global config_in_memory
    if config_in_memory:
        return config_in_memory
    try:
        config_file = Path(config_file_path)
        if config_file.exists():
            with open(config_file, "r") as file:
                config_data = yaml.safe_load(file)
                if config_data:
                    # when rolling out new config options, we need to merge the old and new and save the new
                    existing_config = config_data or {}
                    merge_model = merge_new_configs(existing_config, DEFAULT_CONFIGURATION)
                    config_in_memory = merge_model

                    config_in_memory = IdtConfig.model_validate(merge_model)
                    if config_in_memory.yt.openai_api_key is None:
                        raise ValueError("OpenAI API key is not set.")
                    generate_directories(config_in_memory.yt)
                    return config_in_memory
                else:
                    config_in_memory = DEFAULT_CONFIGURATION
                    generate_directories(config_in_memory.yt)
                    return config_in_memory
        else:
            write_config(DEFAULT_CONFIGURATION)
            config_in_memory = DEFAULT_CONFIGURATION
            generate_directories(config_in_memory.yt)
            return config_in_memory
    except Exception as e:
        print(f"Error loading configuration: {e}")
        raise e
        config_in_memory = DEFAULT_CONFIGURATION
        generate_directories(config_in_memory.yt)
        return config_in_memory


def generate_directories(yt_config: IdtYoutube):
    """Generates the draft and final directories based on the configuration."""
    draft_dir = Path(yt_config.operating_dir) / yt_config.draft_sub_dir
    final_dir = Path(yt_config.operating_dir) / yt_config.final_sub_dir
    draft_dir.mkdir(parents=True, exist_ok=True)
    final_dir.mkdir(parents=True, exist_ok=True)


def write_config(data: IdtConfig):
    """Writes (or updates) the YAML configuration file."""
    try:
        config_dir.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
        config_file = Path(config_file_path)
        with open(config_file, "w") as file:
            yaml.safe_dump(data.model_dump(), file)
    except Exception as e:
        print(f"Error writing configuration: {e}")
