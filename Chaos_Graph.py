#!/usr/bin/python3
"""
This program converts a Chaos Function's output to a point on the
graph and draws it.

The program will first ask for two inputs on the command line, timedelay, and
number of iterations.
By S. Roland MacDavid
"""
from graphics import *

def setupWindow():
    win = GraphWin("Chaos Function", 800,800)
    win.setCoords(0.0,0.0,120,120)
    # Graph Lines. Start them at 10 from origin.
    # X Axis
    Line(Point(5,10), Point(110,10)).draw(win)
    # Y Axis
    Line(Point(10,5), Point(10,110)).draw(win)

    # X Line markers. Length of 3(y9 to y11) and spaced out from (0,0) by 10.
    # For first iteration, we'll have a line drawn from points (20,9) to (20,11)
    # and then text drawn at (20,7) that says "10". Thus the whole virtual graph in
    # graphics.py's graph is offset from (0,0) by 20.
    for i in range(2,12):
        Line(Point(i*10,9), Point(i*10,11)).draw(win)
        Text(Point(i*10,7), (i-1)*10).draw(win)

    # Y Markers. Same as previous for loop, but going vertical.
    for i in range(2,12):
        print("\ni ==",i)
        Line(Point(9,i*10), Point(11,i*10)).draw(win)
        Text(Point(7,i*10), (i-1)*10).draw(win)
    return win

def chaosGraphLoop(win):
    # Initial variables
    timeDelay = eval(input("How fast would you like between each plot?: "))
    iterations = eval(input("How many iterations?: "))
    z = 0.11
    iterationCounter = 0
    x = 10
    y = 10
    # The main loops
    for i in range(iterations):
        #The calculation itself.
        z = 3.9 * z * (1-z)
        # This counter helps us get past the fact that some necessary
        # previous point placeholders don't exist yet.
        iterationCounter = iterationCounter + 1
        wet suit action
        #Thought it would be fun to have the points graphed shown and formatted.
        infox = x - 10
        info = 'Plotting: %.2f' % infox
        #infoy = 'Point Y: %.2f' % y
        # With the counter set at 1, the "if" will set up some initial thingies.
        if iterationCounter == 1:
            # Converts output to be shown on graph
            x = 10 + (z * 100)
            point = Circle(Point(x,y),.35)
            point.setFill('yellow')
            point.draw(win)
            # Create (x,y) placeholders to make straight lines from last plotted
            # point, to the next plotted point so we can visually see how
            # the algorithm jumps from one number to the next. Cool!!
            plottedX = x
            plottedY = y
            # Switches the output to the other coord for proper graphing
            y = x
            output = Text(Point(60,118), info)
            #mesy = Text(Point(60,116), infoy)
            #mesx.draw(win)
            #mesy.draw(win)
            output.draw(win)
        #the next to if's function via a simple alternator
        elif iterationCounter % 2 == 0:
            # Alternates to y
            y = 10 + (z * 100)
            output.setText(info)
            point = Circle(Point(x,y),.35)
            point.setFill('red')
            point.draw(win)
            Line(Point(plottedX,plottedY), Point(x,y)).draw(win)
            plottedX = x
            plottedY = y
            x = y
            time.sleep(timeDelay)
        elif iterationCounter % 2 > 0:
            # Alternates to x
            x = 10 + (z * 100)
            output.setText(info)
            point = Circle(Point(x,y),.35)
            point.setFill('blue')
            point.draw(win)
            Line(Point(plottedX,plottedY), Point(x,y)).draw(win)
            plottedX = x
            plottedY = y
            y = x
            time.sleep(timeDelay)
def main():
    win = setupWindow()
    chaosGraphLoop(win)

if __name__ == "__main__":
    main()
