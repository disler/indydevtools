from indy_dev_tools.models import IdtSimplePromptSystem, IdtSimplePromptTemplate


def sps_get(sps_config: IdtSimplePromptSystem, alias: str) -> IdtSimplePromptTemplate:
    for template in sps_config.templates:
        if template.alias == alias:
            print(f"Alias: {template.alias}")
            print(f"Name: {template.name}")
            print(f"Description: {template.description}")
            print(f"Template: {template.prompt_template}")
            if template.variables:
                print("Variables:")
            for variable in template.variables:
                print(
                    f"  {variable.name} (default: {variable.default}) - {variable.description}"
                )
            print("---")
            return template
    raise ValueError(f"No template found with alias '{alias}'.")
