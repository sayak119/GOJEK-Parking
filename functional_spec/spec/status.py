#! /usr/bin/env python3

"""
file used to give the leave command functionality
for parking lot
"""
from functional_spec.spec.parking_lot import ParkingLot

if __name__ == "__main__":
    command = "status"
    extra_arguments = list()
    ParkingLot(**{'command': command,
                  'extra_arguments': extra_arguments})
