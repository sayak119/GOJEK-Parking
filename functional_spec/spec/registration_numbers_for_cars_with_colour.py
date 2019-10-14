#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
file used to provide the registration
numbers of cars parked in the parking
lot with a specific colour
"""

import argparse
from functional_spec.spec.parking_lot import ParkingLot


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="find the registration number of the cars parked in parkin lot using its colour")
    parser.add_argument("colour",
                        metavar="colour",
                        type=str,
                        help="colour of the vehicle")
    args = parser.parse_args()
    command = "registration_numbers_for_cars_with_colour"
    extra_arguments = [args.colour, ]
    ParkingLot(**{'command': command,
                  'extra_arguments': extra_arguments})
