## Objective
This project is designed to familiarize you with the basics of creating transformation matrices and a matrix stack. The goal of this project is to learn the underlying techniques used in a graphics library that is similar in design to OpenGL. In particular, you will implement transformation, projection, and mapping to the screen of user-provided lines. You will test out your code with the help of the provided routines for drawing a few simple images. You will also create a routine that draws your initials on the screen in perspective.

## Project Description
As stated in the project objective, you will be implementing a basic graphics library that is similar in style to the popular openGL library. Part of these routines are the ones that you wrote for Project 1A. The following routines should act as they did in that earlier project:

`gtInitialize()`

`gtPushMatrix(), gtPopMatrix()`

`gtTranslate(x, y, z)`

`gtScale(sx, xy, sz)`

`gtRotateX(theta), gtRotateY(theta), gtRotateZ(theta)`

You will also implement several new routines which allow a user to manipulate and display 3D lines. The provided source code contains empty methods for each of the following routines:

`gtOrtho(left, right, bottom, top, near, far)`

Specifies that an orthographic projection will be performed on subsequent vertices. The direction of projection is assumed to be along the z-axis. The six values passed to this routine describe a box to which all lines will be clipped. The “left” and “right” values specify the minimum and maximum x values that will be mapped to the left and right edges of the framebuffer. The “bottom” and “top” values specify the y values that map to the bottom and top edges of the framebuffer. The “near” and “far” values are ignored for this project. The eye point is assumed to be facing the negative z-axis.

`gtPerspective(fov, near, far)`

Specifies that a perspective projection will be performed on subsequent vertices. The center of projection is assumed to be the origin, and the viewing direction is along the negative z-axis. The value “fov” is an angle (in degrees) that describes the field of view. In order to make it easier to write this routine, we will assume that all screen sizes will be square, so you don't need to worry about the vertical and horizontal field-of-view being different. The “near” and “far” values are ignored for this project.

In OpenGL, you can specify projections at any time before you draw lines and polygons. We will do the same for our assignment. Which ever projection that you specify (gtOrtho or gtPerspective) should be the last operation that is applied to the line endpoints, regardless of where those procedure calls appear with respect to the other transformations.

`gtBeginShape(), gtEndShape(), gtVertex(x, y, z)`

The `gtBegin` and `gtEnd` commands signal the start and end of a list of endpoints for line segments that are to be drawn. Each call to the routine gtVertex between these two commands specifies a 3D vertex that is a line endpoint. Black lines are drawn between successive odd/even pairs of these vertices. If, for example, the four vertices v1, v2, v3, v4 are given in four sequential gtVertex commands then two line segments will be drawn, one between v1 and v2 and another between v3 and v4.

The vertices of the lines are first modified by the current transformation matrix, and then by which ever projection was most recently described (`gtOrtho` or `gtPerspective`). Only one of `gtOrtho` or `gtPerspective` is in effect at any one time. These projections do not affect the matrix stack and the current transformation matrix! Your gtBegin, gtVertex and gtEnd commands must be able to draw any number of lines. You can draw the lines as soon as both vertices are given to you (using `gtVertex`), or you can store all of the vertices and draw all of the lines when gtEnd is called. Which way you use is up to you. To draw the lines, use the built-in `line()` routine in Processing.

## Provided Code
The provided source code contains various routines to draw a few simple images. Upon running the program, these supplied set of routines can be called with the number keys (0-9). You will use these test cases to debug and validate your library routines.

Pressing the ‘1’ key will call the first test case to draw a square on the screen. This test function should be used to test out your gtOrtho routine. Pressing keys ‘2’ and higher will test out more of the routines that you should provide.

The ‘0’ key will run a routine called persp_initials(). In this routine, you should write a set of commands to draw your initials on the screen, using the commands that you have created (gtPerspective(), gtBeginShape(), gtVertex(), and so on). That is, you should draw the first letters of your personal and family name. You must use perspective projection, and you also make it obvious that your initials are being drawn in perspective.  There are two ways in which you can clearly demonstrate that your initials are being shown in perspective.  One way is to tilt the letters so that parallel lines in the letters are no longer parallel, due to perspective foreshortening.  Greg did this for his initials GT in the example shown below.  Another way is to extend each of the line segments that make up letters in the z direction, using quadrilaterals or cubes. You can be as simple or as elaborate as you like in drawing your initials, so long as these letters can be correctly identified and so that they clearly demonstrate perspective.

You should modify the source code in the drawlib and initials tabs, and include your name in the header. The source code is written in Python Processing. Visit “py.processing.org/reference/” for more information on built in functions and structure. Please not that you are not allowed to use the built-in matrix stack and transformation functions in Processing to accomplish the tasks for this project. The only built-in drawing routine that you should use in your code is line(). When in doubt about what you are allowed to use, ask.

Note that your instructor strongly recommends that you do not use matrices to implement orthographic projection, perspective projection, and mapping to the screen.  Our textbook demonstrates doing these steps with matrices, but there are several potential pitfalls with this approach.  You are more likely to be successful if you make use of the techniques that we went over in class for these operations.

## Suggested Approach
You should decide for yourself whether you need suggestions for the project, or whether you know how to proceed on your own.  The choice is yours!

Your first goal should be to draw the square that is shown when you press the '1' key.  For this, you will need to implement the gtOrtho() command, as well as gtBeginShape(), gtEndShape() and gtVertex().  Notice that this example does not require using the current transformation matrix. You should definitely feel free to save various values in one or more global variables.  When the user calls the gtVertex() command, you should store the coordinates that are passed to this function. When the gtOrtho() command is called, you should store the values of left, right, bottom, top, near, and far.  You should also use a variable to record that subsequent drawing commands should will use orthographic projection, not perspective.

There are two straightforward approaches to drawing lines. One way is for you to store the first vertex, and then draw the line when you are given the second vertex, and then repeat this for subsequent pairs of lines.  Another approach is for you to store all of the vertices that are defined, and then draw all of the lines when the gtEndShape() function is called.  Either approach is fine.

After you have implemented and tested gtOrtho() for the first example, then you should have the current transformation matrix affect the positions of the points given in gtVertex().  For key press '2', the vertices of the square are affected by the non-uniform scale that is called before the square is drawn. Note that the vertices that are the endpoints of the lines should first be modified by the current transformation, and then modified by the current projection (orthographic or perspective).

Once all of the orthographic projection examples are working, you should implement gtPerspective(). Just like with gtOrtho(), the perspective command should store the field of view, near, and far.  You should also use a variable value to indicate that when lines are drawn, they will be drawn in perspective.  Then modify your line drawing routines so that they properly handle both the orthographic and perspective cases.

## Write Your Own Projection Routines

Please note that you are not allowed to use built-in graphics functions to accomplish the tasks listed in the project description. Just like for Project 1A, you cannot use the built-in matrix and vector data types, the transformation functions (scale, translate, rotate), or the push and pop functions that are provided by Processing. You also cannot use the built-in routines for ortho, perspective, beginShape, endShape, or vertex. It is fine for you to use any of the built-in math functions such as cos(), sin(), tan(), sqrt(), pow() and so on.  When in doubt about what Processing routines you may use, ask.

## Processing Versions
Students in the class have had mixed results when using the latest version of Processing (4.0.1).  If you have trouble using the most recent version, you should download and use the previous version, 3.5.4.  If you still have problems using the Python version of Processing, seek the help of the TA's.

## Authorship Rules
The code that you turn in entirely your own. You are allowed to talk to other members of the class and to the instructor and the TA’s about general implementation of the assignment. It is also fine to seek the help of others for general Python Processing programming questions. You may not, however, use code that anyone other than yourself has written. The only exception is that you should use the source code that we provide for this project, and the code that you wrote for Project 1A. Code that is explicitly not allowed includes code taken from other students, the Web, github, from books, from other assignments or from any source other than yourself. You should not show your code to other students. Feel free to seek the help of the instructor and the TA's for suggestions about organizing and debugging your code.

## Submission
In order to run the source code, it must be in a folder named after the main .pyde file. When submitting any assignment, leave it in this folder, zip it and submit via Canvas.  Please do not use tar or rar to turn in your files.

## Results
Below are the results that your program should draw when you press the 1-9 and the 0 keys.  Note that you will use your own initials for the final image, and you must clearly demonstrate that this image was created using perspective projection.

