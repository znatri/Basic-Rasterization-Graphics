# Drawing Routines that are similar to those in OpenGL

from matrix_stack import *
import math

class Vertex():
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def getCoords(self):
        return [self.x, self.y, self.z, 1.0]
    

class defaultProjection():
    def __init__(self):
        self.type = 0
        
    def getType(self):
        return self.type
    

class OrthogonalProj():
    def __init__(self, left, right, bottom, top, near, far):
        self.left = float(left)
        self.right = float(right)
        self.bottom = float(bottom)
        self.top = float(top)
        self.near = float(near)
        self.far = float(far)
        self.method = 1   
   
    def left(self):
        return self.left
   
    def right(self):
        return self.right
   
    def bottom(self):
        return self.bottom
   
    def top(self):
        return self.top
    
    def near(self):
        return self.near
    
    def far(self):
        return self.far
   
    def getType(self):
        return self.method 

    
class Perspective():
    def __init__(self, fov, near, far):
        self.fov = float(fov)
        self.near = float(near)
        self.far = float(far)
        self.method = int(2)
        
    def fov(self):
        return self.fov
    
    def near(self):
        return self.near
    
    def far(self):
        return self.far
        
    def getType(self):
        return self.method

points = []
startStatus = False
views =  defaultProjection()

def gtOrtho(left, right, bottom, top, near, far):
    global views
    views = OrthogonalProj(left, right, bottom, top, near, far)

def gtPerspective(fov, near, far):
    global views
    views = Perspective(fov, near, far)

def gtVertex(x, y, z):
    global startStatus
    
    if startStatus:
        if len(points) == 0:
            points.append(Vertex(x, y, z))
            
        else:
            coord1 = points.pop().getCoords()
            coord2 = Vertex(x, y, z).getCoords()
            ctm = stack.peek()
            ptA = crossProduct(ctm, coord1)
            ptB = crossProduct(ctm, coord2)
            
            if views.method == 1:
                x1 = (ptA[0] - views.left) * (width / (views.right - views.left))
                y1 = (ptA[1] - views.top) * (height / (views.bottom - views.top)) 
                x2 = (ptB[0] - views.left) * (width / (views.right - views.left))
                y2 = (ptB[1] - views.top) * (height / (views.bottom - views.top))
                
            elif views.method == 2:
                f = math.tan(math.radians(views.fov)/ 2)
                x1 = ((ptA[0] / -abs(ptA[2])) + f) * (width / (2 * f))
                y1 = height - ((ptA[1] / abs(ptA[2])) + f) * (height / (2 * f))
                x2 = ((ptB[0] / -abs(ptB[2])) + f) * (width / (2 * f))
                y2 = height - ((ptB[1] / abs(ptB[2])) + f) * (height / (2 * f))
    
            line(x1, y1, x2, y2)
    
def gtBeginShape():
    global startStatus
    if not startStatus:
        startStatus = True

def gtEndShape():
    global startStatus
    if startStatus:
        startStatus = False
        
def crossProduct(ctm, x):
    result = []
    for row in ctm:
        sum = 0
        for i in range(len(x)):
            sum += row[i] * x[i]
        result.append(sum)
    return result
            
