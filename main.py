import pyautogui
import time
from random import uniform


def main():
    while True:
        time.sleep(1)
        build_larder()
        time.sleep(1.5)
        remove_larder()
        time.sleep(0.4)
        get_planks()
        time.sleep(0.4)
        build_larder()
        time.sleep(1.5)
        remove_larder()
        time.sleep(0.6)
        build_larder()
        time.sleep(1.9)
        remove_larder()


def build_larder():
    pyautogui.moveTo(1547, 1242)
    time.sleep(round(uniform(0.06, 0.08), 2))
    pyautogui.rightClick(interval=(round(uniform(0.02, 0.05), 2)))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
    time.sleep(round(uniform(0.6, 0.7), 2))
    pyautogui.press("2")


def remove_larder():
    pyautogui.moveTo(1547, 1242)
    time.sleep(round(uniform(0.06, 0.08), 2))
    pyautogui.rightClick(interval=(round(uniform(0.02, 0.05), 2)))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
    time.sleep(round(uniform(0.63, 0.68), 2))
    pyautogui.press("1")


def get_planks():
    pyautogui.moveTo(1106, 869)
    time.sleep(round(uniform(0.06, 0.08), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
    time.sleep(round(uniform(0.64, 0.69), 2))
    pyautogui.press("1")


if __name__ == "__main__":
    time.sleep(3)
    main()
