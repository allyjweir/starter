#!/usr/bin/env sh
set -eu

# Add any pre-run steps such as injecting configuration here...

echo "Running: '${@}'"
exec $@