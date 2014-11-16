# This Program converts a Chaos Function's output to a point on the
# graph and draws it.
# By S. Roland MacDavid


from graphics import *

win = GraphWin("Chaos Function", 800,800)
win.setCoords(0.0,0.0,120,120)

# Graph Lines
# X Axis
Line(Point(5,10), Point(110,10)).draw(win)
# Y Axis
Line(Point(10,5), Point(10,110)).draw(win)
# X markers
Line(Point(20,9), Point(20,11)).draw(win) #x, 10
Text(Point(20,7), 10).draw(win)
Line(Point(30,9), Point(30,11)).draw(win) #x, 20
Text(Point(30,7), 20).draw(win)
Line(Point(40,9), Point(40,11)).draw(win) #x, 30
Text(Point(40,7), 30).draw(win)
Line(Point(50,9), Point(50,11)).draw(win) #x, 40
Text(Point(50,7), 40).draw(win)
Line(Point(60,9), Point(60,11)).draw(win) #x, 50
Text(Point(60,7), 50).draw(win)
Line(Point(70,9), Point(70,11)).draw(win) #x, 60
Text(Point(70,7), 60).draw(win)
Line(Point(80,9), Point(80,11)).draw(win) #x, 70
Text(Point(80,7), 70).draw(win)
Line(Point(90,9), Point(90,11)).draw(win) #x, 80
Text(Point(90,7), 80).draw(win)
Line(Point(100,9), Point(100,11)).draw(win) #x, 90
Text(Point(100,7), 90).draw(win)
Line(Point(110,9), Point(110,11)).draw(win) #x, 100
Text(Point(110,7), 100).draw(win)

# Y Markers
Line(Point(9,20), Point(11,20)).draw(win) #x, 10
Text(Point(7,20), 10).draw(win)
Line(Point(9,30), Point(11,30)).draw(win) #x, 20
Text(Point(7,30), 20).draw(win)
Line(Point(9,40), Point(11,40)).draw(win) #x, 30
Text(Point(7,40), 30).draw(win)
Line(Point(9,50), Point(11,50)).draw(win) #x, 40
Text(Point(7,50), 40).draw(win)
Line(Point(9,60), Point(11,60)).draw(win) #x, 50
Text(Point(7,60), 50).draw(win)
Line(Point(9,70), Point(11,70)).draw(win) #x, 60
Text(Point(7,70), 60).draw(win)
Line(Point(9,80), Point(11,80)).draw(win) #x, 70
Text(Point(7,80), 70).draw(win)
Line(Point(9,90), Point(11,90)).draw(win) #x, 80
Text(Point(7,90), 80).draw(win)
Line(Point(9,100), Point(11,100)).draw(win) #x, 90
Text(Point(7,100), 90).draw(win)
Line(Point(9,110), Point(11,110)).draw(win) #x, 100
Text(Point(7,110), 100).draw(win)

# Initial variables
timedelay = eval(input("How fast would you like between each plot?: "))
it = eval(input("How many iterations?: "))
z = 0.11
counter = 0
x = 10
y = 10
# Da Loop.
for i in range(it):
    z = 3.9 * z * (1-z)
    # This counter helps us get past the fact that some necessary
    # previous point placeholders don't exist yet.
    counter = counter + 1
    
    #Thought it would be fun to have the points graphed shown and formatted.
    # info = 'Point X: %.2f' % x + ' Y: %.2f' % y
    infox = x - 10
    info = 'Plotting: %.2f' % infox
    #infoy = 'Point Y: %.2f' % y
    # With the counter set at 1, the "if" will set up some initial thingies.
    if counter == 1:
        # Converts output to be shown on graph
        x = 10 + (z * 100)
        point = Circle(Point(x,y),.35)
        point.setFill('yellow')
        point.draw(win)
        # Switches the output to the other coord for proper graphing
        # Creates the placeholders to make straight lines.
        px = x
        py = y
        y = x
        output = Text(Point(60,118), info)
        #mesy = Text(Point(60,116), infoy)
        #mesx.draw(win)
        #mesy.draw(win)
        output.draw(win)
    #the next to if's function via a simple alternator
    elif counter % 2 == 0:
        # Alternates to y
        y = 10 + (z * 100)
        output.setText(info)
        point = Circle(Point(x,y),.35)
        point.setFill('red')
        point.draw(win)
        Line(Point(px,py), Point(x,y)).draw(win)
        px = x
        py = y
        x = y
        #mesx.setText(infox)
        #mesy.setText(infoy)
        time.sleep(timeDelay)
    elif counter % 2 > 0:
        # Alternates to x
        x = 10 + (z * 100)
        output.setText(info)
        point = Circle(Point(x,y),.35)
        point.setFill('blue')
        point.draw(win)
        Line(Point(px,py), Point(x,y)).draw(win)
        px = x
        py = y
        y = x
        #mesx.setText(infox)
        #mesy.setText(infoy)
        time.sleep(timeDelay)
