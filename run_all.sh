#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "=========================================="
echo " Starting Wheeler Wilkinson Data Pipeline "
echo "=========================================="

# 1. Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 could not be found. Please install it to continue."
    exit 1
fi

# 2. Set up a virtual environment (keeps your system clean)
echo "[1/4] Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# 3. Install required dependencies
echo "[2/4] Installing required libraries (pandas, matplotlib)..."
pip install --upgrade pip -q
pip install pandas matplotlib -q

# 4. Execute the pipeline
echo "[3/4] Executing pipeline.py..."
echo "      (Note: Downloading data and verifying SHA-256 hashes...)"
python3 pipeline.py

# 5. Deactivate environment
deactivate

echo "[4/4] Pipeline execution complete!"
echo "Check your directory for the cleaned CSV files and generated PNG charts."
echo "=========================================="
