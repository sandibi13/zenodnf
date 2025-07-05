"""The main module for ZenoDNF."""

import sys
import errno

from zenodnf.rich import console
from zenodnf.zenodnf import app


def main() -> None:
    """ZenoDNF function to reference from the entry point."""
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
