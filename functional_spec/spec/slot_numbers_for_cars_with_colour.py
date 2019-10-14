#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
file used to give the slot
numbers of the parking_lot slots
where a particular colour car is parked
"""

import argparse
from parking_lot import ParkingLot


if __name__ == "__main__":
    parser = arparse.ArgumentParser(desription="find the slot number of the cars parked in parkin lot using its colour")
    parser.add_argument("colour",
                        metavar="colour",
                        type=str,
                        help="colour of the vehicle")
    args = parser.parse_args()
    command = "slot_numbers_for_cars_with_colour"
    extra_arguments = [args.colour, ]
    ParkingLot(**{'command': command,
                  'extra_arguments': extra_arguments})
