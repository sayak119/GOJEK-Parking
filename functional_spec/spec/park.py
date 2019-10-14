#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""
file used to genrate the park command
functionality.
"""

import argparse
from functional_spec.spec.parking_lot import ParkingLot


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="command to park the vehicle in already created parking lot")
    parser.add_argument("registration_number",
                        metavar="registration_number",
                        type=str,
                        help="registration number of the vehicle")
    parser.add_argument("colour",
                        metavar="colour",
                        type=str,
                        help="colour or the vehicle")
    args = parser.parse_args()
    command = "park"
    extra_arguments = [args.registration_number, args.colour]
    ParkingLot(**{"command": command, "extra_arguments": extra_arguments})
