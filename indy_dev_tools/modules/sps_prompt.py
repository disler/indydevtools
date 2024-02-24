from typing import Optional
import openai
from indy_dev_tools.models import IdtSimplePromptSystem, IdtSimplePromptTemplate
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.sps_get import get_prompt_template_by_alias
from indy_dev_tools.modules.llm import prompt as llm_prompt

def sps_prompt(alias: str, prompt: str, vars: Optional[str] = None, openai_key: str) -> str:
    config = load_config()
    if not config.sps:
        raise ValueError("Simple Prompt System configuration not found.")

    template = get_prompt_template_by_alias(config.sps, alias)
    template_content = template.prompt_template

    if vars:
        variables = dict(var.split('=') for var in vars.split(','))
        for key, value in variables.items():
            template_content = template_content.replace(f"{{{{ {key} }}}}", value)

    final_prompt = template_content.replace("{{prompt}}", prompt)
    # Call the llm.prompt() function and return its result
    return llm_prompt(
        prompt=final_prompt,
        openai_key=openai_key,
        model="text-davinci-003",  # Assuming the model to be used is text-davinci-003
        instructions="You are a helpful assistant."  # Assuming default instructions
    )
