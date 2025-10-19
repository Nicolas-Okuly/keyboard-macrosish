# ahk-macros.py
import sys
import pyautogui

pyautogui.PAUSE = 0.05

key = sys.argv[1] if len(sys.argv) > 1 else "NONE"

with open("C:\\Users\\nicol\\ahk-test-log.txt", "a") as f:
    f.write(f"Key pressed: {key}\n")

def left(count):
    pyautogui.press('left', presses=count, interval=0.005)

if (key == "c"):
    pyautogui.write("console.log(\"\");", 0.005)
    left(3)
elif key == "l":
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.press("backspace")
elif key == "w":
    pyautogui.write("while () {}", interval=0.005)
    left(4)
elif key == "Right":
    pyautogui.press("right", presses=3, interval=0.005)
elif key == "i":
    pyautogui.write("if () {}", interval=0.005)
    left(4)
elif key == ";":
    pyautogui.press("end")
    pyautogui.write(";")
