from typing import Optional
from indy_dev_tools.modules.llm import make_cap_refs, prompt_json_response
from indy_dev_tools.models import IdtConfig
from indy_dev_tools.modules.idt_config import load_config
import os

from indy_dev_tools.modules.prompts import ULTIMATE_YT_CREATOR_INSTRUCTION

CREATE_TITLE_PROMPT = """{ULTIMATE_YT_CREATOR_INSTRUCTION}

You follow these rules to a tee to deliver the best youtube video titles on the planet:

- You focus exclusively on creating the best possible title for your next video.
- Create {count} titles for your next video. 
- Respond strictly in this json format: {high_quality_titles: [{title, explanation, score}, ...]}
- The title must be a string.
- The score must be a number between 0 and 10.
- The explanation must be a string explaining why the title is good.
- To fit in the youtube UI, all titles must be shorter than 90 characters.
- You always incorporate at least one of the VIDEO_ELEMENTS into your title from below.
- You use the information below to create the best possible title for your next video.

VIDEO_ELEMENTS:

- Refute an objective (disobey common knowledge)
- Epic or Extreme
- Beginner tips
- Emotional
- Time frames (1 app 30 days)
- Deep desire ‘how to change your life in 3 weeks’
- Authority (pull a celeb, brand, or government)
- Timeliness (news jacking or trend jacking)
- Lists (N best M to buy)
- Curiosity ‘why you shouldn’t do X’ ‘what N should you use to W’ ‘Every wonder how N does X’
- Branding 'name, brand, or company recognition'
- Value proposition 'I read twitters code so you dont have to' (functional value that clearly explains what the watcher will learn or gain from the video)
- Personal experience or storytelling
- Controversy or debate
- Clarity 'clearly convey the subject matter of the video, making it easy for viewers to understand what the content is about'

"""

config: IdtConfig = load_config()


def create_title(
    count: int,
    draft_title: str,
    path_to_script: Optional[str],
    seo_keywords: Optional[str] = None,
):
    """
    Create a titles for a youtube video given a draft title, script, and SEO keywords.
    """

    print(
        f"create_title(count={count}, draft_title={draft_title}, path_to_script={path_to_script}, seo_keywords={seo_keywords})"
    )

    cap_refs = {}

    print(f"Using draft title: {draft_title}")
    cap_refs["draft_title"] = draft_title

    if seo_keywords:
        print(f"Using SEO keywords: {seo_keywords}")
        cap_refs["seo_keywords"] = seo_keywords

    if path_to_script:
        print(f"Using script file: {path_to_script}")
        with open(path_to_script, "r") as file:
            script = file.read()
            cap_refs["script"] = script

    prompt = CREATE_TITLE_PROMPT.replace("{count}", str(count))
    prompt = prompt.replace(
        "{ULTIMATE_YT_CREATOR_INSTRUCTION}", ULTIMATE_YT_CREATOR_INSTRUCTION
    )

    prompt = make_cap_refs(prompt, cap_refs)

    # print(f"Running prompt: {prompt}")

    response = prompt_json_response(
        prompt,
        openai_key=config.yt.openai_api_key,
        instructions=ULTIMATE_YT_CREATOR_INSTRUCTION,
    )

    if config.yt.title_file_path:
        with open(config.yt.title_file_path, "w") as file:
            print(f"Writing response to {config.yt.title_file_path}")
            file.write(response)

    return response
