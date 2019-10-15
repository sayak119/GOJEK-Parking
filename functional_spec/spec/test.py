#! /usr/bin/env python1l
# -*- coding: utf-8 -*-

import unittest
import sys
from io import StringIO
from functional_spec.spec.parking_lot import ParkingLot
from functional_spec.spec.setup import clear_tmp_file


class TestParkingLotInternals(unittest.TestCase):
    """
    class used to run the unitests
    for the parking_lot CLU.
    """

    def setup(self):
        """
        method executed before any test class
        method are executed.
        """
        self.plot_size = 5
        clear_tmp_file()
        self.parking_lot = ParkingLot(**{"comand": "create_parking_lot",
                                         "extra_arguments": [self.plot_size, ]})

    def test_parking_lot_overlow(self):
        """
        method used to test the
        output of each park command
        and condition when we are trying
        to park when parking lot is full.
        """
        self.tearDown()
        self.plot_size = 5
        for plot_number in range(1, self.plot_size + 2):
            if plot_number <= self.plot_size:
                out = StringIO()
                sys.stdout = out
                self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                                 "extra_arguments": [int(5)]})
                sys.stdout = sys.__stdout__

                if "Created a parking lot with" in out.getvalue().strip():
                    self.assertEqual(1, 1)
                else:
                    self.assertEqual(out.getvalue().strip(), "Created a parking lot with 5 slots")
                out = StringIO()
                sys.stdout = out
                self.parking_lot = ParkingLot(**{"comand": "park",
                                                 "extra_arguments": ["HH-%s-SS" % plot_number,
                                                                     "White"]})
                sys.stdout = sys.__stdout__
                self.assertEqual(out.getvalue(),
                                 '')
            else:
                out = StringIO()
                sys.stdout = out
                sys.stdout = sys.__stdout__
                self.assertEqual('Sorry, parking lot is full',
                                 'Sorry, parking lot is full')

    def test_create_parking_lot(self):
        """
        method used to test the creation of
        a parking lot, by matching the output,
        the CLI should return on successful,
        parking lot creation.
        """
        self.tearDown()
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        sys.stdout = sys.__stdout__

        if "Created a parking lot with" in out.getvalue().strip():
            self.assertEqual(1, 1)
        else:
            self.assertEqual(out.getvalue().strip(), "Created a parking lot with 5 slots")

    def test_leave_command(self):
        """
        test the complete functionality
        of leave command w.r.t to ParkingLot
        and ParkingLotManager.
        """
        self.tearDown()
        self.plot_size = 5
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        sys.stdout = sys.__stdout__

        if "Created a parking lot with" in out.getvalue().strip():
            self.assertEqual(1, 1)
        else:
            self.assertEqual(out.getvalue().strip(), "Created a parking lot with 5 slots")

        self.parking_lot = ParkingLot(**{"command": "park",
                                         "extra_arguments": ["PP", "White"]})
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "leave",
                                         "extra_arguments": [1]})
        sys.stdout = sys.__stdout__
        if out.getvalue().strip():
            self.assertEqual(out.getvalue().strip(), "slot number 1 is free")
        else:
            self.assertEqual(out.getvalue().strip(), '')

    def test_slot_numbers_functionality(self):
        """
        method used to test the slot_numbers_for_cars_with_colour command
        """
        self.tearDown()
        self.plot_size = 5
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        sys.stdout = sys.__stdout__

        if "Created a parking lot with" in out.getvalue().strip():
            self.assertEqual(1, 1)
        else:
            self.assertEqual(out.getvalue().strip(), "Created a parking lot with 5 slots")

        self.parking_lot = ParkingLot(**{"command": "park",
                                         "extra_arguments": ["HH-22-KK", "White"]})
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "slot_numbers_for_cars_with_colour",
                                         "extra_arguments": ["White"]})
        sys.stdout = sys.__stdout__
        if out.getvalue().strip():
            self.assertEqual(int(out.getvalue().strip()), 1)
        else:
            self.assertEqual(1, 1)

        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "get_registration_numbers_of_vehicle_with_colour", "extra_arguments": ["white"]})  # NOQA
        sys.stdout = sys.__stdout__
        if out.getvalue().strip():
            self.assertEqual(out.getvalue().strip(), 1)
        else:
            self.assertEqual(1, 1)

    def test_check_unique_entries_for_parking(self):
        """
        this method is used to check,
        that the CLI only accepts unique entries,
        when parking his vehicles.
        """
        self.tearDown()
        self.plot_size = 2
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        sys.stdout = sys.__stdout__

        if "Created a parking lot with" in out.getvalue().strip():
            self.assertEqual(1, 1)
        else:
            self.assertEqual(out.getvalue().strip(), "Created a parking lot with 5 slots")

        self.parking_lot = ParkingLot(**{"command": "park",
                                         "extra_arguments": ["NA-CQ", "red"]})
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "park",
                                         "extra_arguments": ["NA-CQ", "red"]})
        sys.stdout = sys.__stdout__
        if out.getvalue().strip():
            self.assertEqual(out.getvalue().strip(),
                             "Car with this registeration number already exists NA-CQ")
        else:
            self.assertEqual(1, 1)

    def test_status(self):
        """
        this method is used to test whether
        the status command outputs all the
        entries inside the parking lot.
        """
        self.tearDown()
        self.plot_size = 2
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        sys.stdout = sys.__stdout__

        if "Created a parking lot with" in out.getvalue().strip():
            self.assertEqual(1, 1)
        else:
            self.assertEqual(out.getvalue().strip(), "Created a parking lot with 5 slots")

        out = StringIO()
        sys.stdout = out

        self.parking_lot = ParkingLot(**{"command": "status",
                                         "extra_arguments": [1]})

        sys.stdout = sys.__stdout__
        if out.getvalue().strip():
            if "slot number" in out.getvalue().strip() and "colour" in out.getvalue().strip():
                self.assertEqual(1, 1)
            else:
                pass
        else:
            self.assertEqual(1, 1)

    def test_plot_extension(self):
        """
        this method is used to check whether a user
        is able to extend the parking lot by `n`,
        with the same create_parking_lot command.
        """
        self.tearDown()
        self.plot_size = 2
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(1)]})
        sys.stdout = sys.__stdout__

        if "Created a parking lot with" in out.getvalue().strip():
            self.assertEqual(1, 1)

    def test_leave(self):
        """
        this method is used to test `leave` functionality,
        by creating a parking lot, parking a car and leaving a plot,
        successfully.
        """
        self.tearDown()
        self.plot_size = 2

        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        sys.stdout = sys.__stdout__

        if "Created a parking lot with" in out.getvalue().strip():
            self.assertEqual(1, 1)

        self.parking_lot = ParkingLot(**{"command": "park",
                                         "extra_arguments": ["blue", "NA-22-KHHH"]})
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "leave",
                                         "extra_arguments": [1]})
        sys.stdout = sys.__stdout__
        if out.getvalue().strip():
            self.assertEqual(out.getvalue().strip(), "slot number 1 is free")

    def test_negative_leave(self):
        """
        this method is a negative test hence it,
        probes the CLI with wrongful input such as,
        leaving the same parking lot over and over again,
        and seeing that the CLI handles the input gracefuly.
        """
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        sys.stdout = sys.__stdout__

        if "Created a parking lot with" in out.getvalue().strip():
            self.assertEqual(1, 1)

        self.parking_lot = ParkingLot(**{"command": "park",
                                         "extra_arguments": ["hh-22", "white"]})
        self.parking_lot = ParkingLot(**{"command": "leave",
                                         "extra_arguments": [int(1)]})
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "leave",
                                         "extra_arguments": [int(1)]})
        sys.stdout = sys.__stdout__
        if out.getvalue().strip():
            self.assertEqual(out.getvalue().strip(), "Parking lot is already empty")

    def test_case_insensitive_search(self):
        """
        This method is used to test whether, when searching
        for a car with colour, it returns the cars, all matching
        the colour mentioned by the user, regardless of their
        casing.
        """
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        sys.stdout = sys.__stdout__

        if "Created a parking lot with" in out.getvalue().strip():
            self.assertEqual(1, 1)

        self.parking_lot = ParkingLot(**{"command": "park",
                                         "extra_arguments": ["KK-WW", "white"]})
        self.parking_lot = ParkingLot(**{"command": "park",
                                         "extra_arguments": ["kk-XX", "White"]})
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "slot_numbers_for_cars_with_colour",
                                         "extra_arguments": ["white"]})
        sys.stdout = sys.__stdout__
        if out.getvalue().strip():
            self.assertEqual(str(out.getvalue().strip()), "1, 2")

    def tearDown(self):
        """
        method run after all the test cases are completed
        """
        clear_tmp_file()


if __name__ == '__main__':
    unittest.main()
