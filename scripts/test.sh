#!/usr/bin/env bash

# Run Tests
uv run pytest --cov src --cov-branch --cov-report=xml
