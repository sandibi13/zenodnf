"""The main module for Zeno."""

import typer

from zeno import operations, rich

app = typer.Typer()


@app.command()
def install(package: str):
    """Install a package."""
    operations.install_package(package)


@app.command()
def remove(package: str):
    """Remove a package."""
    operations.remove_package(package)


@app.command()
def search(query: str):
    """Search for a package."""
    operations.search_package(query)


@app.command()
def history():
    """Show the transaction history."""
    rich.print_history()


if __name__ == "__main__":
    app()
