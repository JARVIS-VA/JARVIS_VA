import ctypes
import datetime
import subprocess
import psutil as psutil
import pyautogui
from Body.Speak import Speak
'''from plyer import notification'''
import os
import cv2
import subprocess


def Shutdown_pc():
    Speak('Shutting Down your pc sir!!')
    os.system("shutdown /s /t 0")
    Shutdown_pc()


def Lock_pc():
    try:
        process_status = Speak("Locking the device")
        ctypes.windll.user32.LockWorkStation()
        return process_status
    except:
        process_error = "Sir !, I am Unable to Lock Your Device"
        return process_error


def battery_per():

    try:
        battery = psutil.sensors_battery()
        percent = battery.percent
        Laptop_per = Speak(f"Sir Laptop Battery is {percent} percent")
        return Laptop_per
    except StopIteration:
        Laptop_error = "You are on Computer without battery"
        return Laptop_error


def Screen_shot():
    screenshot = pyautogui.screenshot()

    img_name = datetime.datetime.now().strftime("%d_%B_%Y_%I_%M_%p")
    img = str(img_name)
    screenshot.save(f"{img}.png")
    return Speak("Screenshot taken Successfully")

def Camera_photo():

    # Create a VideoCapture object to access the camera
    cap = cv2.VideoCapture(0)

    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error opening camera")
        exit()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Camera', frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()



