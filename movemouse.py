# pip install --user pyautogui
import pyautogui
wh = pyautogui.size()
wh
# Size(width=1440, height=900)
wh[0]
# 1440
import pyautogui
for i in range(10):
      pyautogui.moveTo(100, 100, duration=0.25)
      pyautogui.moveTo(200, 100, duration=0.25)
      pyautogui.moveTo(200, 200, duration=0.25)
      pyautogui.moveTo(100, 200, duration=0.25)
