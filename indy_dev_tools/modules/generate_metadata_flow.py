from indy_dev_tools.models import IdtConfig, GenerateMetadataInput
from indy_dev_tools.modules import (
    create_thumbnail_prompt,
    create_thumbnail,
    create_title,
    create_transcription,
    create_description,
    resize_image,
    create_formatted_references,
    create_hashtags,
    compose_description,
    compose_hashtags,
    compose_title,
    compose_thumbnail,
)
from indy_dev_tools.modules.idt_config import load_config


def generate_metadata_flow(input_data: GenerateMetadataInput):
    config_file: IdtConfig = load_config()

    # Transcribe 120 seconds to create the script
    if not input_data.skip_transcription:
        create_transcription.create_transcription(
            input_data.path_to_audio_or_video,
            duration_limit_in_seconds=input_data.transcription_length,
            create_json_file=True,
        )
    else:
        print("Skip Transcription Flag Present: Skipping transcription...")

    # Format references
    if input_data.references:
        create_formatted_references.create_formatted_references(
            input_data.references,
            input_data.rough_draft_title,
            input_data.seo_keywords,
        )
    else:
        print("No references provided.")

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

    # Generate Hashtags
    create_hashtags.create_hashtags(
        input_data.rough_draft_title, input_data.seo_keywords
    )

    # Generate thumbnail prompt
    create_thumbnail_prompt.create_thumbnail_prompt(
        input_data.count, input_data.rough_draft_title, input_data.seo_keywords
    )

    # Generate thumbnails - technically this is a create & compose step
    create_thumbnail.create_thumbnail_from_generated_prompt(input_data.count)

    # Assuming there's a function for resizing in create_thumbnails
    for i in range(input_data.count):
        resize_image.resize_image(config_file.yt.make_thumbnail_file_path(i, ext="png"))

    # Everything is generated - now handle selection and composing of final assets
    # Compose the final set of hashtags for use in metadata
    compose_hashtags.compose_hashtags()

    # Compose the final description incorporating all necessary elements
    compose_description.compose_description()

    # Compose the final titles based on generated data and input parameters
    compose_title.compose_titles()

    # Compose the final thumbnail from generated assets
    compose_thumbnail.compose_thumbnail()

    final_dir = config_file.yt.final_dir_path

    print(
        f"🎉 Youtube Metadata Generation Complete 🎉\n\n Open your {final_dir} to view your finalized metadata."
    )
