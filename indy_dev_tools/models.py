from typing import Optional
from pydantic import BaseModel
from typing import List


class IdtYoutube(BaseModel):
    openai_api_key: Optional[str]
    output_dir: Optional[str]
    config_file_path: Optional[str]


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
