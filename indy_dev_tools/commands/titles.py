import typer
from indy_dev_tools.modules.compose_title import compose_titles
from indy_dev_tools.modules.create_title import create_title

app = typer.Typer()


@app.command(
    help="Select titles from 'draft/titles.json' for the final title for a video."
)
def compose():
    compose_titles()


@app.command(help="Create a new title for a video.")
def create(
    rough_draft_title: str = typer.Option(
        "", "-r", "--rough-draft-title", help="The rough draft title of the video."
    ),
    script_file: str = typer.Option(
        None,
        "-s",
        "--script-file",
        help="The file containing the script for the video.",
    ),
    count: int = typer.Option(
        3, "-c", "--count", help="The number of titles to create."
    ),
    seo_keywords: str = typer.Option(
        None, "-k", "--seo-keywords", help="The SEO keywords for the video."
    ),
):
    create_title(count, rough_draft_title, script_file, seo_keywords)


@app.command(help="Iterate over user data (unimplemented).")
def iterate(title: str):
    raise NotImplementedError("This command is not yet implemented.")


if __name__ == "__main__":
    app()
