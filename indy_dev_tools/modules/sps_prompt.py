from typing import Optional
import openai
from indy_dev_tools.models import IdtSimplePromptSystem, IdtSimplePromptTemplate
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.sps_get import get_prompt_template_by_alias
from indy_dev_tools.modules.llm import prompt as llm_prompt


def sps_prompt(alias: str, prompt: str, vars: Optional[str] = None) -> str:
    config = load_config()
    if not config.sps:
        raise ValueError("Simple Prompt System configuration not found.")
    if not config.sps.openai_api_key:
        raise ValueError(
            "OpenAI API key not found in Simple Prompt System configuration."
        )

    template = get_prompt_template_by_alias(config.sps, alias)
    template_content = template.prompt_template

    # Set default values for variables
    variables = {var.name: var.default for var in template.variables}
    # Override defaults with provided values
    if vars:
        variables.update(dict(var.split("=") for var in vars.split(",")))
    for key, value in variables.items():
        if value is not None:
            template_content = template_content.replace(f"{{{{ {key} }}}}", value)

    final_prompt = template_content.replace("{{prompt}}", prompt)
    # Call the llm.prompt() function with the OpenAI key from the config and return its result
    return llm_prompt(prompt=final_prompt, openai_key=config.sps.openai_api_key)
