#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
file used to give the leave command functionality
for parking lot
"""

import argparse
from functional_spec.spec.parking_lot import ParkingLot


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Leave command to leave any parking lot")
    parser.add_argument("lot_number",
                        type=int,
                        help="parking lot number to leave")
    args = parser.parse_args()
    command = "leave"
    extra_arguments = [args.lot_number, ]
    ParkingLot(**{'command': command,
                  'extra_arguments': extra_arguments})
