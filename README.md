# Battery State Tracker

## Overview

This repository contains the source code for a web application that tracks a battery's state of charge using an ESP8266 and an Arduino 2650. The website is built using Django, and it receives HTTP POST requests from the ESP8266 to update the battery percentage using JavaScript. Additionally, the application provides functionality to control the battery's outputs automatically based on user-defined thresholds. For example, when the battery drops to a certain percentage, the application sends an HTTP POST request to the ESP8266 to update the current threshold, which triggers actions like cutting the output voltage.

## Technology Stack

- **Django Python:** The web application is built using the Django framework, providing a robust and scalable structure for managing the backend logic.

- **ESP8266:** This microcontroller is used to interface with the battery, sending HTTP POST requests to the Django web application to update the state of charge.

- **Arduino 2650:** Another microcontroller employed to handle specific tasks related to the battery, with scripts written in C++.

## Features

1. **Real-time Battery Tracking:** The website updates the battery's state of charge in real-time based on data received from the ESP8266.

2. **Threshold-based Output Control:** Users can define thresholds for the battery's state of charge. When the battery reaches a specified percentage, the application sends commands to the ESP8266 to perform actions like cutting the output voltage.

3. **User Interface for Threshold Configuration:** The web interface allows users to configure the threshold values easily.

