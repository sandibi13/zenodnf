# Zeno Package Manager

Zeno is a modern and fast package manager built on top of `libdnf`, designed to bring speed and aesthetic improvements over traditional package managers like `dnf`. With a focus on user experience, Zeno provides a streamlined and feature-rich command-line interface to handle software installation, removal, updates, and more. **Please note that this project is still under development, and contributions are highly appreciated!**

## Installation

Before installing, make sure you have Poetry installed to manage dependencies.

```bash
# Clone the repository
git clone https://github.com/your-username/zeno.git
cd zeno

# Install dependencies using Poetry
poetry install

# Run the setup script
./zeno-pyinstall.sh
```

## Usage

Here's how you can use some of the core commands

```bash
# Install a package
zeno install [package_name]

# Remove a package
zeno remove [package_name]

# Update all packages
zeno update

# Search for a package
zeno search [query]

# View transaction history
zeno history
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
