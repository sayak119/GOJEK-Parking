#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import pickle
import argparse
from setup import clear_tmp_file
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
        self.pickle_file_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tmp')
        # parkining_lot class lifecycle methods
        # begins below.
        self.__get_opeation_value__
        self.__check_existing_instance__
        self.run

    @property
    def __get_opeation_value__(self):
        """
        get operational value
        it can be size of the parking plot
        or None in case of status
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
        print("lifecycle method one")
        if os.path.exists(os.path.join(self.pickle_file_dir, 'parking_lot.pickle')):
            print("pickle file exists")
            self.load_data_from_pickle()
        else:
            print("No pickle file exists")
            self.manager = None
            self.pickle = None


    def __del__(self):
        pass


    def dump_data_to_pickle(self):
        """
        Method used to dump the latest
        class instance state to pickle
        """
        print("dumping pickle data")
        if self.pickle is not None:
            pickle.dump(self.pickle, open(os.path.join(self.pickle_file_dir, 'parking_lot.pickle'), 'wb'), pickle.HIGHEST_PROTOCOL)
        else:
            pickle.dump(self, open(os.path.join(self.pickle_file_dir, 'parking_lot.pickle'), 'wb'), pickle.HIGHEST_PROTOCOL)

    def load_data_from_pickle(self):
        """
        Method used to load the instance
        form pickle which actualy have the
        state information of commandline
        """
        print("loading pickle data")
        self.pickle = pickle.load(open(os.path.join(self.pickle_file_dir,
                                                    'parking_lot.pickle'),
                                       'rb'))
        self.pickle.command = self.command
        self.pickle.operation_value = self.operation_value

    @property
    def run(self):
        """
        Run command specified
        """
        if self.pickle is not None:
            # producing command output
            if self.command == "park":
                self.pickle.manager.allot_one_plot(self.operation_value)
                self.dump_data_to_pickle()
            elif self.command == "leave":
                self.pickle.manager.clear_one_plot(self.operation_value)
                self.dump_data_to_pickle()
            elif self.command == "status":
                self.pickle.manager.status()
            elif self.command == "exit":
                clear_tmp_file()
            else:
                print("command not found")
        else:
            if self.command == "create_parking_plot":
                print("creating parking plot manager")
                self.manager = ParkingLotManager(**{'size':int(self.operation_value),
                                                    'empty':set(range(1, int(self.operation_value) + 1)),
                                                    'consumed':set()})
                self.dump_data_to_pickle()
            else:
                raise Exception("there is no parking plot available")

            # prducing command output
            if self.command == "park":
                self.manager.allot_one_plot(self.operation_value)
                self.dump_data_to_pickle()
            elif self.command == "leave":
                self.manager.clear_one_plot(self.operation_value)
                self.dump_data_to_pickle()
            elif self.command == "status":
                self.manager.status()
            elif self.command == "exit":
                clear_tmp_file()
                sys.exit()
            else:
                print("command not found")


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
        print("size : %s \n consumed: %s \n empty: %s" % (self.size,
                                                          self.consumed,
                                                          self.empty))

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
        if len(empty) > 0:
            return self.empty[0]
        else:
            raise Exception("overflowed ")

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

    def allot_one_plot(self, car):
        """
        Method used to allot one parking plot
        to the car when it arrives into the parking plot
        """
        if len(self.empty) == self.size:
            self.consumed.add(1)
            self.empty.remove(1)
            self.plot[str(1)] = car
        elif len(self.consumed) == self.size:
            raise Exception("overflowed")
        else:
            nearest_empty_plot = sorted(self.empty)[0]
            self.empty.remove(nearest_empty_plot)
            self.plot[str(nearest_empty_plot)] = car
            print("Alloting parking plot number: %s" % nearest_empty_plot)

    def status(self):
        print("slot number \t Registration number \t color")
        for key in self.plot:
            print("%s \t \t %s" %(key, self.plot.get(key)))
            

if __name__ == "__main__":
    # defining parser for this file
    # in order to use it using command line
    # arguments
    parser = argparse.ArgumentParser(description="Parkinglot commandline")
    parser.add_argument("command",
                        metavar='Command',
                        type=str,
                        help="command to operate parkinglot")
    parser.add_argument('extra_arguments',
                        action='store',
                        nargs=argparse.REMAINDER)
    args = parser.parse_args()
    print(vars(args))
    print(type(vars(args)))

    # initiate parking lot class instance
    parking_lot = ParkingLot(**vars(args))
