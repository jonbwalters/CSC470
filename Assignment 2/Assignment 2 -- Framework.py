# Program begun 12/27/19
# by Jonathan Walters (101-77-508)
# Assignment 2


import math
from tkinter import *
import copy

class Object:
    def __init__(self):
        self.PointCloud = []
        self.DefaultCloud = []
        self.Polys = []

    def setPointCloud(self, pointList):
        if len(self.PointCloud) == 0:
            for point in pointList:
                self.PointCloud.append(point)
            self.DefaultCloud = copy.deepcopy(self.PointCloud)
        else:
            for i in range(len(pointList)):
                for j in range(len(pointList[i])):
                    self.PointCloud[i][j] = pointList[i][j]

    def getPointCloud(self):
        return self.PointCloud

    def setPolys(self,polygon):
        self.Polys.append(polygon)

    def getPolys(self):
        return self.Polys

    def resetObject(self):
        for i in range(len(self.DefaultCloud)):
            for j in range(len(self.DefaultCloud[i])):
                self.PointCloud[i][j] = self.DefaultCloud[i][j]
        print("reset stub executed.")

    def translate(self, displacement):
        # the object being passed in here is the pointcloud
        for vert in self.PointCloud:
            for i in range(0, 3):
                vert[i] = vert[i] + displacement[i]
        print("translate stub executed.")

    def scale(self, scalefactor):
        # Really need to translate to origin first then scale then translate back
        for x in self.PointCloud:  # loop through each point in the point cloud
            for i in range(0, len(x) - 1):  # loop through each coordinate in the point and scale
                x[i] = x[i] * scalefactor[i]
        print("scale stub executed.")

    def rotateZ(self, degrees):
        for vert in self.PointCloud:
            angle = degrees * (3.141592) / 180
            x = vert[0]
            y = vert[1]
            vert[0] = x * math.cos(angle) - y * math.sin(angle)
            vert[1] = x * math.sin(angle) + y * math.cos(angle)
        print("rotateZ stub executed.")

    def rotateY(self, degrees):
        for vert in self.PointCloud:
            angle = degrees * (3.141592) / 180
            x = vert[0]
            z = vert[2]
            vert[0] = x * math.cos(angle) + z * math.sin(angle)
            vert[2] = -x * math.sin(angle) + z * math.cos(angle)
        print("rotateY stub executed.")

    def rotateX(self, degrees):
        for vert in self.PointCloud:
            angle = degrees * (3.141592) / 180
            y = vert[1]
            z = vert[2]
            vert[1] = y * math.cos(angle) - z * math.sin(angle)
            vert[2] = y * math.sin(angle) + z * math.cos(angle)
        print("rotateX stub executed.")

    # The function will draw an object by repeatedly calling drawPoly on each polygon in the object
    def drawObject(self):
        for x in self.Polys:
            self.drawPoly(x)
        print("drawObject stub executed.")

    # This function will draw a polygon by repeatedly calling drawLine on each pair of points
    # making up the object.  Remember to draw a line between the last point and the first.
    def drawPoly(self, poly):
        for i in range(0, len(poly) - 1):
            self.drawLine(poly[i], poly[i + 1])
        # drawLine(poly[len(poly)-1], poly[0])

        print("drawPoly stub executed.")

    # Project the 3D endpoints to 2D point using a perspective projection implemented in 'project'
    # Convert the projected endpoints to display coordinates via a call to 'convertToDisplayCoordinates'
    # draw the actual line using the built-in create_line method
    def drawLine(self, start, end):
        #        w.create_line(startdisplay[0],startdisplay[1],enddisplay[0],enddisplay[1])
        startdisplay = self.convertToDisplayCoordinates(self.project(start))  # convert projected coordinates to display coords
        enddisplay = self.convertToDisplayCoordinates(self.project(end))  # convert projected coordinates to display coords
        w.create_line(startdisplay[0], startdisplay[1], enddisplay[0], enddisplay[1])
        print("drawLine stub executed.")

    # This function converts from 3D to 2D (+ depth) using the perspective projection technique.  Note that it
    # will return a NEW list of points.  We will not want to keep around the projected points in our object as
    # they are only used in rendering
    def project(self, point):
        ps = [0, 0, 0]  # initialize the coordinates
        ps[0] = (-d) * point[0] / ((-d) + point[2])  # project the x-component
        ps[1] = (-d) * point[1] / ((-d) + point[2])  # project the y-component
        ps[2] = point[2] / ((-d) + point[2])  # project the z component
        return ps

    # This function converts a 2D point to display coordinates in the tk system.  Note that it will return a
    # NEW list of points.  We will not want to keep around the display coordinate points in our object as
    # they are only used in rendering.
    def convertToDisplayCoordinates(self, point):
        displayXY = [0, 0]  # initialize the coordinates
        displayXY[0] = point[0] + CanvasWidth  # x - component shift 200 pixels since size is 400x400 for graphing
        displayXY[1] = -point[1] + CanvasHeight  # make negative since down is positive in tkinter then create y - component shift for graphing
        return displayXY

CanvasWidth = 400
CanvasHeight = 400
d = 500

# ***************************** Initialize Objects ***************************
# Definition  of the five underlying points
apex = [0,50,100]
base1 = [-50,-50,50]
base2 = [50,-50,50]
base3 = [50,-50,150]
base4 = [-50,-50,150]
Default = [apex, base1, base2, base3, base4]

pyramid = Object()
pyramid.setPointCloud(Default)
selected = pyramid
selected.Polys.append([selected.PointCloud[0],selected.PointCloud[1],selected.PointCloud[2]])
selected.Polys.append([selected.PointCloud[0],selected.PointCloud[2],selected.PointCloud[3]])
selected.Polys.append([selected.PointCloud[0],selected.PointCloud[3],selected.PointCloud[4]])
selected.Polys.append([selected.PointCloud[0],selected.PointCloud[4],selected.PointCloud[1]])
selected.Polys.append([selected.PointCloud[4],selected.PointCloud[3],selected.PointCloud[2], selected.PointCloud[1]])

Shapes = [pyramid]

def drawAllObjects():
    for object in Shapes:
        object.resetObject()
        object.drawObject(object.Polys)

# **************************************************************************
# Everything below this point implements the interface
def reset():
    w.delete(ALL)
    for object in Shapes:
        object.resetObject()
        object.drawObject(object.Polys)

def larger():
    w.delete(ALL)
    selected.scale(1.1)
    drawAllObjects()

def smaller():
    w.delete(ALL)
    selected.scale(.9)
    drawAllObjects()

def forward():
    w.delete(ALL)
    selected.translate([0,0,5])
    drawAllObjects()

def backward():
    w.delete(ALL)
    selected.translate([0,0,-5])
    drawAllObjects()

def left():
    w.delete(ALL)
    selected.translate([-5,0,0])
    drawAllObjects()

def right():
    w.delete(ALL)
    selected.translate([5,0,0])
    drawAllObjects()

def up():
    w.delete(ALL)
    selected.translate([0,5,0])
    drawAllObjects()

def down():
    w.delete(ALL)
    selected.translate([0,-5,0])
    drawAllObjects()

def xPlus():
    w.delete(ALL)
    selected.rotateX(5)
    drawAllObjects()

def xMinus():
    w.delete(ALL)
    selected.rotateX(-5)
    drawAllObjects()

def yPlus():
    w.delete(ALL)
    selected.rotateY(5)
    drawAllObjects()

def yMinus():
    w.delete(ALL)
    selected.rotateY(-5)
    drawAllObjects()

def zPlus():
    w.delete(ALL)
    selected.rotateZ(5)
    drawAllObjects()

def zMinus():
    w.delete(ALL)
    selected.rotateZ(-5)
    drawAllObjects()

root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
drawAllObjects()
w.pack()

controlpanel = Frame(outerframe)
controlpanel.pack()

resetcontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
resetcontrols.pack(side=LEFT)

resetcontrolslabel = Label(resetcontrols, text="Reset")
resetcontrolslabel.pack()

resetButton = Button(resetcontrols, text="Reset", fg="green", command=reset)
resetButton.pack(side=LEFT)

scalecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
scalecontrols.pack(side=LEFT)

scalecontrolslabel = Label(scalecontrols, text="Scale")
scalecontrolslabel.pack()

largerButton = Button(scalecontrols, text="Larger", command=larger)
largerButton.pack(side=LEFT)

smallerButton = Button(scalecontrols, text="Smaller", command=smaller)
smallerButton.pack(side=LEFT)

translatecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
translatecontrols.pack(side=LEFT)

translatecontrolslabel = Label(translatecontrols, text="Translation")
translatecontrolslabel.pack()

forwardButton = Button(translatecontrols, text="FW", command=forward)
forwardButton.pack(side=LEFT)

backwardButton = Button(translatecontrols, text="BK", command=backward)
backwardButton.pack(side=LEFT)

leftButton = Button(translatecontrols, text="LF", command=left)
leftButton.pack(side=LEFT)

rightButton = Button(translatecontrols, text="RT", command=right)
rightButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="UP", command=up)
upButton.pack(side=LEFT)

downButton = Button(translatecontrols, text="DN", command=down)
downButton.pack(side=LEFT)

rotationcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
rotationcontrols.pack(side=LEFT)

rotationcontrolslabel = Label(rotationcontrols, text="Rotation")
rotationcontrolslabel.pack()

xPlusButton = Button(rotationcontrols, text="X+", command=xPlus)
xPlusButton.pack(side=LEFT)

xMinusButton = Button(rotationcontrols, text="X-", command=xMinus)
xMinusButton.pack(side=LEFT)

yPlusButton = Button(rotationcontrols, text="Y+", command=yPlus)
yPlusButton.pack(side=LEFT)

yMinusButton = Button(rotationcontrols, text="Y-", command=yMinus)
yMinusButton.pack(side=LEFT)

zPlusButton = Button(rotationcontrols, text="Z+", command=zPlus)
zPlusButton.pack(side=LEFT)

zMinusButton = Button(rotationcontrols, text="Z-", command=zMinus)
zMinusButton.pack(side=LEFT)

root.mainloop()
