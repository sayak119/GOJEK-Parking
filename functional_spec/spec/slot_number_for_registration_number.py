#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""
file used to provide the slot number
where car with specific registration number
is parked.
"""

import argparse
from functional_spec.spec.parking_lot import ParkingLot


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="find the registration number of the cars parked in parkin lot using its colour")  # NOQA
    parser.add_argument("registration_number",
                        metavar="registration_number",
                        type=str,
                        help="registration number of vehicle whose slot number is to be found")
    args = parser.parse_args()
    command = "slot_number_for_registration_number"
    extra_arguments = [args.registration_number, ]
    ParkingLot(**{'command': command,
                  'extra_arguments': extra_arguments})
