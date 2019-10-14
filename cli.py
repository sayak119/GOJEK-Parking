#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from functional_spec.__main__ import main
import argparse

if __name__ == "__main__":
    # defining parser for this file
    # in order to use it using command line
    # arguments
    parser = argparse.ArgumentParser(description="Parkinglot commandline")
    parser.add_argument("command",
                        metavar='Command',
                        type=str,
                        choices=['create_parking_lot', 'park', 'parking_lot_status', 'leave',
                                 'registration_numbers_for_cars_with_colour',
                                 "slot_numbers_for_cars_with_colour",
                                 "slot_number_for_registration_number", "quit"],
                        help="command to operate parkinglot")
    parser.add_argument('extra_arguments',
                        action='store',
                        nargs=argparse.REMAINDER)
    args = parser.parse_args()
    main(**vars(args))
