import cv2
import numpy as np
import socket
import time

def detect_color(img, color_range):
    mask = cv2.inRange(img, color_range[0], color_range[1])
    return mask.any()

def main():
    host = '192.168.42.3'  # The IP address of the EV3
    port = 10000  # The port number where the EV3 server is listening

    # Define more precise range of blue and orange colors in HSV
    blue_range = ([np.array([100, 100, 50]), np.array([128, 255, 255])])
    orange_range = ([np.array([10, 150, 100]), np.array([18, 255, 255])])

    cap = cv2.VideoCapture(0)
    last_print_time = time.time()

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                print("Connecting to {} on port {}".format(host, port))
                sock.connect((host, port))
                print("Connected to server")

                while True:
                    ret, img = cap.read()
                    if not ret:
                        continue

                    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                    blue_detected = detect_color(hsv, blue_range)
                    orange_detected = detect_color(hsv, orange_range)

                    current_time = time.time()
                    if current_time - last_print_time >= 1:
                        message = "No"
                        if blue_detected:
                            message = "Blue"
                        elif orange_detected:
                            message = "Orange"

                        print(message)
                        sock.sendall(message.encode())
                        last_print_time = current_time
                    time.sleep(0.25)
        except Exception as e:
            print(f"An error occurred: {e}. Retrying in 5 seconds...")
            time.sleep(5)  # Wait before trying to reconnect

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()