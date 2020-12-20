# UDistance
#### Alternate Title: Code Tracker
#### Made for [HackUMass 2020](www.hackumass.com)

UDistance is an App helping you find safe campus spots to study by tracking the real-time population density in campus buildings by having a hardware system of sensors, and a database that puts the hardware and the App together.

Made using:
* SwiftUI
* Firebase Realtime Database
* Radar.io
* Arduino UNO R3
* Python

## Inspiration

Due to the coronavirus pandemic, many students, like ourselves, are struggling due to living environments that are not conducive to learning. Finally, as we all slowly return to college campuses, it is important that we use college facilities as safe as possible. It is crucial that we stay safe, yet still attain the best college experience. To this end, we made UDistance.

## How it Works

We developed a prototype for the hardware system, which would eventually be deployed into a network that monitors building entrances on campus, where we used smart sensors to identify a person entering or exiting. This system, built using Arduino, was connected to our backend database built using Google Cloud's Firebase platform.

Furthermore, we developed an iOS app using SwiftUI and Xcode which displayed a list of buildings and crowd calculations using data from the hardware (via the Firebase API). We also used Radar.io to develop geofencing for each college campus building, which is used to inform users when they enter a crowded (and thereby, dangerous) building.

## Usage

Download the project and use the .xcworkspace file to open using Xcode. The hardware folder contains implementation of the Arduino + Python code, where we used PySerial to send data to the Python program which updated the Firebase RTDB.

## Credits

Dhruv Vikram Krishna, Heta Shah & Ananya Rao

## License
[MIT](https://choosealicense.com/licenses/mit/)

