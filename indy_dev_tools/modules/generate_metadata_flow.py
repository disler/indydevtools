from indy_dev_tools.models import IdtConfig, GenerateMetadataInput
from indy_dev_tools.modules import (
    create_thumbnail,
    create_title,
    create_transcription,
    create_description,
    resize_image,
)
from indy_dev_tools.modules.idt_config import load_config


def generate_metadata_flow(input_data: GenerateMetadataInput):
    config_file: IdtConfig = load_config()

    # Transcribe 120 seconds to create the script
    create_transcription.create_transcription(
        input_data.path_to_audio_or_video,
        duration_limit_in_seconds=120,
        create_json_file=True,
    )

    # Generate titles
    create_title.create_title(
        input_data.count,
        input_data.rough_draft_title,
        config_file.yt.script_file_path,
        seo_keywords=input_data.seo_keywords,
    )

    # Generate descriptions
    create_description.create_description(
        input_data.count,
        config_file.yt.script_file_path,
        seo_keywords=input_data.seo_keywords,
    )

    # Generate thumbnails
    create_thumbnail.create_thumbnail(input_data.count, input_data.thumbnail_prompt)

    # Assuming there's a function for resizing in create_thumbnails
    for i in range(input_data.count):
        resize_image.resize_image(config_file.yt.make_thumbnail_file_path(i, ext="png"))
