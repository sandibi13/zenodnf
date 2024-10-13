"""Rich options for Zeno output."""

from rich.console import Console
from rich.table import Table

console = Console()


def print_success(message: str):
    """Prints a success message"""
    console.print(f"[bold green]Success:[/bold green] {message}")


def print_error(message: str):
    """Prints an error message"""
    console.print(f"[bold red]Error:[/bold red] {message}")


def print_install_summary(transaction):
    """Prints a summary of the transaction after installation."""
    table = Table(title="Transaction Summary")

    table.add_column("Action", justify="right", style="cyan", no_wrap=True)
    table.add_column("Package", style="magenta")
    table.add_column("Version", style="green")

    for item in transaction.items():
        table.add_row(item.action, item.name, item.version)

    console.print(table)


def print_history():
    # This would load from a history management system
    console.print("[bold]Transaction History:[/bold]")
    # For now just a placeholder
    console.print("No history available.")
