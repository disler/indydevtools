import typer
from typing import Optional

app = typer.Typer()


@app.command()
def run(
    alias: str = typer.Option(..., "-a", help="Alias"),
    prompt: str = typer.Option(..., "-p", help="Prompt"),
    vars: Optional[str] = typer.Option(
        None, "-v", help="Custom variables in key=value format separated by commas"
    ),
):
    # Process defined options
    print(f"Alias: {alias}")
    print(f"Prompt: {prompt}")

    # Process custom variables string
    custom_vars = {}
    if vars:
        for option in vars.split(","):
            key, value = option.split("=")
            custom_vars[key] = value

    print("Custom Variables:")
    for var, value in custom_vars.items():
        print(f"{var}: {value}")
