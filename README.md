# Thesis
For z5359838 (Taha Inam) Undergraduate Thesis Project - Omron Mobile Manipulator

## Overview
This repository is used to be able to use ROS2 to interface with the Omron Mobile Manipulator system owned by the UNSW Mechatronics Laboratory (J18 215).

The system consists of the following core components
- Omron TM12-S
    - The Cobot 6 degree of freedom robot arm
- Omron LD250 AMR
    - The differential drive robot base
- Omron PLC
    - The controller used to interface between the TM12-S and LD250
- Robotiq 2F140 Gripper
    - The gripper attached to the TM12-S

This repository is intended to be used on a machine installed with ROS2 Humble and MoveIt. The respective installation pages can be referenced.

Need to add thorough information about installation since I changed some source packages

## Network Topology

Outline the ip addresses and subnets

reference the config package section. The ip addresses must be set in the config package...

## System Overview
The control of the TM12-S and AMR250 using ROS2 is achieved in a very similar way. Each robot uses its own command language for control, the TM Expression Editor for the TM12-S, and the [Advanced Robotics Command Language (ARCL)](#advanced-robotics-command-language-arcl) for the AMR250. These are exploited by ROS2 "interface" nodes that monitor published messages/services/actions that build and send command strings to the respective robots, and vice versa for feedback. ROS2 "control" nodes then use RViz2 windows to visually monitor and manipulate the robots based on the state of the various ROS2 interfaces.

Using a 



Describe how we have the interface package, and then the visualisation/control package.

Describe how the system can be used. (with one computer, with two, wireless/wired etc)

## Packages Overview
Many packages in this repository are based on source filed obtained from [Omron APAC Github Repo](https://github.com/OmronAPAC/Omron_AMR_ROS2) and [Techman Robotic Inc Github Repo](https://github.com/TechmanRobotInc/tmr_ros2). Some changes have been made to suit the specific use in the UNSW MoMa system.

Contributions and discussions from Wiechen Tie, David Nie and Wong Chung Fong accelerated significant progress in building aspects in this repository. Big thanks!

Packages prefixed with 'amr' and 'tm' are used exclusively for their respective robot systems. Packages prefixed with moma are used for both. 

### Config Packages
The config package 'shared_config' contains one file of interest, 'config/ip_settings.py'. This file contains the IP addresses to be used by the respective interfaces. The AMR and TM IP addresses should not be changed, as these are the default as configured on the UNSW MoMa system.
The server and client IP addresses must match the interfaces used by the respective machines.

### AMR-ROS2 Overview
#### Advanced Robotics Command Language (ARCL)

#### Interface Packages
To interface with the AMR, the launch file 'amr_util/launch/server.launch.py' is used to translate ROS2 interfaces (messages, services and actions) to ARCL commands. It can be called from the command line using:
```
ros2 launch amr_util server.launch.py 
```
The launch file runs three nodes, which can be run manually (in this order) in seperate terminals using:
```
ros2 run amr_util arcl_api_server --ros-args -p ip_address:=[amr ip address] -p port:=7171 -p def_arcl_passwd:=omron
```
```
ros2 run amr_util ld_states_publisher --ros-args -p local_ip:=[local interface ip address] -p local_port:=7179
```
```
ros2 run amr_navigation action_server --ros-args -p ip_address:=[amr ip address] -p port:=7171 -p def_arcl_passwd:=omron
```
Describe what each node does (make sure all files are described)

#### Control Packages
To control the LD250, the launch file 'amr_visualisation/launch/display.launch.py' is used to open an RViz2 screen that shows the main Lidar Scans, the 

### TM-ROS2 Overview
