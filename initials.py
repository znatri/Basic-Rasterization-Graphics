# The routine below should draw your initials in perspective

from matrix_stack import *
from drawlib import *

def persp_initials():
    gtInitialize()
    gtOrtho (-100, 100, -100, 100, -100, 100)
    gtPerspective(60, -100, 100)
    gtPushMatrix()
    gtTranslate(0, 0, -4)
    H()
    G()
    gtPopMatrix()


def J():
    gtBeginShape()
    # Front J
    gtVertex(-.5,  1.0,  1.0)
    gtVertex( .5,  1.0,  1.0)

    gtVertex(0, 1.0, 1.0)
    gtVertex(0, 0, 1)
    
    gtVertex(0, 0, 1)
    gtVertex(-.9,0, 1)
    
    gtVertex(-.9,0, 1)
    gtVertex(-.9,.25,1)
    # Back J
    gtVertex(-.5,  1.0,  .7)
    gtVertex( .5,  1.0,  .7)

    gtVertex(0, 1.0, .7)
    gtVertex(0, 0, .7)
    
    gtVertex(0, 0, .7)
    gtVertex(-.9,0, .7)
    
    gtVertex(-.9,0, .7)
    gtVertex(-.9,.25,.7)

    gtEndShape()

def G():
    gtBeginShape()
    gtVertex (0.25, -0.50, -0.5)
    gtVertex (0.75, -0.50, -0.5)
    
    gtVertex (0.25, -0.50, -0.5)
    gtVertex (0.25, 0.50, 0.5)
    
    gtVertex (0.25, 0.50, 0.5)
    gtVertex (0.75, 0.50, 0.5)
    
    gtVertex(0.75, 0, 0.1)
    gtVertex(0.75, -0.70, 0.6)
    
    gtVertex(0.45, 0, 0.1)
    gtVertex(0.75, 0, 0.1)
    gtEndShape()
    

def H():
    gtBeginShape()
    gtVertex (-0.75, -0.5, -0.5)
    gtVertex (-0.75, 0.50, 0.5)
    
    gtVertex (-0.25, -0.50, -0.5)
    gtVertex (-0.25, 0.50, 0.5)
    
    gtVertex (-0.75, 0, 0.1)
    gtVertex (-0.25, 0, 0.1)
    gtEndShape()
