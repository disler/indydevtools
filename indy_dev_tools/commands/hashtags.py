import typer
from indy_dev_tools.modules.compose_hashtags import compose_hashtags
from indy_dev_tools.modules.create_hashtags import create_hashtags

app = typer.Typer()


@app.command(help="Compose the final set of hashtags for a video.")
def compose():
    """
    Compose the final set of hashtags for a video.
    - inputs
        - `/draft/hashtags.json`
    - outputs
        - Finalized `/final/hashtags.txt` with a list of tags to use in the video.
    """
    compose_hashtags()


@app.command(
    help="Generate hashtags for a video (list of 10 comma sep, and top three)."
)
def create(
    rough_draft_title: str = typer.Option(
        ..., "--title", "-r", help="The rough draft title of the video."
    ),
    seo_keywords: str = typer.Option(
        ..., "--keywords", "-k", help="The SEO keywords for the video."
    ),
):
    """
    - Generate hashtags for a video (list of 10 comma sep, and top three).
    - Inputs
        - `-r`: The rough draft title of the video.
        - `-k`: The SEO keywords for the video.
    - Outputs
        - Tags and top three hashtags for the video output to `/draft/hashtags.json`.
    """
    create_hashtags(rough_draft_title, seo_keywords)


if __name__ == "__main__":
    app()
