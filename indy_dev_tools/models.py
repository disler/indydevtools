import os
from typing import Optional
from pydantic import BaseModel
from typing import List


class ReferenceItems(BaseModel):
    references: str


class HashTagItems(BaseModel):
    hashtags: str
    top_three: str


class ThumbnailPromptItem(BaseModel):
    thumbnail_prompt: str
    explanation: str


class HighQualityThumbnailPrompts(BaseModel):
    high_quality_thumbnail_prompts: List[ThumbnailPromptItem]


class DescriptionItems(BaseModel):
    hook: str
    first_paragraph: str
    second_paragraph: str
    explanation: str


class HighQualityDescriptions(BaseModel):
    high_quality_descriptions: List[DescriptionItems]


class TitleItems(BaseModel):
    title: str
    explanation: str
    score: float


class HighQualityTitles(BaseModel):
    high_quality_titles: List[TitleItems]


class IdtYoutube(BaseModel):
    openai_api_key: Optional[str]
    operating_dir: Optional[str]
    config_file_path: Optional[str]

    @property
    def draft_sub_dir(self) -> str:
        return "draft"

    @property
    def final_sub_dir(self) -> str:
        return "final"

    @property
    def draft_dir_path(self) -> str:
        return os.path.join(self.operating_dir, self.draft_sub_dir)

    @property
    def final_dir_path(self) -> str:
        return os.path.join(self.operating_dir, self.final_sub_dir)

    @property
    def thumbnail_prompt_file_path(self) -> str:
        return os.path.join(
            self.operating_dir, self.draft_sub_dir, "thumbnail_prompt.json"
        )

    @property
    def script_file_path(self) -> str:
        return os.path.join(self.operating_dir, self.draft_sub_dir, "script.txt")

    @property
    def script_json_file_path(self) -> str:
        return os.path.join(self.operating_dir, self.draft_sub_dir, "script.json")

    @property
    def title_file_path(self) -> str:
        return os.path.join(self.operating_dir, self.draft_sub_dir, "titles.json")

    @property
    def description_file_path(self) -> str:
        return os.path.join(self.operating_dir, self.draft_sub_dir, "descriptions.json")

    @property
    def hashtags_file_path(self) -> str:
        return os.path.join(self.operating_dir, self.draft_sub_dir, "hashtags.json")

    @property
    def formatted_references_file_path(self) -> str:
        return os.path.join(
            self.operating_dir, self.draft_sub_dir, "formatted_references.txt"
        )

    @property
    def final_description_file_path(self) -> str:
        return os.path.join(self.operating_dir, self.final_sub_dir, "description.txt")

    @property
    def final_title_file_path(self) -> str:
        return os.path.join(self.operating_dir, self.final_sub_dir, "title.txt")

    @property
    def final_hashtags_file_path(self) -> str:
        return os.path.join(self.operating_dir, self.final_sub_dir, "hashtags.txt")

    @property
    def final_thumbnail_file_path(self) -> str:
        return os.path.join(self.operating_dir, self.final_sub_dir, "thumbnail.png")

    def make_thumbnail_file_path(self, count: int, ext="png") -> str:
        return os.path.join(
            self.operating_dir, self.draft_sub_dir, f"thumbnail_{count}.{ext}"
        )


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


class GenerateMetadataInput(BaseModel):
    path_to_audio_or_video: str
    rough_draft_title: str
    references: str
    seo_keywords: str
    count: int
    skip_transcription: Optional[bool] = False
    transcription_length: Optional[int] = 120
