"""The main module for Zeno."""

import sys
import errno

from zeno.rich import console
from zeno.zeno import app


def main() -> None:
    """Zeno function to reference from the entry point."""
    try:
        app()
    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting at your request.[/bold red]")
        sys.exit(130)
    except BrokenPipeError:
        sys.stderr.close()
    except OSError as error:
        if error.errno == errno.ENOSPC:
            console.print("[bold red]Error: No space left on device.[/bold red]")
            sys.exit(1)
        raise error from error
