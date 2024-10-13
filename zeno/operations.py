"""Functions for Zeno operation commands."""

import dnf

from zeno.rich import print_success, print_error, print_install_summary


def install_package(package_name: str):
    """Install a package using libdnf."""
    try:
        base = dnf.Base()
        base.read_all_repos()
        base.fill_sack()

        package_query = base.sack.query().filter(name=package_name)
        if not package_query:
            print_error(f"Package {package_name} not found.")
            return

        base.install(package_name)
        print_success(f"Package {package_name} installed successfully.")

        base.do_transaction()
        print_install_summary(base.transaction)

    except Exception as e:
        print_error(f"Failed to install {package_name}: {str(e)}")


def remove_package(package_name: str):
    """Remove a package."""
    try:
        base = dnf.Base()
        base.read_all_repos()
        base.fill_sack()

        base.remove(package_name)
        base.do_transaction()
        print_success(f"Package {package_name} removed successfully.")

    except Exception as e:
        print_error(f"Failed to remove {package_name}: {str(e)}")


def search_package(query: str):
    """Search for a package by query."""
    try:
        base = dnf.Base()
        base.read_all_repos()
        base.fill_sack()

        package_query = base.sack.query().filter(name__glob=query)
        for pkg in package_query.run():
            print(f"Found package: {pkg.name}-{pkg.version}")

    except Exception as e:
        print_error(f"Failed to search for {query}: {str(e)}")
