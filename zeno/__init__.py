"""Zeno package manager."""

import os
import sys
from subprocess import run

from rich.console import Console

console = Console()

# Stop this code from running during shell completions
if not os.environ.get("_ZENO_COMPLETE"):
    if len(sys.argv) == 1:
        sys.exit(run(["man", "zeno"]).returncode)

__version__ = "0.1.0"


def color_text(text: str, text_color: str = "") -> None:
    """Use rich to color text."""
    if text_color:
        console.print(f"[{text_color}]{text}[/]")
    else:
        console.print(text)


def print_version() -> None:
    """Print Zeno version."""
    console.print(f"Zeno [blue]version {__version__}[/blue]")


def print_help() -> None:
    """Show help message."""
    console.print("Zeno - A fast package manager on top of libdnf\n")
    console.print("[bold]Usage:[/bold] zeno [command] [options]\n")
    console.print("[bold]Commands:[/bold]")
    console.print("  install <package>  - Install a package")
    console.print("  remove <package>   - Remove a package")
    console.print("  search <query>     - Search for a package")
    console.print("  history            - Show transaction history")
