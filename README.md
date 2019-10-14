# GOJEK-Parking
GOJEK Parking Assignment to check OOPS concept

> Parking_lot is a linux CLU, used to create a test the parking lot funcationality.
# commands defined by parking_lot package
```sh
create_parking_lot <parking_lot_size>
park <registration_number> [colour]
leave
parking_lot_status
stot_numbers_for_cars_with_colour
slot_number_for_registration_number
registration_numbers_for_cars_with_colour
```
# Note: updates in commands!

  - 'status' comman has been updted with 'parking_lot_status'
  - 'exit' command has been updated with 'quit' command


#### Reason for update:
  > 'status' and 'exit' command conflicted with already existing Linux CLI, as 'exit' is used to get rid of current shell session
  > 'status' is used with GIT to find the status for current working branch


### Installation
> we are making assumption that you have already forked the project and have a clone ready repository setup for you
> for better understanding we are using the default repository clone path.

#### setup virtual environment for project to run
> inside your the home directory run the following commnads
```sh
$ virtualenv -p python3 parking_plot_env # to create a virtualenv directory named parking_plot_env
$ cd parking_plot_env # to switch to parking_plot_env directory
$ source bin/activate # to activate the virtual environment
$ git clone https://nareshkumarjaggi@bitbucket.org/nareshkumarjaggi/parking_lot.git
$ cd parking_plot
```

# building the code
> we are assuming the virtual environment created is acrtivated
> and you are in project root, as left by above commnads
```sh
$ source bin/setup.sh # loads required environment variables and begin build process 
```
> building process will create a binary executable at path bin/parking_plot inside project root


### usage
> Assumption: 
- We are assuming that you have sucessfuly build the source code as sepcified above
```sh
$ create_parkinig_lot 5 # to create a parking_lot of size 5.

$ park HP55a-3161 # park a car with registration number only.
#[output] Alloting parking plot number 1

$ park HP55B-8789 black # park a car with both registration_number and colour.
#[output] Alloting parking plot number 2

$ parking_lot_status # to view status of the parking_lot
#[output]
# sLot number    registaration number  colour
# 1              HP55a-3161            None 
# 2              HP55B-8789            black

$ leave 2 # to laeave the lot number 2
$ parking_lot_status
#[output]
# Lot number    registaration number  colour
# 1              HP55a-3161           None

$ park pb58-5858 red # park a new car to the parking_lot
#[output] Alloting parking plot number 2

$ stot_numbers_for_cars_with_colour red  # to find slot numbers of cars with color red
#[output]
# slot number   colour
# 2             red

$ slot_number_for_registration_number pb58-5858 # find slot number for registration number pb58-5858
# [output]
# slot number          Resitration number
# 2                    pb58-5858


$ registration_numbers_for_cars_with_colour red # find the registration number of vehicle pared in parking plot with color red
# [output]
# Registration number       colour
# pb58-5858                 black


```
### License
 > MIT, Licence is subject to client's specification and requirements, clients have complete right to update the licence once product is delivered to them completely.
 > before project completion we will use the same licence as mentioned here.
