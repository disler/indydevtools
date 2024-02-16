import typer
from indy_dev_tools.modules.create_description import create_description
from indy_dev_tools.modules.compose_description import compose_description

app = typer.Typer()


@app.command(
    help="Combine various /draft/* assets and generates a finalized /final/description.txt"
)
def compose():
    """
    - Compose a description given a completed draft directory.
    - Inputs
      - `<config.yt.operating_dir>/draft/descriptions.json`
      - `<config.yt.operating_dir>/draft/hashtags.json`
      - `<config.yt.operating_dir>/draft/references.txt` (optional)
    - Outputs
      - The finalized description ready for youtube in `<config.yt.operating_dir>/final/description.txt`
    """
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
