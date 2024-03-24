from typing import Optional
from indy_dev_tools.models import IdtSimplePromptSystem, IdtSimplePromptTemplate
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.llm import prompt as llm_prompt, prompt_stream
import os


def _parse_prompt_template(template: IdtSimplePromptTemplate) -> str:
    template_content = ""

    # Check if the string is a path to a file that exists
    if os.path.isfile(template.prompt_template):
        try:
            with open(template.prompt_template, "r") as file:
                template_content = file.read()
        except (FileNotFoundError, OSError) as e:
            # Fallback to using the string directly if there's an error reading the file
            template_content = template.prompt_template
    else:
        # If the path does not point to a file, use the string as is
        template_content = template.prompt_template
    return template_content


def sps_prompt(
    alias: str, prompt: str, vars: Optional[str] = None, stream_response: bool = True
) -> str:
    config = load_config()
    if not config.sps:
        raise ValueError("Simple Prompt System configuration not found.")
    if not config.sps.openai_api_key:
        raise ValueError(
            "OpenAI API key not found in Simple Prompt System configuration."
        )

    template: Optional[IdtSimplePromptTemplate] = None
    for tmpl in config.sps.templates:
        if tmpl.alias == alias:
            template = tmpl
            break
    if template is None:
        raise ValueError(f"Template with alias '{alias}' not found.")

    # Attempt to read the prompt template from a file, if it exists
    template_content = _parse_prompt_template(template)

    if not template_content:
        raise ValueError("Prompt template is empty.")

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
    if stream_response:
        response_stream = prompt_stream(
            prompt=final_prompt, openai_key=config.sps.openai_api_key
        )
        for response_part in response_stream:
            if response_part.choices[0].delta.content is not None:
                print(response_part.choices[0].delta.content, end="", flush=True)
    else:
        result = llm_prompt(prompt=final_prompt, openai_key=config.sps.openai_api_key)
        print(result)
