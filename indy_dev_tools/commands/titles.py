import typer
from indy_dev_tools.modules.create_title import create_title

app = typer.Typer()


@app.command()
def create(
    rough_draft_title: str = typer.Option(None, "-r", "--rough-draft-title"),
    script_file: str = typer.Option(None, "-s", "--script-file"),
    count: int = typer.Option(3, "-c", "--count"),
    seo_keywords: str = typer.Option(None, "-k", "--seo-keywords"),
):
    print(f"Rough Draft Title: {rough_draft_title}")
    print(f"Script File: {script_file}")

    create_title(count, rough_draft_title, script_file, seo_keywords)


@app.command()
def iterate(user_name: str):
    print(f"iterating user: {user_name}")


if __name__ == "__main__":
    app()
