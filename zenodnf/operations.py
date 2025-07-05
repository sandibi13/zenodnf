"""Functions for the ZenoDNF commands."""

import libdnf

from zenodnf.rich import (
    print_success,
    print_error,
    print_info,
    print_package_info,
    print_package_table,
    show_progress,
)


# Create a base object to interact with libdnf
def create_base():
    base = libdnf.base.Base()
    base.load_config_from_file()  # Loads the default config file
    base.setup()  # Initializes necessary components (repositories, etc.)
    return base


# Install the mentioned package(s)
def install_package(package_name: str):
    try:
        base = create_base()
        sack = base.get_rpm_sack()
        repo_query = base.get_repo_sack().new_query()

        # Searching for the package
        package_query = repo_query.filter_name([package_name])
        package_set = package_query.run()

        if not package_set:
            print_error(f"Package '{package_name}' not found.")
            return

        package = package_set[0]

        # Start the transaction to install
        transaction = base.get_transaction()
        transaction.install(package)

        show_progress()  # Show progress while the package installs

        result = transaction.run()

        if result == 0:
            print_success(f"Successfully installed '{package_name}'.")
        else:
            print_error(f"Failed to install '{package_name}'.")

    except Exception as e:
        print_error(f"Error during installation: {e}")


# Remove the mentioned package(s)
def remove_package(package_name: str):
    try:
        base = create_base()
        sack = base.get_rpm_sack()
        package_query = sack.new_query().filter_name([package_name])

        # Searching for the installed package
        installed_packages = package_query.filter_installed().run()
        if not installed_packages:
            print_error(f"Package '{package_name}' is not installed.")
            return

        package = installed_packages[0]

        # Start the transaction to remove
        transaction = base.get_transaction()
        transaction.remove(package)

        show_progress()  # Show progress while the package is removed

        result = transaction.run()

        if result == 0:
            print_success(f"Successfully removed '{package_name}'.")
        else:
            print_error(f"Failed to remove '{package_name}'.")

    except Exception as e:
        print_error(f"Error during removal: {e}")


# Update all the packages
def update_packages():
    try:
        base = create_base()
        repo_sack = base.get_repo_sack()

        # Load the repositories and check for updates
        repo_sack.update_and_load_enabled_repos(True)
        sack = base.get_rpm_sack()
        package_query = sack.new_query().filter_latest().filter_upgradable()
        upgradable_packages = package_query.run()

        if not upgradable_packages:
            print_info("No packages to update.")
            return

        # Start the transaction to update
        transaction = base.get_transaction()
        for package in upgradable_packages:
            transaction.install(package)

        show_progress()  # Show progress while packages update

        result = transaction.run()

        if result == 0:
            print_success("Successfully updated all packages.")
        else:
            print_error("Failed to update some packages.")

    except Exception as e:
        print_error(f"Error during update: {e}")


# Search for the mentioned package
def search_packages(query: str):
    try:
        base = create_base()
        sack = base.get_rpm_sack()
        package_query = sack.new_query().filter_name([query])

        search_results = package_query.run()
        if not search_results:
            print_info(f"No packages found for query: {query}")
            return

        print_info(f"Search results for '{query}':")
        packages = [
            {
                "name": package.get_name(),
                "version": package.get_evr(),
                "description": package.get_summary(),
            }
            for package in search_results
        ]
        print_package_table(packages)

    except Exception as e:
        print_error(f"Error during search: {e}")


# List all installed packages
def list_packages():
    try:
        base = create_base()
        sack = base.get_rpm_sack()

        # Query to list installed packages
        package_query = sack.new_query().filter_installed()
        installed_packages = package_query.run()

        if not installed_packages:
            print_info("No packages are currently installed.")
            return

        packages = [
            {
                "name": package.get_name(),
                "version": package.get_evr(),
                "description": package.get_summary(),
            }
            for package in installed_packages
        ]

        print_package_table(packages)

    except Exception as e:
        print_error(f"Error listing packages: {e}")


# Get detailed package info
def get_package_info(package_name: str):
    try:
        base = create_base()
        sack = base.get_rpm_sack()
        package_query = sack.new_query().filter_name([package_name])

        search_results = package_query.run()
        if not search_results:
            print_info(f"Package '{package_name}' not found.")
            return

        package = search_results[0]
        package_info = {
            "name": package.get_name(),
            "version": package.get_evr(),
            "summary": package.get_summary(),
            "description": package.get_description(),
            "repo": package.get_repo_id(),
        }
        print_package_info(package_info)

    except Exception as e:
        print_error(f"Error getting package info: {e}")


# Get transaction history
def get_history():
    try:
        base = create_base()
        history = base.get_transaction_history()

        transactions = history.list_transactions()

        if not transactions:
            print_info("No transaction history found.")
            return

        print_info("Transaction History:")
        for transaction in transactions:
            print_info(
                f"- ID: {transaction.get_id()} | Command: {transaction.get_cmdline()} | Time: {transaction.get_begin_ts()}"
            )

    except Exception as e:
        print_error(f"Error retrieving history: {e}")


# Clean cached metadata and packages
def clean_cache():
    try:
        base = create_base()
        repo_sack = base.get_repo_sack()

        # Clean the metadata cache
        repo_sack.clean_cache()

        print_success("Cache cleaned successfully.")

    except Exception as e:
        print_error(f"Error cleaning cache: {e}")


# Autoremove unused dependencies and packages
def autoremove_packages():
    try:
        base = create_base()
        transaction = base.get_transaction()

        # Mark orphaned packages for removal
        transaction.mark_orphaned()

        if transaction.get_transaction_size() == 0:
            print_info("No orphaned packages to remove.")
            return

        show_progress()  # Show progress while removing orphaned packages

        result = transaction.run()

        if result == 0:
            print_success("Successfully removed unused packages.")
        else:
            print_error("Failed to remove some packages.")

    except Exception as e:
        print_error(f"Error during autoremove: {e}")
