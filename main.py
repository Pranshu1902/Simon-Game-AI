import time
import pyautogui

# color locations
green = [782, 435]
red = [1119, 423]
yellow = [782, 767]
blue = [1128, 770]

queue = []

def detectPatter():
    # while pyautogui.locateOnScreen("clicked.png", confidence=0.7) == None:
        # pass
        # pyautogui.press("a")

    # print("detected")
    print(pyautogui.locateOnScreen("clicked.png", confidence=0.7))
    # print(x, y)


time.sleep(3)

# start the game
pyautogui.press("a")
image = pyautogui.screenshot()
image.save("test.png")
detectPatter()
a
# while True:
#     detectPatter()
#     time.sleep(1)
