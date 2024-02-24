from indy_dev_tools.models import IdtSimplePromptSystem
import typer


def sps_list(sps_config: IdtSimplePromptSystem):
    print(sps_config.model_dump_json(indent=2))
