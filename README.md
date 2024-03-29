# GOJEK-Parking (Sayak Kundu)
GOJEK Parking Assignment to check OOPS concept.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

> GOJEK-Parking is a linux CLI. More information is present in the docs folder.
# Commands defined by parking_lot package
```sh
create_parking_lot <parking_lot_size>
park <registration_number> <colour>
leave <slot_number>
status
stot_numbers_for_cars_with_colour <colour>
slot_number_for_registration_number <registration_number>
registration_numbers_for_cars_with_colour <colour>
quit
```

## Assumptions made
* We used **quit** instead of **exit** command because the exit command is a default command to exit the terminal.
* **create_parking_lot** command when ran one after the other, keeps adding new slots.
* This project is made for python3 as python2 is going to become obsolete.
* The vehicle colour is case insensitive but the vehicle registration number is not.
* After **quit**, you can't run any other command until and unless you create a parking lot first.


### Installation
> we are making assumption that you have already forked the project and have a clone ready repository setup for you
> for better understanding we are using the default repository clone path.


#### Setup virtual environment for project to run
> inside your the home directory run the following commnads
```sh
$ virtualenv -p python3 parking_plot_env # to create a virtualenv directory named parking_plot_env
$ cd parking_plot_env # to switch to parking_plot_env directory
$ source bin/activate # to activate the virtual environment
$ git clone https://github.com/sayak119/GOJEK-Parking.git
$ cd parking_plot
```

# Building the code
> we are assuming the virtual environment created is activated
> and you are in project root, as left by above commnads
```sh
$ source bin/setup.sh # loads required environment variables and begin build process
```
> building process will create a binary executable at path bin/parking_plot inside project root


### Usage
> Assumption:
- We are assuming that you have sucessfuly build the source code as sepcified above
```sh
$ create_parkinig_lot 5 # to create a parking_lot of size 5.
#[output] creating parking lot with 5 slots

$ park HP55a-3161 # park a car with registration number only.
#[output] Allocated slot number number 1

$ park HP55B-8789 black # park a car with both registration_number and colour.
#[output] Allocated slot number number: 2

$ status # to view status of the parking_lot
#[output]
# sLot number    registaration number  colour
# 1              HP55a-3161            None
# 2              HP55B-8789            black

$ leave 2 # to laeave the lot number 2
#[output]
#slot number 2 is free

$ status
#[output]
# Lot number    registaration number  colour
# 1              HP55a-3161           None

$ park pb58-5858 red # park a new car to the parking_lot
#[output] Allocated slot number number: 2

$ park pb58-5858 red # validation check, only unique registration_number will enter
#[output] ar with this registeration number already exists pb58-5858

$ stot_numbers_for_cars_with_colour red  # to find slot numbers of cars with color red, also search is case insensitive
#[output]
# 2

$ slot_number_for_registration_number pb58-5858 # find slot number for registration number pb58-5858
# [output]
# 2


$ registration_numbers_for_cars_with_colour red # find the registration number of vehicle pared in parking plot with color red
$ # Search is case insensitive
# [output]
# pb58-5858

$ create_parking_lot 2 # creates a parking lot with 2 slots
# [output] creating parking plot with 2 slots

$ create_parking_lot 2 # ammends to the previous empty slots
# [output] creating parking plot with 4 slots


```


### Working with file input
```
$ source bin/setup.sh
$ bin/parking_lot  ./functional_spec/fixtures/file_input.txt

# [output]
#Created a parking lot with 6 slots
#Allocated slot number: 1
#Allocated slot number: 2
#Allocated slot number: 3
#Allocated slot number: 4
#Allocated slot number: 5
#Allocated slot number: 6
#slot number 4 is free
#slot number	 Registration number		 color
#1			KA-01-HH-1234			 White
#2			KA-01-HH-9999			 White
#3			KA-01-BB-0001			 Black
#5			KA-01-HH-2701			 Blue
#6			KA-01-HH-3141			 Black
#Allocated slot number: 4
#Sorry, parking lot is full
#KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333
#1, 2, 4
#6
#Not Found
```


### Check linting
* Used Flake8 for linting as linting is one of the most important part in maintaining large code bases.
```
To check any formatting errors simply run check_linting.sh inside bin directory, this should solve the issues as well.
$ bin/check_linting.sh
# [output] checking for any linting errors
---	Display's any errors that might be there ---
# [output] trying to fix these issues...
# [output] checking again to see if anything was missed
```


### Tests
```
To run the unittests just source the setup.sh inside bin directory
$ source bin/setup.sh
```


### Quit
```
$ quit # this will clear all the pickled files hence removing all entries and any saved data in context to the application
```


### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
