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
        startdisplay = convertToDisplayCoordinates(project(start))  # convert projected coordinates to display coords
        enddisplay = convertToDisplayCoordinates(project(end))  # convert projected coordinates to display coords
        w.create_line(startdisplay[0], startdisplay[1], enddisplay[0], enddisplay[1])
        print("drawLine stub executed.")

    # This function converts from 3D to 2D (+ depth) using the perspective projection technique.  Note that it
    # will return a NEW list of points.  We will not want to keep around the projected points in our object as
    # they are only used in rendering
    def project(point):
        ps = [0, 0, 0]  # initialize the coordinates
        ps[0] = (-d) * point[0] / ((-d) + point[2])  # project the x-component
        ps[1] = (-d) * point[1] / ((-d) + point[2])  # project the y-component
        ps[2] = point[2] / ((-d) + point[2])  # project the z component
        return ps

    # This function converts a 2D point to display coordinates in the tk system.  Note that it will return a
    # NEW list of points.  We will not want to keep around the display coordinate points in our object as
    # they are only used in rendering.
    def convertToDisplayCoordinates(point):
        displayXY = [0, 0]  # initialize the coordinates
        displayXY[0] = point[0] + 200  # x - component shift 200 pixels since size is 400x400 for graphing
        displayXY[1] = -point[
            1] + 200  # make negative since down is positive in tkinter then create y - component shift for graphing
        return displayXY

