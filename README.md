# Smart Guard 

## Overview
**Smart Guard** is an intelligent mobile robot designed to automatically detect and extinguish indoor fires. This project integrates software and hardware to provide a fast, autonomous, and reliable response to fire hazards in enclosed environments.

## Technologies & Tools 
* **Operating System:** Ubuntu Linux
* **Robotics Framework:** ROS2 (Robot Operating System 2)
* **Hardware Controller:** Arduino
* **Robot Modeling:** URDF (Unified Robot Description Format)

## Core Concepts Implemented 
* **ROS2 Nodes & Topics:** Used for seamless communication between sensors, the main processing unit, and the actuators.
* **ROS2 Services:** Handled specific request-response actions, such as triggering the fire extinguishing mechanism.
* **URDF Modeling:** Designed the physical layout and kinematics of the robot for simulation and visualization.
* **Hardware Integration:** Used Arduino to bridge the ROS2 system with physical components (motors, fire sensors, and the extinguisher).

## How It Works 
1. The robot navigates the indoor environment continuously.
2. Sensors read the surroundings and send data through **ROS2 Topics**.
3. Once a fire is detected, a **ROS2 Node** processes the exact location.
4. The system commands the Arduino to move towards the target and activate the extinguisher.

## Setup and Prerequisites 
To run this project, you need:
- Ubuntu Linux installed on your machine.
- ROS2 installed and configured.
- Arduino IDE for uploading the hardware code.

## Future Improvements 🚀
- Adding Machine Learning algorithms for better obstacle avoidance.
- Integrating a mobile app alert system for remote monitoring.
