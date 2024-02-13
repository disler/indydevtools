from indy_dev_tools.modules.llm import make_cap_refs, prompt_json_response
from indy_dev_tools.models import IdtConfig
from indy_dev_tools.modules.idt_config import load_config


config: IdtConfig = load_config()

FORMAT_REFERENCES_PROMPT = """You are an AI that formats references for YouTube video descriptions. Use the rough draft title and SEO keywords to format the references in a 'title\\nlink' format for each reference. Here are the references:

{references}

Rough draft title: {rough_draft_title}
SEO keywords: {seo_keywords}
"""


def create_formatted_references(
    references: str,
    rough_draft_title: str,
    seo_keywords: str,
):
    cap_refs = {
        "references": references,
        "rough_draft_title": rough_draft_title,
        "seo_keywords": seo_keywords,
    }

    prompt = make_cap_refs(FORMAT_REFERENCES_PROMPT, cap_refs)

    response = prompt_json_response(
        prompt,
        openai_key=config.yt.openai_api_key,
        instructions="Format the references in a title and link format."
    )

    # Write the formatted references to a file
    if config.yt.formatted_references_file_path:
        with open(config.yt.formatted_references_file_path, "w") as file:
            print(f"Writing formatted references to {config.yt.formatted_references_file_path}")
            file.write(response)
