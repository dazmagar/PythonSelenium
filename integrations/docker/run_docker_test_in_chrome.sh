#!/bin/bash
set -e
# Run example test from inside Docker image
echo "Running example PythonSelenium test from Docker with headless Chrome..."
cd /PythonSelenium/examples/ && pytest my_first_test.py --browser=chrome --headless
exec "$@"
