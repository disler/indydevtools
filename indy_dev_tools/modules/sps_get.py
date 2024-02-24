from indy_dev_tools.models import IdtSimplePromptSystem, IdtSimplePromptTemplate


def sps_get(sps_config: IdtSimplePromptSystem, alias: str) -> IdtSimplePromptTemplate:
    for template in sps_config.templates:
        if template.alias == alias:
            print(template.model_dump_json(indent=2))
            return template
    raise ValueError(f"No template found with alias '{alias}'.")
