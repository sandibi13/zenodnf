#!/bin/bash

# ZenoDNF package manager installation script

echo "Starting the installation of ZenoDNF..."

# Check if Poetry is installed
if ! command -v poetry &> /dev/null
then
    echo "Poetry could not be found, installing Poetry..."
    
    # Install Poetry
    curl -sSL https://install.python-poetry.org | python3 -
    
    # Add Poetry to the current shell environment
    export PATH="$HOME/.local/bin:$PATH"
fi

echo "Poetry is installed!"

# Install project dependencies using Poetry
echo "Installing dependencies with Poetry..."
poetry install

# Ensure that Poetry shell is used
echo "Activating Poetry shell..."
poetry shell

echo "ZenoDNF package manager installed and ready to use!"

# Output helpful instructions for the user
echo "To run the ZenoDNF CLI, use the following command:"
echo "    python zenodnf-cli.py [command]"
