# TFT Data Project

This project is aimed at collecting and preparing TFT match data for machine learning model training.

## Project Structure

- \data/\: Contains raw and processed data.
  - \aw/\: Raw data files.
  - \processed/\: Processed data files.
- \src/\: Source code for data collection, preparation, and model training.
- \	ests/\: Unit tests for the project.

## Setup

1. Install the required dependencies:
    \\\ash
    pip install -r requirements.txt
    \\\

2. Run the setup script to collect initial data:
    \\\ash
    python setup.py
    \\\

## Running the Project

To run individual scripts or the entire workflow, use the respective commands as described in the README.md.

## Running Tests

To run the tests, open the terminal in your project directory and execute:
    \\\ash
    pytest tests/
    \\\

