import keyboard
import time

keyboard.wait('esc')
f = open("input.txt", "r")
input = f.read()
print(input)

keyboard.press(input)
time.sleep(2)
print("release")
keyboard.release(input)
time.sleep(2)
