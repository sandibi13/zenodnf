"""Rich options for ZenoDNF output."""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress

# Initialize a Rich console instance
console = Console()


def print_success(message: str):
    """Print success messages in green."""
    console.print(f"[bold green]✔ {message}[/bold green]")


def print_error(message: str):
    """Print error messages in red."""
    console.print(f"[bold red]✖ {message}[/bold red]")


def print_info(message: str):
    """Print informational messages in blue."""
    console.print(f"[bold cyan]ℹ {message}[/bold cyan]")


def print_package_table(packages):
    """Print a table of packages."""
    table = Table(title="Installed Packages")
    table.add_column("Package", justify="left", style="cyan", no_wrap=True)
    table.add_column("Version", justify="center", style="magenta")
    table.add_column("Description", justify="left")

    for package in packages:
        table.add_row(package["name"], package["version"], package["description"])

    console.print(table)


def print_package_info(package):
    """Print detailed info for a single package."""
    console.print(
        Panel(
            f"[bold cyan]{package['name']}[/bold cyan]\n"
            f"[bold]Version:[/bold] {package['version']}\n"
            f"[bold]Summary:[/bold] {package['summary']}\n"
            f"[bold]Description:[/bold] {package['description']}\n"
            f"[bold]Repo:[/bold] {package['repo']}"
        )
    )


def show_progress():
    """Display progress for an operation."""
    with Progress() as progress:
        task = progress.add_task("[cyan]Processing...", total=100)
        while not progress.finished:
            progress.update(task, advance=0.5)
