from typing import Optional
from pydantic import BaseModel


class IdtYoutube(BaseModel):
    openai_api_key: Optional[str]
    output_dir: Optional[str]
    config_file_path: Optional[str]


class IdtConfig(BaseModel):
    yt: Optional[IdtYoutube]
