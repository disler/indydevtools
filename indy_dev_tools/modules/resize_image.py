from PIL import Image


def resize_image(
    image_path: str, width: int = 1280, height: int = 720, output_path: str = ""
):
    """
    Rescales an image from one ratio to another (1792x1024 to 1280x720) and saves it.

    Args:
      image_path: Path to the input image.
      output_path: Path to save the rescaled image.
    """

    if output_path == "":
        output_path = image_path

    with Image.open(image_path) as img:

        # Rescale using bicubic interpolation for better quality
        resized_img = img.resize((width, height), Image.BICUBIC)
        resized_img.save(output_path)

        print(f"Rescaled image saved to {output_path}")
