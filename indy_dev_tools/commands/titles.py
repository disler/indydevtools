import typer

app = typer.Typer()


@app.command()
def create(user_name: str):
    print(f"Creating user: {user_name}")


@app.command()
def iterate(user_name: str):
    print(f"iterating user: {user_name}")


if __name__ == "__main__":
    app()
