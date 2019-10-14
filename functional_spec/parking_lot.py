#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import pickle
import argparse
from functional_spec.setup import clear_tmp_file
import sys

class ParkingLot:
    """
    class used to define the parking lot
    specifation and methods to implement the
    parking lot functionality
    """
    def __init__(self, *args, **kwargs):
        # instance variable initialization
        self.command = kwargs.get('command')
        self.extra_arguments = kwargs.get('extra_arguments')
        self.pickle_file_dir = os.path.join('/tmp', 'parking_lot')
        # parkining_lot
        # class lifecycle methods
        # begins below.
        self.__check_or_create_pickle_file_dir__
        self.__get_opeation_value__
        self.__check_existing_instance__
        self.__run__

    @property
    def __check_or_create_pickle_file_dir__(self):
        """
        property used to check if the pickle file
        path exists or not. if it exists
        just pass or create the pickle file
        directory in native OS
        """
        if os.path.exists(self.pickle_file_dir):
            pass
        else:
            os.mkdir(self.pickle_file_dir)

    @property
    def __get_opeation_value__(self):
        """
        property used to get operational value
        it can be size of the parking plot
        or None in case user is checking the status
        """
        if len(self.extra_arguments) != 0:
            self.operation_value = self.extra_arguments[0]
        else:
            self.operation_value = None

    @property
    def __check_existing_instance__(self):
        """
        method used to check if there is already existing
        parkinglot instance if there is not parking_lot
        instance we will create a new instance as a pickle file.
        """
        if os.path.exists(os.path.join(self.pickle_file_dir, 'parking_lot.pickle')):
            self.__load_data_from_pickle__
        else:
            self.manager = None
            self.pickle = None

    @property
    def __dump_data_to_pickle__(self):
        """
        Method used to dump the latest
        class instance state to pickle
        """
        if self.pickle is not None:
            pickle.dump(self.pickle, open(os.path.join(self.pickle_file_dir, 'parking_lot.pickle'), 'wb'), pickle.HIGHEST_PROTOCOL)
        else:
            pickle.dump(self, open(os.path.join(self.pickle_file_dir, 'parking_lot.pickle'), 'wb'), pickle.HIGHEST_PROTOCOL)

    @property
    def __load_data_from_pickle__(self):
        """
        Method used to load the instance
        form pickle which actualy have the
        state information of commandline
        """
        self.pickle = pickle.load(open(os.path.join(self.pickle_file_dir,
                                                    'parking_lot.pickle'),
                                       'rb'))
        self.pickle.command = self.command
        self.pickle.operation_value = self.operation_value

    @property
    def __run_plot_commands__(self):
        """
        Property used to run those command
        which are executed after creating a
        parking lot, Initially there is no
        pickle object available which was used
        to store the parking_lot instance
        """
        if self.command == "park":
            if len(self.extra_arguments) >= 2:
                # if colour is specified with the vehicle
                # registration number
                self.pickle.manager.allot_one_plot(self.operation_value, self.extra_arguments[1])
            else:
                # if colour is not specified with the vehicle
                # registration number
                self.pickle.manager.allot_one_plot(self.operation_value, None)
            self.__dump_data_to_pickle__
        elif self.command == "leave":
            self.manager.clear_one_plot(self.operation_value)
            self.__dump_data_to_pickle__
        elif self.command == "parking_lot_status":
            self.manager.status()
        elif self.command == "registration_numbers_for_cars_with_colour":
            self.manager.get_registration_number_of_vehicle_with_colour(self.operation_value)
        elif self.command == "slot_numbers_for_cars_with_colour":
            self.manager.get_slot_number_for_cars_with_colour(self.operation_value)
        elif self.command == "slot_number_for_registration_number":
            self.manager.get_slot_number_for_registration_number(self.operation_value)
        elif self.command == "quit":
            clear_tmp_file()
        else:
            pass

    @property 
    def __run_plot_commands_on_pickle__(self):
        """
        Property used to run the commands
        specified as postional arguments,
        when there is a already created Parking lot
        """
        if self.command == "park":
            if len(self.extra_arguments) >= 2:
                # if colour is specified with the vehicle
                # registration number
                self.pickle.manager.allot_one_plot(self.operation_value, self.extra_arguments[1])
            else:
                # if colour is not specified with the vehicle
                # registration number
                self.pickle.manager.allot_one_plot(self.operation_value, None)
            self.__dump_data_to_pickle__
        elif self.command == "leave":
            self.pickle.manager.clear_one_plot(self.operation_value)
            self.__dump_data_to_pickle__
        elif self.command == "parking_lot_status":
            self.pickle.manager.status()
        elif self.command == "registration_numbers_for_cars_with_colour":
            self.pickle.manager.get_registration_number_of_vehicle_with_colour(self.operation_value)
        elif self.command == "slot_numbers_for_cars_with_colour":
            self.pickle.manager.get_slot_number_for_cars_with_colour(self.operation_value)
        elif self.command == "slot_number_for_registration_number":
            self.pickle.manager.get_slot_number_for_registration_number(self.operation_value)
        elif self.command == "quit":
            clear_tmp_file()
        else:
            pass

    @property
    def __run__(self):
        """
        Run the commands specified as
        CLI arguments, it will use __run_plot_commands__
        property intensively.
        """
        if self.command == "create_parking_lot":
            clear_tmp_file()
            self.pickle = None
            # we are creating a parknig log manager
            # here which is used to do all the
            # combinotirc operations on parking_plot.
            self.manager = ParkingLotManager(**{'size':int(self.operation_value),
                                                'empty':set(range(1, int(self.operation_value) + 1)),
                                                'consumed':set()})
            self.__dump_data_to_pickle__
        elif self.pickle is not None:
            # if pickle is not None
            # it means we have already creaed
            # a parking_plot and it is stored
            # as a pickle file in tmp directory.
            self.__run_plot_commands_on_pickle__
        else:
            self.__run_plot_commands__

class ParkingLotManager:
    """
    manager class used to do all operation
    on parking plot this class should be used
    along with parking plot.
    """
    def __init__(self, *args, **kwargs):
        self.size = kwargs.get('size')
        self.consumed = kwargs.get('consumed')
        self.empty = kwargs.get('empty')
        self.plot = dict()
        # Lifecycle method begins here
        self.__validate__()


    def __validate__(self):
        """
        Method used to validate the initial
        values supplied to the manager instance
        """
        if self.size < 1:
            raise ValueError("size of parking plot should be grater than 0")
        else:
            pass


    def get_nearest_emtpy(self):
        """
        property_used_get the nearest
        empty lot for parking a new vehicle
        """
        if len(empty) > 0:
            return self.empty[0]
        else:
            raise Exception("overflowed")


    def clear_one_plot(self, plot_index):
        """
        method used to clear on parking plot
        when the car leaves.
        """
        if len(self.consumed) == 0:
            raise Exception("overflow")
        else:
            self.consumed.discard(plot_index)
            self.plot.pop(str(plot_index), None)


    def allot_one_plot(self, registration_number, colour):
        """
        Method used to allot one parking plot
        to the car when it arrives into the parking plot
        """
        if len(self.empty) == self.size:
            self.consumed.add(1)
            self.empty.remove(1)
            self.plot[str(1)] = Vehicle(registration_number, colour)
            print("Alloting parking plot number: 1")
        elif len(self.consumed) == self.size:
            raise Exception("overflowed")
        else:
            nearest_empty_plot = sorted(self.empty)[0]
            self.empty.remove(nearest_empty_plot)
            self.plot[str(nearest_empty_plot)] = Vehicle(registration_number, colour)
            print("Alloting parking plot number: %s" % nearest_empty_plot)

    def get_registration_number_of_vehicle_with_colour(self, colour):
        """
        Method used to find the registration number using the color
        of the vehicle
        """
        print("Registration Number\t colour")
        for key in self.plot.keys():
            if self.plot[key].colour == colour:
                print("%s\t\t\t%s" % (self.plot[key].registration_number, colour))
            else:
                continue


    def get_slot_number_for_cars_with_colour(self, colour):
        """
        method used to get the slot number using the
        vehicle colour
        """
        print("Slot Number\t colour")
        for key in self.plot.keys():
            if self.plot[key].colour == colour:
                print("%s\t\t %s" % (key, colour))
            else:
                continue


    def get_slot_number_for_registration_number(self, registration_number):
        """
        Method used to get the slot number
        of the vehicle with provided registration
        number.
        """
        print("Slot Number\t Colour")
        for key in self.plot.keys():
            if self.plot[key].registration_number == registration_number:
                print("%s\t\t %s" % (key, registration_number))
            else:
                continue


    def status(self):
        """
        Method used to print the representation
        of the Parking plot in tabular form.
        """
        print("slot number\t Registration number\t color")
        for key in self.plot.keys():
            print("%s\t\t%s\t\t\t%s" %(key, self.plot.get(key).registration_number, self.plot.get(key).colour))


class Vehicle:
    """
    class to store the vehicle
    registration number and its
    colour, information
    """
    def __init__(self, registration_number, colour):
        self.colour = colour
        self.registration_number = registration_number
        self.__validate__

    @property
    def __validate__(self):
        """
        Vehicle should atlease have
        registration number
        """
        if self.registration_number is None:
            raise Exception("Registraiton Number is required")
        else:
            pass

    @property
    def representation(self):
        return {'colour': self.colour,
                'registration_number': self.registration_number}


if __name__ == "__main__":
    # defining parser for this file
    # in order to use it using command line
    # arguments
    parser = argparse.ArgumentParser(description="Parkinglot commandline")
    parser.add_argument("command",
                        metavar='Command',
                        type=str,
                        choices=['create_parking_lot', 'park', 'prking_lot_status', 'leave',
                                 'registration_numbers_for_cars_with_colour',
                                 "slot_numbers_for_cars_with_colour",
                                 "slot_number_for_registration_number",
                                 "quit"],
                        help="command to operate parkinglot")
    parser.add_argument('extra_arguments',
                        action='store',
                        nargs=argparse.REMAINDER)
    args = parser.parse_args()

    # initiate parking lot class instance
    parking_lot = ParkingLot(**vars(args))
