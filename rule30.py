#!/usr/bin/python3
from gi.repository import Gtk, Gdk
import cairo
from time import sleep
from os import popen
from math import ceil

def ruleThirty(iterations,length = int(popen('stty size', 'r').read().split()[1])):
    """
    http://en.wikipedia.org/wiki/Rule_30
    
    This program demonstrates the chaotic rule, "rule 30"
    Function ruleThirty(i,l) first takes <iterations>, which is how many lines it
    will generate.
    
    We then take the width of the terminal so we can display the algorithm
    nicely, unless otherwise stated.
    
    We then generate a dictionary of arrays, where the key of the dictionary
    is the "level" of the graphical display, and each value is a generated tuple
    of either 0, 1, 2, 3, or 4
    
    
    """
    dicArray = {}
    length -= 6
    half = ceil(length/2)
    tempList = []
    #This for loop makes the first "level", which seeds a 1 in the middle of
    #a list of zero's.
    for i in range(0,length+1):
        if i == half:
            tempList.append(1)
        else:
            tempList.append(0)
    dicArray[0] = tuple(tempList)
    
    level = 1
    loop = True
    
    #This loop gets the three "cells" above a to be determined value, one above,
    #and the two to the left and right of the value.
    while loop:
        tempList = []
        for i in range(0,length+1):
            threeList = []
            #I have to put "tries" here because if we're at the beginning or
            #end of a level, it will give us an index error. If its an edge-case
            #then append a 0.
            try:
                threeList.append(dicArray[level-1][i-1])
            except:
                threeList.append(0)
            try:
                threeList.append(dicArray[level-1][i])
            except:
                threeList.append(0)
            try:
                threeList.append(dicArray[level-1][i+1])
            except:
                threeList.append(0)
            
            #This goes through the patterns that determine a cell.
            #1st pattern
            if threeList[0] > 0 and threeList[1] > 0 and threeList[2] > 0:
                tempList.append(0)
            #2
            elif threeList[0] > 0 and threeList[1] > 0 and threeList[2] == 0:
                tempList.append(0)
            #3  
            elif threeList[0] > 0 and threeList[1] == 0 and threeList[2] > 0:
                tempList.append(0)
            #4  
            elif threeList[0] > 0 and threeList[1] == 0 and threeList[2] == 0:
                tempList.append(1)
            #5  
            elif threeList[0] == 0 and threeList[1] > 0 and threeList[2] > 0:
                tempList.append(2)
            #6  
            elif threeList[0] == 0 and threeList[1] > 0 and threeList[2] == 0:
                tempList.append(3)
            #7  
            elif threeList[0] == 0 and threeList[1] == 0 and threeList[2] > 0:
                tempList.append(4)
            #8
            else:
                tempList.append(0)
        #Tuple-ize and add the generated "level" to the dictionary.
        dicArray[level] = tuple(tempList)
        level +=1
        if level == iterations:
            loop = False
    return dicArray
    
    
class window(Gtk.Window):
    def __init__(self):
        super().__init__(title="Rule 30 Representation")
        self.init_ui()
        
    def init_ui(self):
        self.set_position(Gtk.WindowPosition.CENTER)
        
        self.cells = ruleThirty(400,1000)
        
        self.grid = Gtk.Grid()

        self.ruleDraw = Gtk.DrawingArea()
        self.ruleDraw.set_size_request(1600,800)
        self.handlerid = -1
        self.grid.attach(self.ruleDraw,0,1,1,1)

        self.button = Gtk.Button("Draw!")
        self.button.connect("clicked",self.on_button_clicked)
        self.grid.attach(self.button,0,0,1,1)

        self.add(self.grid)

        self.coordinateFrequency = {}

    def on_button_clicked(self,widget):
        if self.handlerid > 0:
            self.ruleDraw.handler_unblock(self.handlerid)
        else:
            self.handlerid = self.ruleDraw.connect("draw",self.on_draw)
        self.ruleDraw.queue_draw()

    def on_draw(self, widget, cairoCon):
        width = 1200
        height = 600
        rows = 0
        columns = 0
        cairoCon.set_source_rgb(0, 0, 0)
        cairoCon.select_font_face("Purisa", cairo.FONT_SLANT_NORMAL, 
        cairo.FONT_WEIGHT_NORMAL)
        cairoCon.set_font_size(13)
        for i in self.cells.values():
            columns=0
            rows+=2
            for j in i:
                if j == 0:
                    #cairoCon.rectangle(columns,rows,.006,.006)
                    #cairoCon.stroke()
                    columns+=2
                elif j > 1:
                    #print(columns,rows)
                    cairoCon.rectangle(columns,rows,.05,.05)
                    cairoCon.stroke()
                    columns+=2
        self.ruleDraw.handler_block(self.handlerid)
         
#Function to display rule 30 in the terminal.
def consoleDisplay():
    x = ruleThirty(1000)
    for i in x.keys():
        print(i," ", end='')
        for j in x[i]:
            if j == 0:
                print(' ', end='')
            else:
                print(j, end='')
        print() 
        sleep(0.01)
    print('\n')
         

if __name__ == "__main__":
    win = window()

    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    
    Gtk.main()








