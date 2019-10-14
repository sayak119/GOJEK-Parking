#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""
file used to create a parking
lot of specific size.
"""


import argparse
from functional_spec.spec.parking_lot import ParkingLot


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="command to create a parking lot of desired size")
    parser.add_argument("parking_lot_size",
                        metavar="parking_lot_size",
                        type=int,
                        help="size of the parking_lot in integer values")

    args = parser.parse_args()
    command = "create_parking_lot"
    extra_arguments = [args.parking_lot_size, ]
    ParkingLot(**{"command": command,
                  "extra_arguments": extra_arguments})
