import pyautogui
import time

# Set initial coordinates
x = 200
y = 200

# Move the mouse to the starting position
pyautogui.moveTo(x, y)

# Draw the car body
pyautogui.drag(100, 0, duration=0.2, button='left')  # Draw the top side of the car body
pyautogui.drag(0, 20, duration=0.2, button='left')  # Draw the rear side of the car body
pyautogui.drag(-100, 0, duration=0.2, button='left')  # Draw the bottom side of the car body
pyautogui.drag(0, -20, duration=0.2, button='left')  # Complete the car body

# Draw the car wheels
pyautogui.moveTo(x + 20, y + 20)
pyautogui.drag(20, 0, duration=0.2, button='left')  # Draw the front wheel
pyautogui.moveTo(x + 80, y + 20)
pyautogui.drag(20, 0, duration=0.2, button='left')  # Draw the rear wheel

# Move the mouse away
pyautogui.moveTo(0, 0)

# Give some time to observe the drawing
time.sleep(3)
