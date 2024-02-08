from PIL import Image


def rescale_image(image_path: str, output_path: str, width: int, height: int):
    """
    Rescales an image from one ratio to another (1792x1024 to 1280x720) and saves it.

    Args:
      image_path: Path to the input image.
      output_path: Path to save the rescaled image.
    """
    with Image.open(image_path) as img:

        # Rescale using bicubic interpolation for better quality
        resized_img = img.resize((width, height), Image.BICUBIC)
        resized_img.save(output_path)

        print(f"Rescaled image saved to {output_path}")
