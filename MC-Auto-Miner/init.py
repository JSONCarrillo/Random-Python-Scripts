import pyautogui as pag
from time import sleep

def countdown():
    timer = 3

    while(timer != 0):
        print(timer)
        timer -= 1
        sleep(1)

def mine():
    pag.keyDown('o')
    sleep(1)
    pag.keyUp('o')
    sleep(2)

countdown()


while(True):
    mine()