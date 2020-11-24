import pynput
from pynput.mouse import Controller, Button
from pynput.mouse import Listener as MouseListener
import os
def on_scroll(x, y, dx, dy):
    print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    print("Mouse scrolled")
    mouse.press(Button.right)
    mouse.release(Button.right)
mouse_listener = MouseListener(on_move=None, on_click=None, on_scroll=on_scroll)
mouse = Controller()
mouse_listener.start()
mouse_listener.join()