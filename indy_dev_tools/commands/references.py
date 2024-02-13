import typer
from indy_dev_tools.modules.create_formatted_references import (
    create_formatted_references,
)

app = typer.Typer()


@app.command()
def format(
    references: str = typer.Argument(..., help="The references to format."),
    rough_draft_title: str = typer.Argument(
        ..., help="The rough draft title of the video."
    ),
    seo_keywords: str = typer.Argument(None, help="The SEO keywords for the video."),
):
    create_formatted_references(references, rough_draft_title, seo_keywords)


if __name__ == "__main__":
    app()
