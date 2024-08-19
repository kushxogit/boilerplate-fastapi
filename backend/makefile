# Makefile for managing the Python project

# Variables
VENV_DIR := venv

.PHONY: all install install-dev clean run test

# Default target
all: install

# Create a virtual environment and install dependencies
$(VENV_DIR)/bin/activate:
	python3 -m venv $(VENV_DIR)
	. $(VENV_DIR)/bin/activate; pip install --upgrade pip
	. $(VENV_DIR)/bin/activate; pip install -r requirements.txt

# Install dependencies
install: $(VENV_DIR)/bin/activate

# Install development dependencies
install-dev: $(VENV_DIR)/bin/activate
	. $(VENV_DIR)/bin/activate; pip install -r requirements-dev.txt

# Clean the environment
clean:
	rm -rf $(VENV_DIR)
	find . -type d -name "__pycache__" -exec rm -rf {} +

# Run the application
run: install
	. $(VENV_DIR)/bin/activate; uvicorn main:app --reload

# Run tests
test: install
	. $(VENV_DIR)/bin/activate; pytest

# Additional commands can be added here