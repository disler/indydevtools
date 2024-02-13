import os
from typing import Optional
from pydantic import BaseModel
from typing import List


class IdtYoutube(BaseModel):
    openai_api_key: Optional[str]
    output_dir: Optional[str]
    config_file_path: Optional[str]
    thumbnail_prompt_file_path: Optional[str] = None

    @property
    def script_file_path(self) -> str:
        return os.path.join(self.output_dir, "script.txt")

    @property
    def script_json_file_path(self) -> str:
        return os.path.join(self.output_dir, "script.json")

    @property
    def title_file_path(self) -> str:
        return os.path.join(self.output_dir, "titles.json")

    @property
    def description_file_path(self) -> str:
        return os.path.join(self.output_dir, "descriptions.json")

    def make_thumbnail_file_path(self, count: int, ext="png") -> str:
        return os.path.join(self.output_dir, f"thumbnail_{count}.{ext}")


class IdtConfig(BaseModel):
    yt: Optional[IdtYoutube]


class TranscriptWord(BaseModel):
    """Represents a word in the transcript."""

    start: float
    end: float
    word: str


class TranscriptSegment(BaseModel):
    """Represents a segment in the transcript."""

    start: float
    end: float
    text: str
    words: List[TranscriptWord]


class Transcription(BaseModel):
    """Represents the entire transcription output."""

    entire_script: str
    segments: List[TranscriptSegment]
    words: List[TranscriptWord]


class Research(BaseModel):
    seo_keyword: str
    highlights: List[str]
    @property
    def thumbnail_prompt_file_path(self) -> str:
        return os.path.join(self.output_dir, "thumbnail_prompt.txt")
