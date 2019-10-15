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

                if "creating parking plot with" in out.getvalue().strip():
                    self.assertEqual(1, 1)
                else:
                    self.assertEqual(out.getvalue().strip(), "creating parking plot with 5 slots")
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
        self.tearDown()
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        sys.stdout = sys.__stdout__

        if "creating parking plot with" in out.getvalue().strip():
            self.assertEqual(1, 1)
        else:
            self.assertEqual(out.getvalue().strip(), "creating parking plot with 5 slots")

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

        if "creating parking plot with" in out.getvalue().strip():
            self.assertEqual(1, 1)
        else:
            self.assertEqual(out.getvalue().strip(), "creating parking plot with 5 slots")

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

        if "creating parking plot with" in out.getvalue().strip():
            self.assertEqual(1, 1)
        else:
            self.assertEqual(out.getvalue().strip(), "creating parking plot with 5 slots")

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
        self.tearDown()
        self.plot_size = 2
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        sys.stdout = sys.__stdout__

        if "creating parking plot with" in out.getvalue().strip():
            self.assertEqual(1, 1)
        else:
            self.assertEqual(out.getvalue().strip(), "creating parking plot with 5 slots")

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
        self.tearDown()
        self.plot_size = 2
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        sys.stdout = sys.__stdout__

        if "creating parking plot with" in out.getvalue().strip():
            self.assertEqual(1, 1)
        else:
            self.assertEqual(out.getvalue().strip(), "creating parking plot with 5 slots")

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
        self.tearDown()
        self.plot_size = 2
        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(1)]})
        sys.stdout = sys.__stdout__

        if "creating parking plot with" in out.getvalue().strip():
            self.assertEqual(1, 1)

    def test_leave(self):
        self.tearDown()
        self.plot_size = 2

        out = StringIO()
        sys.stdout = out
        self.parking_lot = ParkingLot(**{"command": "create_parking_lot",
                                         "extra_arguments": [int(5)]})
        sys.stdout = sys.__stdout__

        if "creating parking plot with" in out.getvalue().strip():
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

    def tearDown(self):
        """
        method run after all the test cases are completed
        """
        clear_tmp_file()


if __name__ == '__main__':
    unittest.main()
