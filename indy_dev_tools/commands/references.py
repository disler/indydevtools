import typer
from indy_dev_tools.modules.create_formatted_references import create_formatted_references

app = typer.Typer()

@app.command()
def format_references(
    references: str = typer.Argument(..., help="The references to format.")
):
    # Assuming rough_draft_title and seo_keywords are to be input by the user as well.
    rough_draft_title = typer.prompt("Enter the rough draft title")
    seo_keywords = typer.prompt("Enter the SEO keywords")
    create_formatted_references(references, rough_draft_title, seo_keywords)

if __name__ == "__main__":
    app()
