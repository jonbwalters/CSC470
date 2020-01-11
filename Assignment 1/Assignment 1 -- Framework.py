# Program begun 12/16/19
# by Jonathan Walters (101-77-508)
# Assignment 1


import math
from tkinter import *


CanvasWidth = 800
CanvasHeight = 600
d = 500

# ***************************** Initialize Pyramid Object ***************************
# Definition  of the five underlying points
apex = [0,50,100]
base1 = [-50,-50,50]
base2 = [50,-50,50]
base3 = [50,-50,150]
base4 = [-50,-50,150]

# Definition of the five polygon faces using the meaningful point names
# Polys are defined in counter clockwise order when viewed from the outside
frontpoly = [apex,base1,base2]
rightpoly = [apex,base2,base3]
backpoly = [apex,base3,base4]
leftpoly = [apex,base4,base1]
bottompoly = [base4,base3,base2,base1]

# Definition of the object
Pyramid = [bottompoly, frontpoly, rightpoly, backpoly, leftpoly]

# Definition of the Pyramid's underlying point cloud.  No structure, just the points.
PyramidPointCloud = [apex, base1, base2, base3, base4]
PyramidPointCloudDefault = [apex, base1, base2, base3, base4]
#************************************************************************************

# This function resets the pyramid to its original size and location in 3D space
# Note that shortcuts like "apex = [0,50,100]" will not work as they build new
# structures rather than modifying the existing Pyramid / PyramidPointCloud
def resetPyramid():
    PyramidPointCloud[0][0] = 0
    PyramidPointCloud[0][1] = 50
    PyramidPointCloud[0][2] = 100
    PyramidPointCloud[1][0] = -50
    PyramidPointCloud[1][1] = -50
    PyramidPointCloud[1][2] = 50
    PyramidPointCloud[2][0] = 50
    PyramidPointCloud[2][1] = -50
    PyramidPointCloud[2][2] = 50
    PyramidPointCloud[3][0] = 50
    PyramidPointCloud[3][1] = -50
    PyramidPointCloud[3][2] = 150
    PyramidPointCloud[4][0] = -50
    PyramidPointCloud[4][1] = -50
    PyramidPointCloud[4][2] = 150


    print("resetPyramid stub executed.")

# This function translates an object by some displacement.  The displacement is a 3D
# vector so the amount of displacement in each dimension can vary.
def translate(object, displacement):
    # the object being passed in here is the pointcloud
    for vert in object:
        for i in range(0,3):
            vert[i] = vert[i]+displacement[i]
    print("translate stub executed.")

# This function performs a simple uniform scale of an object assuming the object is
# centered at the origin.  The scalefactor is a scalar.
def scale(object,scalefactor):
    #Really need to translate to origin first then scale then translate back
    for x in object:    #loop through each point in the point cloud
        for i in range(0,len(x)-1):    #loop through each coordinate in the point and scale
            x[i] = x[i]*scalefactor
    print("scale stub executed.")

# This function performs a rotation of an object about the Z axis (from +X to +Y)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CCW
# in a LHS when viewed from -Z [the location of the viewer in the standard position]
def rotateZ(object,degrees):
    for vert in object:
        angle = degrees*(3.141592)/180
        x = vert[0]
        y=vert[1]
        vert[0] = x * math.cos(angle) - y*math.sin(angle)
        vert[1] = x * math.sin(angle) + y * math.cos(angle)
    print("rotateZ stub executed.")

# This function performs a rotation of an object about the Y axis (from +Z to +X)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +Y looking toward the origin.
def rotateY(object,degrees):
    for vert in object:
        angle = degrees*(3.141592)/180
        x = vert[0]
        z = vert[2]
        vert[0] = x * math.cos(angle) + z*math.sin(angle)
        vert[2] = -x * math.sin(angle) + z * math.cos(angle)
    print("rotateY stub executed.")

# This function performs a rotation of an object about the X axis (from +Y to +Z)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +X looking toward the origin.
def rotateX(object,degrees):
    for vert in object:
        angle = degrees*(3.141592)/180
        y = vert[1]
        z = vert[2]
        vert[1] = y * math.cos(angle) - z*math.sin(angle)
        vert[2] = y * math.sin(angle) + z * math.cos(angle)
    print("rotateX stub executed.")

# The function will draw an object by repeatedly calling drawPoly on each polygon in the object
def drawObject(object):
    for x in object:
        drawPoly(x)
    print("drawObject stub executed.")

# This function will draw a polygon by repeatedly calling drawLine on each pair of points
# making up the object.  Remember to draw a line between the last point and the first.
def drawPoly(poly):
    for i in range(0, len(poly)-1):
       drawLine(poly[i],poly[i+1])
    #drawLine(poly[len(poly)-1], poly[0])

    print("drawPoly stub executed.")

# Project the 3D endpoints to 2D point using a perspective projection implemented in 'project'
# Convert the projected endpoints to display coordinates via a call to 'convertToDisplayCoordinates'
# draw the actual line using the built-in create_line method
def drawLine(start,end):
    #        w.create_line(startdisplay[0],startdisplay[1],enddisplay[0],enddisplay[1])
    startdisplay = convertToDisplayCoordinates(project(start)) #convert projected coordinates to display coords
    enddisplay = convertToDisplayCoordinates(project(end)) #convert projected coordinates to display coords
    w.create_line(startdisplay[0], startdisplay[1], enddisplay[0], enddisplay[1])
    print("drawLine stub executed.")

# This function converts from 3D to 2D (+ depth) using the perspective projection technique.  Note that it
# will return a NEW list of points.  We will not want to keep around the projected points in our object as
# they are only used in rendering
def project(point):
    ps = [0,0,0]  # initialize the coordinates
    ps[0] = (-d) * point[0]/((-d)+point[2])   #project the x-component
    ps[1] = (-d) * point[1] / ((-d) + point[2])  # project the y-component
    ps[2] = point[2] / ((-d) + point[2])  # project the z component
    return ps

# This function converts a 2D point to display coordinates in the tk system.  Note that it will return a
# NEW list of points.  We will not want to keep around the display coordinate points in our object as
# they are only used in rendering.
def convertToDisplayCoordinates(point):
    displayXY = [0, 0]   #initialize the coordinates
    displayXY[0] = point[0] + CanvasWidth/2   # x - component shift 200 pixels since size is 400x400 for graphing
    displayXY[1] = -point[1] + CanvasHeight/2   # make negative since down is positive in tkinter then create y - component shift for graphing
    return displayXY

# **************************************************************************
# Everything below this point implements the interface
def reset():
    w.delete(ALL)
    resetPyramid()
    drawObject(Pyramid)

def larger():
    w.delete(ALL)
    scale(PyramidPointCloud,1.1)
    drawObject(Pyramid)

def smaller():
    w.delete(ALL)
    scale(PyramidPointCloud,.9)
    drawObject(Pyramid)

def forward():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,0,5])
    drawObject(Pyramid)

def backward():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,0,-5])
    drawObject(Pyramid)

def left():
    w.delete(ALL)
    translate(PyramidPointCloud,[-5,0,0])
    drawObject(Pyramid)

def right():
    w.delete(ALL)
    translate(PyramidPointCloud,[5,0,0])
    drawObject(Pyramid)

def up():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,5,0])
    drawObject(Pyramid)

def down():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,-5,0])
    drawObject(Pyramid)

def xPlus():
    w.delete(ALL)
    rotateX(PyramidPointCloud,5)
    drawObject(Pyramid)

def xMinus():
    w.delete(ALL)
    rotateX(PyramidPointCloud,-5)
    drawObject(Pyramid)

def yPlus():
    w.delete(ALL)
    rotateY(PyramidPointCloud,5)
    drawObject(Pyramid)

def yMinus():
    w.delete(ALL)
    rotateY(PyramidPointCloud,-5)
    drawObject(Pyramid)

def zPlus():
    w.delete(ALL)
    rotateZ(PyramidPointCloud,5)
    drawObject(Pyramid)

def zMinus():
    w.delete(ALL)
    rotateZ(PyramidPointCloud,-5)
    drawObject(Pyramid)

root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
drawObject(Pyramid)
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
