import pyglet
from pynput.mouse import Controller, Button
from pynput.mouse import Listener as MouseListener
import os
import keyboard
activate = 1
def on_scroll(x, y, dx, dy):
    if activate == 1:
        print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
        print("Mouse scrolled")
        mouse.click(Button.right, 1)
keyboard.on_press_key("F5", lambda _:toggle())
def toggle():
    global activate
    if activate == 1:
        activate = 0
        print("deactivated")
    else:
        activate = 1
        print("activated")
mouse_listener = MouseListener(on_move=None, on_click=None, on_scroll=on_scroll)
mouse = Controller()
mouse_listener.start()
mouse_listener.join()