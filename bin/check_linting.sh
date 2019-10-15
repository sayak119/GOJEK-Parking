#!/bin/bash

if [ -n "$ZSH_VERSION" ]; then
    FILE_DIR="$( cd "$( dirname "${(%):-%x}" )" >/dev/null && pwd )"
else
    FILE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
fi
BASE_DIR="${FILE_DIR%/*}"

echo "Checking for any linting errors..."
flake8 $BASE_DIR/functional_spec/spec/*.py
echo "trying to fix these issues..."
autopep8 --in-place $BASE_DIR/functional_spec/spec/*.py
echo "Checking again to see if anything was missed"
flake8 $BASE_DIR/functional_spec/spec/*.py
