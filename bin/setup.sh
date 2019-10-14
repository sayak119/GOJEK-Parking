#!/usr/bin/env bash

if [ -n "$ZSH_VERSION" ]; then
    FILE_DIR="$( cd "$( dirname "${(%):-%x}" )" >/dev/null && pwd )"
else
    FILE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
fi
BASE_DIR="${FILE_DIR%/*}"

# install requirements.
pip install -r "$BASE_DIR/requirements.txt"


# Build the project
pyinstaller "$BASE_DIR/functional_spec/spec/parking_lot.py" --onefile --name "parking_lot" --distpath "$FILE_DIR" --workpath "/tmp" --specpath="/tmp"
pyinstaller "$BASE_DIR/functional_spec/spec/create_parking_lot.py" --onefile --name "create_parking_lot" --distpath "$FILE_DIR" --workpath "/tmp" --specpath="/tmp"
pyinstaller "$BASE_DIR/functional_spec/spec/leave.py" --onefile --name "leave" --distpath "$FILE_DIR" --workpath "/tmp" --specpath="/tmp"
pyinstaller "$BASE_DIR/functional_spec/spec/status.py" --onefile --name "status" --distpath "$FILE_DIR" --workpath "/tmp" --specpath="/tmp"
pyinstaller "$BASE_DIR/functional_spec/spec/slot_numbers_for_cars_with_colour.py" --onefile --name "slot_numbers_for_cars_with_colour" --distpath "$FILE_DIR" --workpath "/tmp" --specpath="/tmp"
pyinstaller "$BASE_DIR/functional_spec/spec/slot_number_for_registration_number.py" --onefile --name "slot_number_for_registration_number" --distpath "$FILE_DIR" --workpath "/tmp" --specpath="/tmp"
pyinstaller "$BASE_DIR/functional_spec/spec/registration_numbers_for_cars_with_colour.py" --onefile --name "registration_numbers_for_cars_with_colour" --distpath "$FILE_DIR" --workpath "/tmp" --specpath="/tmp"
pyinstaller "$BASE_DIR/functional_spec/spec/park.py" --onefile --name "park" --distpath "$FILE_DIR" --workpath "/tmp" --specpath="/tmp"
pyinstaller "$BASE_DIR/functional_spec/spec/test.py" --onefile --name "run_test" --distpath "$FILE_DIR" --workpath "/tmp" --specpath="/tmp"

# export to path
export PATH=$FILE_DIR:$PATH
