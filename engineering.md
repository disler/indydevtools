# Raw Engineering Documentation

## Default typer commands

```python
@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    open_in_editor: bool = typer.Option(
        False,
        "--open-in-editor",
        "-o",
        help="Open the configuration file in the default editor",
    ),
):
    """
    Print the configuration file to the console.

    Input:
        - None
    Output:
        - The configuration file is printed to the console.
    """
    if ctx.invoked_subcommand is None:
        config: IdtConfig = idt_config.load_config()
        if open_in_editor and config.yt and config.yt.config_file_path:
            typer.launch(config.yt.config_file_path)
        else:
            typer.echo(config.model_dump_json(indent=2))
```