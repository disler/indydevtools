import typer
from indy_dev_tools.modules.create_description import create_description

app = typer.Typer()


@app.command()
def create(
    script_file: str = typer.Option(..., "-s", "--script-file"),
    rough_draft_title: str = typer.Option(None, "-r", "--rough-draft-title"),
    seo_keywords: str = typer.Option(None, "-k", "--seo-keywords"),
    count: int = typer.Option(3, "-c", "--count"),
):
    print(f"Rough Draft Title: {rough_draft_title}")
    print(f"Script File: {script_file}")
    print(f"SEO Keywords: {seo_keywords}")

    seo_keywords_list = seo_keywords.split(",") if seo_keywords else None
    create_description(count, script_file, seo_keywords_list, rough_draft_title)


@app.command()
def iterate(prompt: str, description: str):
    print(f"iterating description: {description}")


if __name__ == "__main__":
    app()
