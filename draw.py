import pyautogui
import time

time.sleep(5)
pyautogui.click()  # Click to make the window active.

distance = 300
change = 20

while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2, button='left')  # Move right.
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2, button='left')  # Move down.
    pyautogui.drag(-distance, 0, duration=0.2, button='left')  # Move left.
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2, button='left')  # Move up.
