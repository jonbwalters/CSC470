# Program begun 12/28/19
# by Jonathan Walters (101-77-508)
# Assignment 1


import math
from tkinter import *
import copy

class Object:

    def __init__(self):

        self.PointCloud = []
        self.DefaultCloud = []
        self.Polys = []
        self.CP = [0,0,0]

    def setPointCloud(self, pointList):
        if len(self.PointCloud) == 0:
            for point in pointList:
                self.PointCloud.append(point)
            self.DefaultCloud = copy.deepcopy(self.PointCloud)
        else:
            for i in range(len(pointList)):
                for j in range(len(pointList[i])):
                    self.PointCloud[i][j] = pointList[i][j]
        self.GetCenter()

    def GetCenter(self):
        xsum = 0
        ysum = 0
        zsum = 0
        for point in self.PointCloud:
            xsum = xsum + point[0]
            ysum = ysum + point[1]
            zsum = zsum + point[2]
        self.CP[0] = xsum/len(self.PointCloud)
        self.CP[1] = ysum / len(self.PointCloud)
        self.CP[2] = zsum / len(self.PointCloud)

    def getPointCloud(self):
        return self.PointCloud

    def setPolys(self,polygon):
        self.Polys.append(polygon)

    def getPolys(self):
        return self.Polys

    # This function resets the object to its original size and location in 3D space
    def resetObject(self):
        for i in range(len(self.DefaultCloud)):
            for j in range(len(self.DefaultCloud[i])):
                self.PointCloud[i][j] = self.DefaultCloud[i][j]
        print("reset stub executed.")

CanvasWidth = 400
CanvasHeight = 400
d = 500

# ***************************** Initialize Pyramid Object ***************************
# Definition  of the five underlying points
apex = [0,50,100]
base1 = [-50,-50,50]
base2 = [50,-50,50]
base3 = [50,-50,150]
base4 = [-50,-50,150]

# Definition of the objects
Default = [apex, base1, base2, base3, base4]

pyramid1 = Object()
pyramid1.setPointCloud(Default)


selected = pyramid1
# Definition of the five polygon faces using the meaningful point names
# Polys are defined in counter clockwise order when viewed from the outside
selected.Polys.append([selected.PointCloud[0],selected.PointCloud[1],selected.PointCloud[2]])
selected.Polys.append([selected.PointCloud[0],selected.PointCloud[2],selected.PointCloud[3]])
selected.Polys.append([selected.PointCloud[0],selected.PointCloud[3],selected.PointCloud[4]])
selected.Polys.append([selected.PointCloud[0],selected.PointCloud[4],selected.PointCloud[1]])
selected.Polys.append([selected.PointCloud[4],selected.PointCloud[3],selected.PointCloud[2], selected.PointCloud[1]])


top1 = [-100, 25, 50]
base1 = [-100,-25,50]
top2 = [-50, 25, 50]
base2 = [-50,-25,50]
top3 = [-50, 25, 150]
base3 = [-50,-25,150]
top4 = [-100, 25, 150]
base4 = [-100,-25,150]

Default = [top1, base1, top2, base2, top3, base3, top4, base4]
cube1 = Object()
cube1.setPointCloud(Default)
selected = cube1
# Definition of the six polygon faces using the meaningful point names
# Polys are defined in counter clockwise order when viewed from the outside
selected.Polys.append([selected.PointCloud[0],selected.PointCloud[1],selected.PointCloud[3],selected.PointCloud[2]])
selected.Polys.append([selected.PointCloud[2],selected.PointCloud[3],selected.PointCloud[5],selected.PointCloud[4]])
selected.Polys.append([selected.PointCloud[4],selected.PointCloud[5],selected.PointCloud[7],selected.PointCloud[6]])
selected.Polys.append([selected.PointCloud[6],selected.PointCloud[7],selected.PointCloud[1],selected.PointCloud[0]])
selected.Polys.append([selected.PointCloud[0],selected.PointCloud[2],selected.PointCloud[4],selected.PointCloud[6]])
selected.Polys.append([selected.PointCloud[1],selected.PointCloud[3],selected.PointCloud[5],selected.PointCloud[7]])

top1 = [100, 25, 50]
base1 = [100,-25,50]
top2 = [50, 25, 50]
base2 = [50,-25,50]
top3 = [50, 25, 150]
base3 = [50,-25,150]
top4 = [100, 25, 150]
base4 = [100,-25,150]

Default = [top1, base1, top2, base2, top3, base3, top4, base4]
cube2 = Object()
cube2.setPointCloud(Default)
selected = cube2

# Definition of the six polygon faces using the meaningful point names
# Polys are defined in counter clockwise order when viewed from the outside
selected.Polys.append([selected.PointCloud[0],selected.PointCloud[1],selected.PointCloud[3],selected.PointCloud[2]])
selected.Polys.append([selected.PointCloud[2],selected.PointCloud[3],selected.PointCloud[5],selected.PointCloud[4]])
selected.Polys.append([selected.PointCloud[4],selected.PointCloud[5],selected.PointCloud[7],selected.PointCloud[6]])
selected.Polys.append([selected.PointCloud[6],selected.PointCloud[7],selected.PointCloud[1],selected.PointCloud[0]])
selected.Polys.append([selected.PointCloud[0],selected.PointCloud[2],selected.PointCloud[4],selected.PointCloud[6]])
selected.Polys.append([selected.PointCloud[1],selected.PointCloud[3],selected.PointCloud[5],selected.PointCloud[7]])

selected = pyramid1
Shapes = [pyramid1, cube1, cube2]
selectindex = 0

#************************************************************************************


# This function translates an object by some displacement.  The displacement is a 3D
# vector so the amount of displacement in each dimension can vary.
def translate(object, displacement):
    # the object being passed in here is the shape object
    # in my object class there is a varaible called PointCloud
    pccopy = copy.deepcopy(object.getPointCloud())
    for vert in pccopy:
        for i in range(0,3):
            vert[i] = vert[i]+displacement[i]
    # I now set the object's PointCloud rather than modify it directly so the new center will be calculated every time
    object.setPointCloud(pccopy)


# This function performs a simple uniform scale of an object assuming the object is
# centered at the origin.  The scalefactor is a scalar.
def scale(object,scalefactor):
    pccopy = copy.deepcopy(object.getPointCloud())
    for x in pccopy:   #loop through each point in the point cloud
        for i in range(0,len(x)-1):    #loop through each coordinate in the point and scale
            x[i] = x[i]*scalefactor[i]
    object.setPointCloud(pccopy)


# This function performs a rotation of an object about the Z axis (from +X to +Y)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CCW
# in a LHS when viewed from -Z [the location of the viewer in the standard position]
def rotateZ(object,degrees):
    pccopy = copy.deepcopy(object.getPointCloud())
    for vert in pccopy:
        angle = degrees*(3.141592654)/180
        x = vert[0]
        y=vert[1]
        vert[0] = x * math.cos(angle) - y*math.sin(angle)
        vert[1] = x * math.sin(angle) + y * math.cos(angle)
    object.setPointCloud(pccopy)


# This function performs a rotation of an object about the Y axis (from +Z to +X)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +Y looking toward the origin.
def rotateY(object,degrees):
    pccopy = copy.deepcopy(object.getPointCloud())
    for vert in pccopy:
        angle = degrees*(3.141592654)/180
        x = vert[0]
        z = vert[2]
        vert[0] = x * math.cos(angle) + z*math.sin(angle)
        vert[2] = -x * math.sin(angle) + z * math.cos(angle)
    object.setPointCloud(pccopy)


# This function performs a rotation of an object about the X axis (from +Y to +Z)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +X looking toward the origin.
def rotateX(object,degrees):
    pccopy = copy.deepcopy(object.getPointCloud())
    for vert in pccopy:
        angle = degrees*(3.141592654)/180
        y = vert[1]
        z = vert[2]
        vert[1] = y * math.cos(angle) - z*math.sin(angle)
        vert[2] = y * math.sin(angle) + z * math.cos(angle)
    object.setPointCloud(pccopy)


# The function will draw an object by repeatedly calling drawPoly on each polygon in the object
# I now have a color parameter because different objects are drawn with different colors depending on toggle
def drawObject(object,color):
    for x in object:
        drawPoly(x,color)


# This function will draw a polygon by repeatedly calling drawLine on each pair of points
# making up the object.  Remember to draw a line between the last point and the first.
def drawPoly(poly,color):
    for i in range(0, len(poly)-1):
       drawLine(poly[i],poly[i+1], color)
    drawLine(poly[len(poly)-1], poly[0],color)



# Project the 3D endpoints to 2D point using a perspective projection implemented in 'project'
# Convert the projected endpoints to display coordinates via a call to 'convertToDisplayCoordinates'
# draw the actual line using the built-in create_line method
# will draw different objects different colors depending on the toggle
def drawLine(start,end, color):
    #        w.create_line(startdisplay[0],startdisplay[1],enddisplay[0],enddisplay[1])
    startdisplay = convertToDisplayCoordinates(project(start)) #convert projected coordinates to display coords
    enddisplay = convertToDisplayCoordinates(project(end)) #convert projected coordinates to display coords
    w.create_line(startdisplay[0], startdisplay[1], enddisplay[0], enddisplay[1], fill=color)


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

# This function draws all objects in the list Shapes with black lines
# Lastly the function draws the selected object with blue lines
def drawAllObjects():
    for object in Shapes:
        drawObject(object.Polys, "black")
    drawObject(selected.Polys, "blue")


# **************************************************************************
# Everything below this point implements the interface

# This function allows the toggle button to cycle through the objects on the screen
def toggle():
    # Rather than passing these through the button line I just called them from the global persepctive
    global selected
    global selectindex
    if selectindex<len(Shapes)-1:
        selected = Shapes[selectindex+1]
        selectindex = selectindex+1
    else:
        selected = Shapes[0]
        selectindex = 0
    w.delete(ALL)
    drawAllObjects()

# the new reset function for the reset button now utilizes the built in resets for the objects using the object class
# it also uses the new function drawAllObjects()
def reset():
    w.delete(ALL)
    selected.resetObject()
    drawAllObjects()

# we now have in place size increases
def larger():
    w.delete(ALL)
    displacement = copy.deepcopy(selected.CP)
    translate(selected,[-displacement[0],-displacement[1],-displacement[2]])
    scale(selected,[1.1,1.1,1.1])
    translate(selected, [displacement[0], displacement[1], displacement[2]])
    drawAllObjects()


# we now have in place size decreases
def smaller():
    w.delete(ALL)
    displacement = copy.deepcopy(selected.CP)
    translate(selected, [-displacement[0], -displacement[1], -displacement[2]])
    scale(selected,[.9,.9,.9])
    translate(selected, [displacement[0], displacement[1], displacement[2]])
    drawAllObjects()


def forward():
    w.delete(ALL)
    translate(selected,[0,0,5])
    drawAllObjects()


def backward():
    w.delete(ALL)
    translate(selected,[0,0,-5])
    drawAllObjects()

def left():
    w.delete(ALL)
    translate(selected,[-5,0,0])
    drawAllObjects()

def right():
    w.delete(ALL)
    translate(selected,[5,0,0])
    drawAllObjects()

def up():
    w.delete(ALL)
    translate(selected,[0,5,0])
    drawAllObjects()

def down():
    w.delete(ALL)
    translate(selected,[0,-5,0])
    drawAllObjects()

# we now have in place rotations in x y and z
def xPlus():
    w.delete(ALL)
    displacement = copy.deepcopy(selected.CP)
    translate(selected,[-displacement[0],-displacement[1],-displacement[2]])
    rotateX(selected,5)
    translate(selected, [displacement[0], displacement[1], displacement[2]])
    drawAllObjects()

def xMinus():
    w.delete(ALL)
    displacement = copy.deepcopy(selected.CP)
    translate(selected, [-displacement[0], -displacement[1], -displacement[2]])
    rotateX(selected, -5)
    translate(selected, [displacement[0], displacement[1], displacement[2]])
    drawAllObjects()

def yPlus():
    w.delete(ALL)
    displacement = copy.deepcopy(selected.CP)
    translate(selected, [-displacement[0], -displacement[1], -displacement[2]])
    rotateY(selected, 5)
    translate(selected, [displacement[0], displacement[1], displacement[2]])
    drawAllObjects()

def yMinus():
    w.delete(ALL)
    displacement = copy.deepcopy(selected.CP)
    translate(selected, [-displacement[0], -displacement[1], -displacement[2]])
    rotateY(selected, -5)
    translate(selected, [displacement[0], displacement[1], displacement[2]])
    drawAllObjects()

def zPlus():
    w.delete(ALL)
    displacement = copy.deepcopy(selected.CP)
    translate(selected, [-displacement[0], -displacement[1], -displacement[2]])
    rotateZ(selected, 5)
    translate(selected, [displacement[0], displacement[1], displacement[2]])
    drawAllObjects()

def zMinus():
    w.delete(ALL)
    displacement = copy.deepcopy(selected.CP)
    translate(selected, [-displacement[0], -displacement[1], -displacement[2]])
    rotateX(selected, -5)
    translate(selected, [displacement[0], displacement[1], displacement[2]])
    drawAllObjects()

root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
drawAllObjects()
w.pack()

controlpanel = Frame(outerframe)
controlpanel.pack()

togglecontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
togglecontrols.pack(side=LEFT)

togglecontrolslabel = Label(togglecontrols, text="Toggle Shapes")
togglecontrolslabel.pack()

toggleButton = Button(togglecontrols, text="Click To Toggle", fg="green", command=toggle)
toggleButton.pack(side=LEFT)

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
