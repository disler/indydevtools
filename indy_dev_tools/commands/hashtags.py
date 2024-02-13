import typer
from indy_dev_tools.modules.create_hashtags import create_hashtags

app = typer.Typer()


@app.command()
def generate(
    rough_draft_title: str = typer.Option(
        ..., "--title", "-t", help="The rough draft title of the video."
    ),
    seo_keywords: str = typer.Option(
        ..., "--keywords", "-k", help="The SEO keywords for the video."
    ),
):
    hashtags = create_hashtags(rough_draft_title, seo_keywords)
    for hashtag in hashtags:
        print(hashtag)


if __name__ == "__main__":
    app()
