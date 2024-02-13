import typer
from indy_dev_tools.modules.create_hashtags import create_hashtags

app = typer.Typer()


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
    create_hashtags(rough_draft_title, seo_keywords)


if __name__ == "__main__":
    app()