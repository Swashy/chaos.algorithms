#!/usr/bin/python3
from gi.repository import Gtk, Gdk
import cairo
from time import sleep
"""
https://en.wikipedia.org/wiki/Collatz_conjecture
From Wikipedia:

"If n is even, divide it by 2 (n/2).
If n is odd, multiply it by 3 and add 1 (3n+1).
Repeat the process (which has been called "Half Or Triple Plus One", or
HOTPO[6]) indefinitely. The conjecture is that no matter what number you start
with, you will always eventually reach 1. The property has also been called
oneness.[7]"

This program graphs the output of the syracuse function, aka Collatz Conjecture.
x = The input number.
y = Number of iterations to reach 1.
"""

def syracuse(n,counter):
    if n > 1:
        # If n is odd
        if (n%2 == 0) and (n != 1):
            n = n//2
            counter +=1
        elif n !=1:
            n = 3*n + 1
            counter +=1
        counter = syracuse(n,counter)
    return(counter)

def introspection(inst):
    for names in dir(inst):
        attr = getattr(inst,names)
        if callable(attr):
            print(names,':',attr.__doc__)

class window(Gtk.Window):
    def __init__(self):

        # initialize Gtk.Window (super calls the parent class's method)
        super().__init__(title="Syracuse Graph")
        #Then initialize our init
        self.init_ui()

    def init_ui(self):

        self.set_position(Gtk.WindowPosition.CENTER)

        self.grid = Gtk.Grid()

        self.syracuseDraw = Gtk.DrawingArea()
        self.syracuseDraw.set_size_request(1200,600)
        self.handlerid = -1
        self.grid.attach(self.syracuseDraw,0,1,1,1)

        self.button = Gtk.Button("Draw Syracuse!")
        self.button.connect("clicked",self.on_button_clicked)
        self.grid.attach(self.button,0,0,1,1)

        self.add(self.grid)

        self.coordinateFrequency = {}

    def on_button_clicked(self,widget):
        if self.handlerid > 0:
            self.syracuseDraw.handler_unblock(self.handlerid)
        else:
            self.handlerid = self.syracuseDraw.connect("draw",self.on_draw)
        self.syracuseDraw.queue_draw()

    def on_draw(self, widget, cairoCon):
        cairoCon.set_source_rgb(0, 0, 0)
        for x in range(0,8000):
            y = syracuse(x,0)
            #Shrink and stretch our coordinates so we can see the coolness!
            x = x/7
            y = y*2.5
            if (x,y) in self.coordinateFrequency.keys():
                self.coordinateFrequency[(x,y)] += 1
            else:
                self.coordinateFrequency[(x,y)] = 1
            cairoCon.rectangle(x,y,.01,.01)
            cairoCon.stroke()
        #Attempt to make certain spots look larger if alot of points have
        #already been placed.
        for i in self.coordinateFrequency.keys():
            if self.coordinateFrequency[i] > 1:
                print(i, self.coordinateFrequency[i])
        self.syracuseDraw.handler_block(self.handlerid)
        

if __name__ == "__main__":
    win = window()

    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    
    Gtk.main()







