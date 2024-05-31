#!/usr/bin/env python3
import socket
from ev3dev.ev3 import Motor
from ev3dev2.button import Button
import subprocess
from time import sleep
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor
import time
from ev3dev2.motor import Motor, OUTPUT_B, OUTPUT_D, SpeedPercent, MoveSteering
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.button import Button


# Initialize the motors and buttons
motorD = Motor(OUTPUT_D)
motorB = Motor(OUTPUT_B)
btn = Button()
gyro = GyroSensor(INPUT_3)
ultrasonic_side = UltrasonicSensor(INPUT_2)
ultrasonic_front = UltrasonicSensor(INPUT_1)

ultrasonic_front.mode = 'US-DIST-CM'
ultrasonic_side.mode = 'US-DIST-CM'

def get_distance_front():
    return ultrasonic_front.distance_centimeters

def get_distance_side():
    return ultrasonic_side.distance_centimeters

# Function to perform a gyro-based turn to the right by 90 degrees
def turn_right_90():
    sleep(1)
    initial_angle = gyro.angle
    while True:
        motorD.run_forever(speed_sp=-1500)
        motorB.run_forever(speed_sp=-1500)
        while gyro.angle < initial_angle + 50:
            print("Current Angle: ", gyro.angle)  # Debugging statement
            sleep(0.1)
        motorB.stop()
        motorD.stop()
        motorB.run_timed(speed_sp=200, time_sp=450)
        sleep(1.5)
        motorD.run_timed(speed_sp=-1500, time_sp=2000)
        print("Final Gyro Angle after Right Turn: ", gyro.angle)
        sleep(1)
        break

# Function to perform a gyro-based turn to the left by 90 degrees
def turn_left_90():
    motorD.on_for_seconds(SpeedPercent(-50), 1, block=True)
    initial_angle = gyro.angle
    while True:
        motorD.run_forever(speed_sp=-1500)
        motorB.run_forever(speed_sp=1500)
        while gyro.angle > initial_angle - 50:
            print("Current Angle: ", gyro.angle)  # Debugging statement
            sleep(0.1)
        motorB.stop()
        motorD.stop()
        sleep(1)
        motorB.run_timed(speed_sp=-250, time_sp=320)
        sleep(1.5)
        motorD.run_timed(speed_sp=-1000, time_sp=800)
        break
            

def setup_network():
    password = 'maker'
    ip_command = "sudo ip addr add 192.168.42.3/24 dev usb0"
    link_command = "sudo ip link set usb0 up"

    # Commands to be executed with sudo
    commands = [ip_command, link_command]

    for cmd in commands:
        # Construct the command using concatenation
        command = 'echo ' + password + ' | sudo -S ' + cmd
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print("Error executing {}: {}".format(cmd, stderr.decode().strip()))
        else:
            print("Executed {} successfully".format(cmd))

def wait_for_button_press():
    print("Waiting for button press to start the server...")
    while True:
        if btn.any():
            print("Button pressed, starting server...")
            break
        sleep(0.1)  # Check every 100 ms

def main():
    # Setup network first
    setup_network()

    # Wait for button press to start receiving messages
    wait_for_button_press()

    host = ''  # Empty string means the server will listen on all available interfaces
    port = 10000  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the address and port
        server_socket.bind((host, port))

        # Listen for incoming connections
        server_socket.listen(1)
        print("Server is listening on port {}".format(port))

        connection, client_address = server_socket.accept()
        with connection:
            print("Connected by", client_address)
            while True:
                motorD.run_forever(speed_sp=-750)
                data = connection.recv(1024)
                if not data:
                    break
                side_distance = get_distance_side()
                if side_distance < 23:
                    motorD.stop()
                    motorB.on_for_degrees(SpeedPercent(50), 22)  # Adjust degrees for sharper turn
                    motorD.on_for_seconds(SpeedPercent(-50), 1, block=True)
                    motorD.stop()
                    motorB.on_for_degrees(SpeedPercent(50), -24)
                    print("side works")
                command = data.decode()
                print("Received: " + command)
                if command == 'Orange':
                    pass
                elif command == 'Blue':
                    while True:
                        turns = 0
                        motorD.run_forever(speed_sp=-1000)
                        front_distance =get_distance_front()
                        if front_distance < 30:
                            
                            # Stop, turn right sharply, then move forward
                            motorD.stop()
                            motorD.on_for_seconds(SpeedPercent(100), 0.7, block=True)
                            motorD.stop()
                            initial_angle = gyro.angle
                            motorB.on_for_degrees(SpeedPercent(10), 28)  # Adjust degrees for sharper turn
                            motorB.stop()
                            motorD.run_forever(speed_sp=-1050)
                            while gyro.angle > initial_angle - 76:
                                sleep(0.1)
                            motorD.stop()
                            motorB.on_for_degrees(SpeedPercent(50), -30)
                            motorB.stop()
                            motorD.on_for_seconds(SpeedPercent(-50), 1, block=True)
                            turns+=1
                            if(turns==12):
                                exit()
                        side_distance = get_distance_side()
                        if side_distance < 20:
                            motorD.stop()
                            motorD.on_for_seconds(SpeedPercent(50), 1, block=True)
                            motorD.stop()
                            motorB.on_for_degrees(SpeedPercent(50), 28)  # Adjust degrees for sharper turn
                            motorD.on_for_seconds(SpeedPercent(-50), 1, block=True)
                            motorB.on_for_degrees(SpeedPercent(50), -27.5)
                            motorD.on_for_seconds(SpeedPercent(-50), 1, block=True)
                            motorB.stop() 


                elif command == 'No':
                    motorD.run_forever(speed_sp=-750)
                
                        

if __name__ == "__main__":
    main()

