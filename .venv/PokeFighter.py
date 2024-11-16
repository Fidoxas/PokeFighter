from pynput import keyboard
import time
import pyautogui
from random import uniform
from PIL import ImageGrab

fight_hud_area = (290, 670, 720, 780)
fight_end_area = (325, 660, 1300, 720)
confidence_level = 0.01

# Ustawienie klawiszy ruchu
up = input("Wprowadź klawisz dla ruchu w górę: ")
down = input("Wprowadź klawisz dla ruchu w dół: ")
left = input("Wprowadź klawisz dla ruchu w lewo: ")
right = input("Wprowadź klawisz dla ruchu w prawo: ")

print("Welcome to PokeFIghter!")
finding = False
fighting = False
find_enabled = False

def click(button):
    pyautogui.keyDown(button)
    duration = uniform(0, 0.3)
    time.sleep(duration)
    pyautogui.keyUp(button)

def combination():
    time.sleep(uniform(7,8))
    click(right)
    click(down)
    click('z')
    time.sleep(uniform(1,4))

def find():
    global finding, fighting
    finding = True
    move_left_right()

def move_left_right():
    global fighting, find_enabled, finding
    dirLeft = False
    while find_enabled:
            if is_screen_black():
                time.sleep(3)
                if is_screen_black():
                    combination()
            else:
                if dirLeft == False:
                    pyautogui.keyDown(left)
                    time.sleep(uniform(0.2, 0.3))
                    pyautogui.keyUp(left)
                    dirLeft = True
                elif dirLeft == True:
                    pyautogui.keyDown(right)
                    time.sleep(uniform(0.2, 0.3))
                    pyautogui.keyUp(right)
                    dirLeft = False

def is_screen_black(threshold=0.5):
    screen = pyautogui.screenshot(region=(421, 793, 1058, 231))
    total_pixels = screen.size[0] * screen.size[1]
    black_pixels = 0
    # Sprawdzamy kolor w każdym pikselu
    for pixel in screen.getdata():
        if pixel == (0, 0, 0):  # Czarny kolor
            black_pixels += 1
    black_percentage = black_pixels / total_pixels
    return black_percentage >= threshold

def stop_find():
    global finding
    finding = False
    print("Stop finding")

def on_key_pressed(key):
    global find_enabled
    try:
        if key.char == '0':
            print("Naciśnięto klawisz '0'")
            combination()
        elif key.char == '-':
            print("Naciśnięto klawisz '-'")
            find_enabled = not find_enabled
            if find_enabled:
                find()
            elif not find_enabled:
                stop_find()
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_key_pressed)
listener.start()
listener.join()
