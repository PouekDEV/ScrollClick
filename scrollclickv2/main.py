import pynput
from pynput.mouse import Controller, Button
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener
import os
import pyglet
import pyglet.window.key
width = 600
height = 500
title = "ScrollClick by Pouek_"
window = pyglet.window.Window(width, height, title) 
text = "ScrollClick"
Scrolled = "Don't worry now. It's working I promise"
etc = "Made by Pouek_ @2020"
mouse = Controller()

label3 = pyglet.text.Label(etc, 
                          font_name ='Times New Roman', 
                          font_size = 24, 
                          x = window.width//2, y = window.height//1.25, 
                          anchor_x ='center', anchor_y ='center') 

label = pyglet.text.Label(text, 
                          font_name ='Times New Roman', 
                          font_size = 36, 
                          x = window.width//2, y = window.height//2, 
                          anchor_x ='center', anchor_y ='center') 
  
new_label = pyglet.text.Label(text, 
                          font_name ='Times New Roman', 
                          font_size = 10, 
                          x = 25, y = 25) 

new_label2 = pyglet.text.Label(text, 
                          font_name ='Times New Roman', 
                          font_size = 10, 
                          x = 25, y = 25) 

label2 = pyglet.text.Label(Scrolled, 
                          font_name ='Times New Roman', 
                          font_size = 24, 
                          x = window.width//2, y = window.height//10, 
                          anchor_x ='center', anchor_y ='center') 

@window.event 
def on_draw():      
    window.clear() 
    label3.draw()
    label.draw() 
    label2.draw()

mouse = Controller()
print ("Current position: " + str(mouse.position))
img = image = pyglet.resource.image("logo.png")
window.set_icon(img)
pyglet.app.run() 
os.system("1.py")