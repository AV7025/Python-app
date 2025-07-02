#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv antenv
source antenv/bin/activate

echo "Installing requirements..."
pip install -r requirements.txt

echo "Starting Gunicorn..."
gunicorn --bind=0.0.0.0:8000 app:app
