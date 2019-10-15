#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import pickle
import argparse
import shlex
import sys
from functional_spec.spec.setup import clear_tmp_file


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
            pickle.dump(self.pickle, open(os.path.join(self.pickle_file_dir,
                                                       'parking_lot.pickle'), 'wb'),
                        pickle.HIGHEST_PROTOCOL)
        else:
            pickle.dump(self, open(os.path.join(self.pickle_file_dir,
                                                'parking_lot.pickle'), 'wb'),
                        pickle.HIGHEST_PROTOCOL)

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
    def __check_manager_existance__(self):
        """
        check if manager object exists for
        self otherwise through an error and
        halt the execution
        """
        if self.manager is not None:
            pass
        else:
            print("No parkinglot exists,  Please create a parking lot first")
            sys.exit()

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
            self.__check_manager_existance__
            if len(self.extra_arguments) >= 2:
                # if colour is specified with the vehicle
                # registration number
                self.pickle.manager.allot_one_plot(
                    self.operation_value, self.extra_arguments[1])
            else:
                # if colour is not specified with the vehicle
                # registration number
                self.pickle.manager.allot_one_plot(self.operation_value, None)
            self.__dump_data_to_pickle__
        elif self.command == "leave":
            self.__check_manager_existance__
            self.manager.clear_one_plot(self.operation_value)
            self.__dump_data_to_pickle__
        elif self.command == "status":
            self.__check_manager_existance__
            self.manager.status()
        elif self.command == "registration_numbers_for_cars_with_colour":
            self.__check_manager_existance__
            self.manager.get_registration_number_of_vehicle_with_colour(
                self.operation_value)
        elif self.command == "slot_numbers_for_cars_with_colour":
            self.__check_manager_existance__
            self.manager.get_slot_number_for_cars_with_colour(
                self.operation_value)
        elif self.command == "slot_number_for_registration_number":
            self.__check_manager_existance__
            self.manager.get_slot_number_for_registration_number(
                self.operation_value)
        elif self.command == "exit":
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
                self.pickle.manager.allot_one_plot(
                    self.operation_value, self.extra_arguments[1])
            else:
                # if colour is not specified with the vehicle
                # registration number
                self.pickle.manager.allot_one_plot(self.operation_value, None)
            self.__dump_data_to_pickle__
        elif self.command == "leave":
            self.pickle.manager.clear_one_plot(self.operation_value)
            self.__dump_data_to_pickle__
        elif self.command == "status":
            self.pickle.manager.status()
        elif self.command == "registration_numbers_for_cars_with_colour":
            self.pickle.manager.get_registration_number_of_vehicle_with_colour(
                self.operation_value)
        elif self.command == "slot_numbers_for_cars_with_colour":
            self.pickle.manager.get_slot_number_for_cars_with_colour(
                self.operation_value)
        elif self.command == "slot_number_for_registration_number":
            self.pickle.manager.get_slot_number_for_registration_number(
                self.operation_value)
        elif self.command == "exit":
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
            # we are creating a parknig log manager
            # here which is used to do all the
            # combinotirc operations on parking_plot.
            if self.pickle:
                self.pickle.manager.empty = self.pickle.manager.empty.union(set([x for x in range(
                    self.pickle.manager.size + 1, self.pickle.manager.size + 1 + self.operation_value)]))  # NOQA
                self.pickle.manager.size = self.pickle.manager.size + int(self.operation_value)
                print("Created a parking lot with %s slots" %
                      len(self.pickle.manager.empty))
                self.__dump_data_to_pickle__
            else:
                self.pikcle = None
                self.manager = ParkingLotManager(**{'size': int(self.operation_value),
                                                    'empty': set(range(1,
                                                                       int(self.operation_value) + 1)),  # NOQA
                                                    'consumed': set()})  # NOQA
                print("Created a parking lot with %s slots" %
                      (int(self.operation_value)))
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
            print("size of parking plot should be grater than 0")
            sys.exit()
        else:
            pass

    def __validate_unique_check__(self, registration_number, colour):
        registration_numbers = list()
        for key in sorted(self.plot.keys()):
            if self.plot[key].registration_number == registration_number:
                registration_numbers.append(self.plot[key].registration_number)
            else:
                continue
        if len(registration_numbers) > 0:
            print("Car with this registeration number already exists %s " %
                  registration_numbers[0], sep=", ")
            return 0
        else:
            return 1

    def get_nearest_emtpy(self):
        """
        property_used_get the nearest
        empty lot for parking a new vehicle
        """
        if len(self.empty) > 0:
            return sorted(self.empty)[0]
        else:
            print("Parking lot is already empty")

    def clear_one_plot(self, plot_index):
        """
        method used to clear on parking plot
        when the car leaves.
        """
        if len(self.consumed) == 0:
            print("Parking lot is already empty")
        else:
            try:
                self.consumed.remove(int(plot_index))
            except KeyError:
                print("lot number %s doesn't exist" % plot_index)
                sys.exit()
            self.empty.add(int(plot_index))
            self.plot.pop(str(plot_index), None)
            print("slot number %s is free" % plot_index)

    def allot_one_plot(self, registration_number, colour):
        """
        Method used to allot one parking plot
        to the car when it arrives into the parking plot
        """
        if self.__validate_unique_check__(registration_number, colour):
            if len(self.empty) == self.size:
                self.consumed.add(1)
                self.empty.remove(1)
                self.plot[str(1)] = Vehicle(registration_number, colour)
                print("Allocated slot number: 1")
            elif len(self.consumed) == self.size:
                print("Sorry, parking lot is full")
            else:
                nearest_empty_plot = sorted(self.empty)[0]
                self.empty.remove(nearest_empty_plot)
                self.consumed.add(nearest_empty_plot)
                self.plot[str(nearest_empty_plot)] = Vehicle(
                    registration_number, colour)
                print("Allocated slot number: %s" % nearest_empty_plot)
        else:
            pass

    def get_registration_number_of_vehicle_with_colour(self, colour):
        """
        Method used to find the registration number using the color
        of the vehicle
        """
        registration_numbers = list()
        for key in sorted(self.plot.keys()):
            if self.plot[key].colour.lower() == colour.lower():
                registration_numbers.append(self.plot[key].registration_number)
            else:
                continue
        if len(registration_numbers) > 0:
            print(*registration_numbers, sep=", ")
        else:
            print("Not found")

    def get_slot_number_for_cars_with_colour(self, colour):
        """
        method used to get the slot number using the
        vehicle colour
        """
        slot_number_list = list()
        for key in self.plot.keys():
            if self.plot[key].colour.lower() == colour.lower():
                slot_number_list.append(key)
            else:
                continue
        if len(slot_number_list) > 0:
            print(*slot_number_list, sep=", ")
        else:
            print("Not Found")

    def get_slot_number_for_registration_number(self, registration_number):
        """
        Method used to get the slot number
        of the vehicle with provided registration
        number.
        """
        for key in self.plot.keys():
            if self.plot[key].registration_number == registration_number:
                print(key)
                break
            else:
                continue
        else:
            print("Not Found")

    def status(self):
        """
        Method used to print the representation
        of the Parking plot in tabular form.
        """
        print("slot number\t Registration number\t\t color")
        for key in sorted(self.plot.keys()):
            print("%s\t\t\t%s\t\t\t %s" % (key, self.plot.get(
                key).registration_number, self.plot.get(key).colour))


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
            print("Registraiton Number is required")
            sys.exit()
        else:
            pass

    @property
    def representation(self):
        return {'colour': self.colour,
                'registration_number': self.registration_number}


class CommandFileParser:
    """
    class used used to parse
    parking_lot command file.
    and validate it before execution
    """

    def __init__(self, file_path, *args, **kwargs):
        self.file_path = file_path

        # lifecycle method begins
        self.__validate_path__
        self.__validate_file_type__
        self.__setup_argument_parser__
        self.__exec_file_commands__

    @property
    def __validate_path__(self):
        """
        check if a file exists at the file path
        otherwise raise a warning.
        """
        if os.path.exists(self.file_path):
            pass
        else:
            print("Error: No file Exists at path %s" % self.file_path)
            sys.exit()

    @property
    def __validate_file_type__(self):
        """
        Validate file of type
        .txt is only allowed as input_file
        """
        if self.file_path.split('.')[-1] == 'txt':
            pass
        else:
            print("Error: file extension is not .txt")
            sys.exit()

    @property
    def __setup_argument_parser__(self):
        """
        property used to create a argument parser
        which will be used to parse each line in the file
        into an array of command line arguments.
        """
        self.parser = argparse.ArgumentParser(
            description="Parkinglot commandline")
        self.parser.add_argument("command",
                                 metavar='Command',
                                 type=str,
                                 choices=['create_parking_lot',
                                          'park',
                                          'status',
                                          'leave',
                                          'registration_numbers_for_cars_with_colour',
                                          "slot_numbers_for_cars_with_colour",
                                          "slot_number_for_registration_number",
                                          "exit"],
                                 help="command to operate parkinglot")
        self.parser.add_argument('extra_arguments',
                                 action='store',
                                 nargs=argparse.REMAINDER)

    @property
    def __exec_file_commands__(self):
        """
        property used to read the
        the file containing the commnads
        """
        with open(self.file_path, 'r') as command_file:
            for line in command_file:
                args = self.parser.parse_args(shlex.split(line))
                ParkingLot(**vars(args))
            clear_tmp_file()


if __name__ == "__main__":
    """
    when this module is run
    as a standlone file. It can accept
    a file
    """
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(
            description="parking_lot command line used to accept file_path as Input")
        parser.add_argument("file_path",
                            metavar="file_path",
                            type=str,
                            help="file of parking lot command file, Input file should be in .txt format with valid commands seperated by \n")  # NOQA
        args = parser.parse_args()
        CommandFileParser(**vars(args))
    else:
        clear_tmp_file
