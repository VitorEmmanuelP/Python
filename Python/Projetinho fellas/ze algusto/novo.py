import time

import pyautogui
time.sleep(2)
for i in range(0,10000):
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.hotkey('enter')
