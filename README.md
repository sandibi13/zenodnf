# ZenoDNF

ZenoDNF is a fast, modern package manager built on `libdnf`, offering speed and aesthetic improvements over `dnf`. It provides a streamlined, user-friendly command-line interface for software installation, removal, updates, and more.

_Please note that this project relies on `libdnf`, which is currently being rewritten and rapidly developed. As a result, certain functionality may or may not work as expected due to `libdnf`'s instability._

## Installation

Before installing, make sure you have Poetry installed to manage dependencies.

```bash
# Clone the repository
git clone https://github.com/sandibi13/zenodnf.git
cd zenodnf

# Install dependencies using Poetry
poetry install

# Run the setup script
./zenodnf-pyinstall.sh
```

## Usage

Here's how you can use some of the core commands:

```bash
# Install a package
zenodnf install [package_name]

# Remove a package
zenodnf remove [package_name]

# Update all packages
zenodnf update

# Search for a package
zenodnf search [query]

# View transaction history
zenodnf history
```

## Features

-   Fast and Aesthetic: A better alternative to dnf, with enhanced output and speed improvements.
-   Rich Formatting: Leveraging the Rich library for beautiful, colorful output.
-   Interactive Search: Quickly search for packages with a more interactive UI.
-   Transaction History: Easily track and view your package management history.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes.
4.  Push to your fork.
5.  Create a pull request.

**Any contributions will be appreciated as this project is still in active development!**
