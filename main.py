#this is the main file. It is mostly just the GUI and some functions that need to be in this file
#import files and modules
from tkinter import Tk, Canvas, pack, BOTH
from functions import *

#makes window
window = Tk()
window.title('Register')
window.geometry('800x800')

#makes canvas
canvas = Canvas(window,height=800,width=800)
canvas.pack(fill=BOTH,expand=True)

#mainloop
run = True
while run:
  if change():
    pass
  canvas.update()
