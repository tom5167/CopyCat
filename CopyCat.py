from pynput.keyboard import Key, Listener as KeyBoardListener
from pynput.mouse import Button, Listener as MouseListener
from pynput.mouse import Button, Controller as MouseController
import threading
import os
import signal
import logging
from datetime import datetime
import time

speed = "0"

def stopRecord():
    print("Stopped Recording")
    os.kill(os.getpid(),signal.SIGTERM)

def on_press_K(key):
    if(key == Key.esc):
        stopRecord()
        return
    logging.info("keyboard.press("+str(key)+")")

def on_release_K(key):
    logging.info("keyboard.release("+str(key)+")")

def on_move_M(x, y):
    logging.info("time.sleep("+speed+")")
    logging.info('pyautogui.moveTo{0}'.format((x,y)))

def on_click_M(x, y, button, pressed):
    logging.info("time.sleep("+speed+")")
    logging.info('pyautogui.moveTo{0}'.format((x,y)))
    if(button == Button.middle):
        stopRecord()
        return
    logging.info('{0}({1})'.format('mouse.press' if pressed else 'mouse.release',button))

def on_scroll_M(x, y, dx, dy):
    logging.info("time.sleep("+speed+")")
    logging.info('pyautogui.moveTo{0}'.format((x,y)))
    logging.info('mouse.scroll{0}'.format((dx, dy)))

def task1():
    mouse = MouseController()
    logging.info('mouse.position = {0}'.format(mouse.position))
    with MouseListener(on_move=on_move_M,on_click=on_click_M,on_scroll=on_scroll_M) as mouseListener:
        mouseListener.join()

def task2():
    with KeyBoardListener(on_press=on_press_K, on_release=on_release_K) as keyBoardListener:
        keyBoardListener.join()

t1 = threading.Thread(target=task1, name='t1')
t2 = threading.Thread(target=task2, name='t2')

if __name__ == "__main__":
    timestamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    recordfileName = "runCopyCat_" + timestamp + ".py"
    print("Record file Name : "+recordfileName)
    logging.basicConfig(filename=(recordfileName), level=logging.DEBUG, format='%(message)s')

    logging.info("import time")
    logging.info("import pyautogui")
    logging.info("from pynput.keyboard import Key, Controller as KeyboardController")
    logging.info("from pynput.mouse import Button, Controller as MouseController")
    logging.info("keyboard = KeyboardController()")
    logging.info("mouse = MouseController()")

    print("Gonna start in 5 secs")
    time.sleep(1)
    print("Gonna start in 4 secs")
    time.sleep(1)
    print("Gonna start in 3 secs")
    time.sleep(1)
    print("Gonna start in 2 secs")
    time.sleep(1)
    print("Gonna start in 1 secs")
    time.sleep(1)
    print("Started Recording")

    # starting threads
    t1.start()
    t2.start()
