import typer
from indy_dev_tools.modules.create_formatted_references import (
    create_formatted_references,
)

app = typer.Typer()


@app.command()
def format(
    references: str = typer.Option(
        ..., "--references", "-r", help="The references (links) to format."
    ),
    rough_draft_title: str = typer.Option(
        ..., "--title", "-t", help="The rough draft title of the video."
    ),
    seo_keywords: str = typer.Option(
        None, "--keywords", "-k", help="The SEO keywords for the video."
    ),
):
    """
    - Format the references for a video.
    - Inputs
        - `-r`: The references to format.
        - `-t`: The rough draft title of the video.
        - `-k`: The SEO keywords for the video.
    - Outputs
        - Formatted references output to `/draft/references.txt`.
    """
    create_formatted_references(references, rough_draft_title, seo_keywords)


if __name__ == "__main__":
    app()
