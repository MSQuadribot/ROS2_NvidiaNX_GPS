#### ROS2 GPS Package for the Nvidia NX Xavier

This package's goal is to use a G-STAR-IV GPS provided with the nvidia NX Xavier in a ROS2 environment

### How to build the package :

First, open a new terminal and go to the following directory : /Desktop/dev_ws
There you will be able to build all the packages that are in the src subdirectory

$ colcon build

This process can take some times (on my machine it could take up to 15s to run)
Remember that if the built was already completed, there is no need to run it again
But, be also aware that you have to rebuild the package each time you make a modification

### How to run the package :

For that, you will need to open a new terminal and go to the following directory : /Desktop/dev_ws
If you just built the package, the terminal will need to be different as this can cause issues otherwise

in order to launch a process for this package you will need to source your workspace

$ . install/setup.bash

Once done, you can process with using this wonderful package

$ ros2 run gps {$processname}

### What are the available process ?

There are currently five available process :

talker will provide the information directly from the gps.
The frequency is quite low (5.5s) due to the fact that the information are emitted with a specific pattern

listened is set to get the data from the publisher.

### Important note

In most Ubuntu devices, normal users will not be able to natively access devices.
As the gps is locates in /dev/ttyUSB0 on the Nvidia Nx Xavier, before using the ROS2 package, the user must be certified as sudo.