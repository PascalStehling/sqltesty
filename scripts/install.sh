#!/bin/bash
sudo apt-get update
sudo apt-get -y upgrade

echo "Installing UV and dependencies"
curl -LsSf https://astral.sh/uv/install.sh | sh
# uv sync --all-packages --all-groups
uv sync
