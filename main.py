import time
import pyautogui

# color locations
green = [782, 435]
red = [1119, 423]
yellow = [782, 767]
blue = [1128, 770]

queue = []

def detectPattern():
    pyautogui.screenshot("me.png")

    x, y, h, w = pyautogui.locateOnScreen("clicked.png", region=(500,400,1200,900), confidence=0.5)
    a = x + h//2
    b = y + w//2

    # adding new pattern to queue
    queue.append([a, b])


time.sleep(3)

# start the game
pyautogui.press("a")
detectPattern()

while True:
    # click previous pattern
    for x, y in queue:
        pyautogui.click(x, y)
        time.sleep(1)

    # detect new pattern
    detectPattern()
    time.sleep(1)
