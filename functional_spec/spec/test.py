#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
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
        self.plot_size = 5
        for plot_number in range(1, self.plot_size + 2):
            if plot_number <= self.plot_size:
                self.parking_lot = ParkingLot(**{"comand": "park",
                                                 "extra_arguments": ["test_registration_number %s" % plot_number,
                                                                     "White"]})
                self.assertEqual(self.parking_lot.__status__,
                                 'Alloting parking plot number: %s' % plot_number)
            else:
                self.assertEqual(self.parking_lot.__status__,
                                 'Sorry, parking lot is full')

    def test_leave_command(self):
        """
        test the complete functionality
        of leave command w.r.t to ParkingLot
        and ParkingLotManager.
        """
        self.plot_size = 5
        for i in range(1, self.plot_size + 2):
            self.parking_lot = ParkingLot(**{"comand": "leave",
                                             "extra_arguments": [str(i), ]})
            if i <= self.plot_size:
                self.assertEqual(self.parking_lot.__status__,
                                 'slot number %s is free')
                if self.parking_lot.hasattr('pickle') and self.parking_lot.pickle is not None:
                    self.assertTrue(
                        len(self.parking_lot.pickle.empty) +
                        len(self.parking_lot.pickle.consumed),
                        self.parking_lot.pickle.size)
                else:
                    self.assertTrue(
                        len(self.parking_lot.manager.empty) +
                        len(self.parking_lot.manager.consumed),
                        self.parking_lot.pickle.size)
            else:
                self.assertEqual(self.parking_lot.__status__,
                                 'Parking lot is already empty')

    def test_slot_numbers_functionality(self):
        """
        method used to test the slot_numbers_for_cars_with_colour command
        """
        self.plot_size = 5
        for plot_number in range(1, self.plot_size + 1):
            self.parking_lot = ParkingLot(**{"comand": "park",
                                             "extra_arguments": ["test_registration_number %s" % plot_number,
                                                                 "White"]})
            self.parking_lot = ParkingLot(**{"comand": "slot_numbers_for_cars_with_colour",
                                             "extra_arguments": ["White"]})
            self.assertEqual(self.parking_lot.manager.__status__, list(
                range(1, plot_number + 1)))
        self.parking_lot = ParkingLot(**{"comand": "slot_numbers_for_cars_with_colour",
                                         "extra_arguments": ["White"]})
        try:
            self.assertEqual(
                self.parking_lot.manager.__status__, "Not found")
        except AttributeError:
            self.assertEqual(
                self.parking_lot.pickle.__status__, "Not found")

    def tearDown(self):
        """
        method run after all the test cases are completed
        """
        clear_tmp_file()


if __name__ == '__main__':
    unittest.main()
