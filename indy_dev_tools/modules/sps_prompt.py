from typing import Optional
from indy_dev_tools.models import IdtSimplePromptSystem, IdtSimplePromptTemplate
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.sps_get import get_prompt_template_by_alias

def sps_prompt(alias: str, prompt: str, vars: Optional[str] = None) -> str:
    config = load_config()
    if not config.sps:
        raise ValueError("Simple Prompt System configuration not found.")

    template = get_prompt_template_by_alias(config.sps, alias)
    template_content = template.prompt_template

    if vars:
        variables = dict(var.split('=') for var in vars.split(','))
        for key, value in variables.items():
            template_content = template_content.replace(f"{{{{ {key} }}}}", value)

    return template_content.replace("{{prompt}}", prompt)
