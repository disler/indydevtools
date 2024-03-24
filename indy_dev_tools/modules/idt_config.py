from typing import Dict
import typer
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
from indy_dev_tools.modules import dict_util

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
    existing_config_dict: Dict, default_config: IdtConfig
) -> IdtConfig:
    """Merges the existing configuration with the default configuration, adding any missing keys."""
    config_updated = False
    for key, value in default_config.model_dump().items():
        if key not in existing_config_dict:
            existing_config_dict[key] = value
            config_updated = True

    # if no openaikey is set, set it to the environment variable - this is not scalable - but it's a start
    if not dict_util.safe_get(existing_config_dict, "yt.openai_api_key"):
        existing_config_dict["yt"]["openai_api_key"] = openai_api_key
        config_updated = True
    if not dict_util.safe_get(existing_config_dict, "sps.openai_api_key"):
        existing_config_dict["sps"]["openai_api_key"] = openai_api_key
        config_updated = True

    merged_config = IdtConfig(**existing_config_dict)
    if config_updated:
        write_config(merged_config)
    return merged_config


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
                    existing_config_dict = config_data or {}

                    merge_model = merge_new_configs(
                        existing_config_dict, DEFAULT_CONFIGURATION
                    )
                    config_in_memory = IdtConfig.model_validate(merge_model)

                    if config_in_memory.yt.openai_api_key is None:
                        raise ValueError(
                            "OpenAI API key is not set. Export your OpenAI API key as OPENAI_API_KEY."
                        )

                    generate_directories(config_in_memory)

                    return config_in_memory
                else:

                    config_in_memory = DEFAULT_CONFIGURATION

                    generate_directories(config_in_memory)

                    write_config(config_in_memory)

                    return config_in_memory
        else:
            write_config(DEFAULT_CONFIGURATION)
            config_in_memory = DEFAULT_CONFIGURATION
            generate_directories(config_in_memory)
            return config_in_memory
    except Exception as e:
        raise e


def generate_directories(config: IdtConfig):
    """Generates the draft and final directories based on the configuration."""
    draft_dir = Path(config.yt.operating_dir) / config.yt.draft_sub_dir
    final_dir = Path(config.yt.operating_dir) / config.yt.final_sub_dir
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


def view_config(only_print: bool = False):
    """View the configuration file in the console."""
    config = load_config()
    if not only_print and config.yt and config.yt.config_file_path:
        typer.launch(config.yt.config_file_path)
    else:
        typer.echo(config.model_dump_json(indent=2))


def view_config_dir():
    """Open the directory where the configuration file is stored."""
    config = load_config()

    # get the dir
    dir = Path(config.yt.config_file_path).parent

    # open the dir
    typer.launch(str(dir))
