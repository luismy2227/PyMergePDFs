#!/bin/bash

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
  echo "Python3 could not be found"
  exit
fi

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

echo "Setup complete. Virtual environment created and packages installed."
