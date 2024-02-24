import json
from indy_dev_tools.models import IdtSimplePromptSystem


def sps_list(sps_config: IdtSimplePromptSystem):
    templates_json = [template.dict() for template in sps_config.templates]
    print(json.dumps(templates_json, indent=2))
