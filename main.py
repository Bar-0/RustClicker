import keyboard
import mouse
import time

isClicking = False
isClickingExit = False
def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("Кликер Отключен")
    else:
        isClicking = True
        print("Кликер Включен")

keyboard.add_hotkey('Alt+X', set_clicker)
keyboard.add_hotkey('Alt+C', isClickingExit)

while 1:
    if isClicking:
        #time.sleep(0.001)
        mouse.double_click('left')
        if isClicking == False:
            print("выход из программы 1")
            break
    if isClickingExit == True:
        print("выход из программы 2")
        break
    else:
        print("выход из программы 3")
        time.sleep(0.01)

