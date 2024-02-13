def generate_metadata_flow():
    # Transcribe 120 seconds to create the script
    create_transcription.create_transcription(
        path_to_audio_or_video, duration_limit_in_seconds=220, create_json_file=True
    )

    # Generate titles
    create_title.create_title(
        count, rough_draft_title, config_file.yt.script_file_path, seo_keywords
    )

    # Generate descriptions
    create_description.create_description(
        count, config_file.yt.script_file_path, seo_keywords
    )

    # Generate thumbnails
    create_thumbnail.create_thumbnail(count, thumbnail_prompt)

    # Assuming there's a function for resizing in create_thumbnails
    for i in range(count):
        resize_image.resize_image(config_file.yt.make_thumbnail_file_path(i))
