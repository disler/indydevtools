import yaml
from platformdirs import user_data_dir, user_desktop_dir
from pathlib import Path
from dotenv import load_dotenv
import os
from indy_dev_tools.models import IdtConfig, IdtYoutube

APP_NAME = "indy_dev_tools"
APP_AUTHOR = "indy_dev_dan"

# Load environment variables from a .env file
load_dotenv()

# Determine the user data directory using platformdirs
config_dir = Path(user_data_dir(APP_NAME, APP_AUTHOR))
output_dir = Path(user_desktop_dir())
config_file_path = config_dir / "config.yml"

# Load the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

DEFAULT_CONFIGURATION = IdtConfig(
    yt=IdtYoutube(
        openai_api_key=openai_api_key,
        output_dir=str(output_dir),
        config_file_path=str(config_file_path),
    )
)

config_in_memory = None


def load_config() -> IdtConfig:
    """Loads the YAML configuration file."""

    global config_in_memory

    if config_in_memory:
        return config_in_memory

    print(f"Loading configuration file")
    # print(f"Loading configuration from {config_file_path}...")

    try:

        config_file = Path(config_file_path)
        if config_file.exists():
            with open(config_file, "r") as file:
                config_data = yaml.safe_load(file)
                if config_data:
                    config_in_memory = IdtConfig.model_validate(config_data)
                    return config_in_memory
                else:
                    config_in_memory = DEFAULT_CONFIGURATION
                    return config_in_memory
        else:
            write_config(DEFAULT_CONFIGURATION)
            config_in_memory = DEFAULT_CONFIGURATION
            return config_in_memory
    except Exception as e:
        print(f"Error loading configuration: {e}")
        config_in_memory = DEFAULT_CONFIGURATION
        return config_in_memory


def write_config(data: IdtConfig):
    """Writes (or updates) the YAML configuration file."""
    try:
        config_dir.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
        config_file = Path(config_file_path)
        with open(config_file, "w") as file:
            yaml.safe_dump(data.model_dump(), file)
    except Exception as e:
        print(f"Error writing configuration: {e}")
