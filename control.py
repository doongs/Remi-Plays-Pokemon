import keyboard
import time

keyboard.wait('esc')

keyboard.press('up')
time.sleep(2)
print("Release Up")
keyboard.release('up')
time.sleep(2)

keyboard.press('F12')
time.sleep(2)
print("Release F12")
keyboard.release('F12')
time.sleep(2)
