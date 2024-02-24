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
        custom_vars = dict(var.split("=") for var in vars.split(","))
        for key, value in custom_vars.items():
            if key in variables:
                variables[key] = value

    # Replace variables in the template content
    for variable_name, variable_value in variables.items():
        if variable_value is not None:
            placeholder = "{{" + variable_name + "}}"
            template_content = template_content.replace(placeholder, variable_value)

    if "{{prompt}}" in template_content:
        final_prompt = template_content.replace("{{prompt}}", prompt)
    else:
        final_prompt = template_content + " " + prompt

    # Call the llm.prompt() function with the OpenAI key from the config and return its result
    return llm_prompt(prompt=final_prompt, openai_key=config.sps.openai_api_key)
