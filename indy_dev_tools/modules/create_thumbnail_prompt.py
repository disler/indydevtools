import random
from typing import Optional
from indy_dev_tools.models import IdtConfig
from indy_dev_tools.modules.idt_config import load_config
from indy_dev_tools.modules.llm import make_cap_refs, prompt_json_response
from indy_dev_tools.modules.prompts import ULTIMATE_YT_CREATOR_INSTRUCTION

ART_STYLES = [
    "Steampunk",
    "Art Deco",
    "Abstract Expressionism",
    "Pointillism",
    "Cubism",
    "Gothic",
    "Pop art",
    "Psychedelic",
    "Impressionism",
    "Fauvism",
    "Glitch Art",
    "Trompe L’oeil",
    "Chiaroscuro",
    "Minimalist",
    "Flat Design",
    "Surface Detail",
    "Halftone",
    "Grid",
    "Guilloché Patterns",
    "Celtic Maze",
    "Glassmorphism",
    "Morphism",
    "Bauhaus",
    "Art Nouveau",
    "Baroque",
    "Postmodernism",
    "Industrial",
    "Mid-Century Modern",
    "Scandinavian",
    "Japanese",
    "Mediterranean",
    "Bohemian",
    "Cyberpunk",
    "Sci-fi",
    "Eclectic",
    "Transitional",
    "Urban",
    "Global",
    "Naturalistic",
    "Geometric",
    "Dada",
    "Dada midjourney style prompt",
    "Opulent",
    "Synthetism",
    "Tachisme",
    "Symbolism",
    "Neo-Expressionism",
    "Vaporware",
    "Vaporware Midjourney Style Prompt",
    "Papercut",
    "Papercut Midjourney Style Prompt",
    "Pixel Art",
    "Pixel art Midjourney Style Prompt",
    "Bokeh",
]

THUMBNAIL_PROMPT = """{ULTIMATE_YT_CREATOR_INSTRUCTION} Create a compelling prompt that will be used to generate a thumbnail. Follow the RULE_SET_FOR_SUCCESS below to create the best prompt that will be used to generate a youtube thumbnail.

RULE_SET_FOR_SUCCESS:
- You create a prompt that is 2-3 sentences long.
- Create {count} descriptions for your next video. 
- Respond strictly in this json format: {high_quality_thumbnail_prompts: [{thumbnail_prompt, explanation}, ...]}
- The thumbnail_prompt must have a unique take on the describe the draft title visually.
- The prompt you create will be used to generate a thumbnail using generative AI.
- Describe the thumbnail that best represents the draft title in a creative way.
- Always specify 1 primary color and 1 secondary color that will be used in the thumbnail that will create a compelling image.
- In addition to primary colors, define how colors are used: gradient, solid, flat, spiral, energetic, simple, minimal, etc.
- We need a concise 2-3 sentence long describe of a unique, creative, engaging visual representation of the draft title.
- With every thumbnail_prompt create a explanation, explaining the choices made in the thumbnail_prompt.
- Use the additional information below to craft the thumbnail_prompt.
- Be sure to use a {art_style} art style in the thumbnail_prompt.

EXAMPLE:
- draft_title: "Using AI Copilots to write code for me"
- thumbnail_prompt: "An engineer sits at a desk with a computer, while a robot sits next to him, typing on a keyboard. The human is relaxing, the robot is working. The primary color is blue, the secondary color is white. Colors are used in a minimalist style."
- explanation: "The human is relaxing while the robot is working, this is a unique take on the draft title. The primary color is blue, the secondary color is white. Colors are used in a minimalist style."
"""


def create_thumbnail_prompt(
    count: int,
    draft_title: str,
    seo_keywords: Optional[str] = None,
    art_style: Optional[str] = None,
):
    config: IdtConfig = load_config()

    cap_refs = {"draft_title": draft_title}

    if seo_keywords:
        print(f"Using SEO keywords: {seo_keywords}")
        cap_refs["seo_keywords"] = seo_keywords

    selected_art_style = art_style if art_style else random.choice(ART_STYLES)

    prompt = THUMBNAIL_PROMPT.replace("{count}", str(count))
    prompt = prompt.replace("{art_style}", selected_art_style)
    prompt = prompt.replace(
        "{ULTIMATE_YT_CREATOR_INSTRUCTION}", ULTIMATE_YT_CREATOR_INSTRUCTION
    )

    prompt = make_cap_refs(prompt, cap_refs)

    # print(f"Running prompt: {prompt}")

    response = prompt_json_response(
        prompt,
        openai_key=config.yt.openai_api_key,
        instructions="Create a compelling description of a thumbnail that will captive viewers.",
    )

    # Write the thumbnail prompt to a file
    if config.yt.thumbnail_prompt_file_path:
        with open(config.yt.thumbnail_prompt_file_path, "w") as file:
            file.write(response)
            print(f"Thumbnail prompt written to {config.yt.thumbnail_prompt_file_path}")
