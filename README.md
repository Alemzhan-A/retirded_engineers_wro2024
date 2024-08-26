# WRO Future Engineers - Team [Your Team Name]

## Table of Contents
1. [Introduction](#introduction)
2. [Robot Design](#robot-design)
   - [Mobility Management](#mobility-management)
   - [Power and Sensing Management](#power-and-sensing-management)
   - [Obstacle Management](#obstacle-management)
3. [Technical Specifications](#technical-specifications)
4. [Software](#software)
5. [Photos and Video](#photos-and-video)
6. [Team Information](#team-information)

## Introduction

Welcome to our WRO Future Engineers project repository! This README provides comprehensive information about our robot design, features, and development process for the 2024 World Robot Olympiad Future Engineers category.

## Robot Design

### Mobility Management

- **Drive System**: Rear-wheel drive powered by two LEGO medium motors
- **Wheel Specifications**: 31mm radius wheels
- **Gear Configuration**: 
  - Two large gears (one per motor) connected by a small gear
  - Additional large gear attached to the small gear, connecting to a differential
- **Differential**: Installed on rear wheels
- **Steering**: Horizontally mounted medium motor controlling the front axle

**Design Rationale:**
- LEGO components for ease of assembly and modification
- Motors with similar manufacturing origins for synchronized operation
- EV3 brick mounted sideways for convenient battery replacement

**Dimensions**: 268mm (length) x 166mm (width) x 204mm (height)

### Power and Sensing Management

- **Power Source**: LEGO EV3 Intelligent Brick with rechargeable lithium-ion battery

**Sensor Suite:**

1. **LEGO Color Sensor**
   - Purpose: Detection of orange and blue field markings
   - Location: front

2. **Pixy2 Camera**
   - Purpose: Identification of red and green objects
   - Location: top-front

3. **LEGO Gyro Sensor**
   - Purpose: Precise rotational control and orientation tracking
   - Location: back-top

### Obstacle Management

[Your obstacle management strategy details]

## Technical Specifications

- **Processor**: LEGO EV3 Intelligent Brick
- **Motors**: 
  - 2x LEGO Medium Motors (Rear drive)
  - 1x LEGO Medium Motor (Front steering)
- **Sensors**:
  - 1x LEGO Color Sensor
  - 1x Pixy2 Camera
  - 1x LEGO Gyro Sensor
- **Power Source**: Rechargeable lithium-ion battery (EV3 brick)
- **Programming Language**: Basic(Clev3r)

## Software

[Software architecture overview]

```python
# Example code snippet
def detect_field_markings():
    # Code for detecting field markings
    pass

def identify_objects():
    # Code for identifying objects
    pass
```

## Photos and Video

### Team Photos
Team photos are in the `t-photos` folder.

<details>
<summary>Click to view team photo</summary>

![Team Photo](t-photos/team_photo.jpg)
*Caption: [Your Team Name] at [Event/Location]*

</details>

### Vehicle Photos
Robot photos are in the `v-photos` folder.

<details>
<summary>Click to view robot photos</summary>

![Robot Front View](v-photos/robot_front.jpeg)
*Front view of our robot*

![Robot Side View](v-photos/robot_right.jpeg)
*Side view showcasing the drive system*

![Robot Top View](v-photos/robot_top.jpeg)
*Top view highlighting sensor placement*

</details>

### Video Demonstration

[![Robot Demo Video](https://youtu.be/v8r7JQF2mQA?si=ztm9AK12ajWzkM_R)]

## Team Information

- **Team Name**: Retired Engineers
- **Country/Region**: Kazakhstan, Semey
- **Members**:
  - Akhmetzhanov Alemzhan
  - Serikgali Daulet
