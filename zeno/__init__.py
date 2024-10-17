"""Zeno package manager."""

import os
import sys
from subprocess import run
from rich.console import Console

# Stop this code from running during shell completions
if not os.environ.get("_ZENO_COMPLETE"):
    # If zeno is run with no arguments, show the help page
    if len(sys.argv) == 1:
        sys.exit(run([sys.executable, "-m", "zeno", "--help"]).returncode)

# Set up console for rich output
console = Console()

__version__ = "0.2.0"
