import os
import fnmatch


def get_path_to_files_with_sound(dir):
    # Define a list of common audio and movie file extensions
    audio_movie_extensions = [
        "*.mp3",
        "*.wav",
        "*.m4a",
        "*.flac",
        "*.aac",
        "*.ogg",
        "*.wma",
        "*.mov",
        "*.mp4",
        "*.avi",
        "*.mkv",
        "*.wmv",
        "*.m4v",
        "*.mpg",
        "*.flv",
    ]

    # List to store paths of files with sound
    files_with_sound = []

    # Walk through the directory
    for root, dirs, files in os.walk(dir):
        for extension in audio_movie_extensions:
            for filename in fnmatch.filter(files, extension):
                # Append the file path to the list
                files_with_sound.append(os.path.join(root, filename))

    return files_with_sound
