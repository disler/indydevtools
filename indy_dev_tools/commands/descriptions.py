import typer
from indy_dev_tools.modules.create_description import create_description
from indy_dev_tools.modules.compose_description import compose_description

app = typer.Typer()


@app.command(help="Compose a description given a completed draft directory.")
def compose():
    compose_description()


@app.command(help="Create a new description for a video.")
def create(
    script_file: str = typer.Option(
        ..., "-s", "--script-file", help="The path to the script file."
    ),
    rough_draft_title: str = typer.Option(
        None, "-r", "--rough-draft-title", help="The rough draft title of the video."
    ),
    seo_keywords: str = typer.Option(
        None,
        "-k",
        "--seo-keywords",
        help="SEO keywords to be included in the description.",
    ),
    count: int = typer.Option(
        3, "-c", "--count", help="The number of descriptions to generate."
    ),
):
    create_description(count, script_file, seo_keywords, rough_draft_title)


@app.command(help="Iterate over the description to improve it.")
def iterate(prompt: str, description: str):
    print(f"iterating description: {description}")
