"""Main module for Zeno."""

import typer

from zeno import __version__
from zeno.rich import print_info
from zeno.operations import (
    install_package,
    remove_package,
    update_packages,
    search_packages,
    list_packages,
    get_package_info,
    get_history,
    clean_cache,
    autoremove_packages,
)

# Initialize Typer app
app = typer.Typer(help="Zeno: A blazing-fast package manager built on top of libdnf.")


# Version command
@app.command()
def version():
    """Show Zeno version."""
    print_info(f"Zeno version: {__version__}")


# Install command
@app.command()
def install(package_name: str):
    """Install a package by name."""
    install_package(package_name)


# Remove command
@app.command()
def remove(package_name: str):
    """Remove an installed package."""
    remove_package(package_name)


# Update command
@app.command()
def update():
    """Update all installed packages."""
    update_packages()


# Search command
@app.command()
def search(query: str):
    """Search for a package by name or keyword."""
    search_packages(query)


# List installed packages
@app.command("list")
def list():
    """List all installed packages."""
    list_packages()


# Get package info command
@app.command()
def show(package_name: str):
    """Get detailed information about a specific package."""
    get_package_info(package_name)


# History command
@app.command()
def history():
    """View the transaction history of package installations and removals."""
    get_history()


# Clean cache command
@app.command("clean")
def clean_package_cache():
    """Clean the package manager's cache."""
    clean_cache()


# Autoremove command
@app.command("autoremove")
def autoremove():
    """Remove orphaned packages that are no longer needed."""
    autoremove_packages()
