# PaintProgram.py
# Created by Seel Patel

# IMPORTS
# External Modules
from pygame import *
from math import sqrt # For use in creating the spray paint tool in a circle
# for creating importing/exporting dialog boxes
from tkinter import *
from tkinter import filedialog
# Also mainly used for the spraypaint tool
from random import randint
#Used to center main window and splashscreen
from os import environ

# imports from my other files
from otherFunctions import errorMsg
from interfaceFunctions import *

#END IMPORTS

#Create and remove main Tkinter window so it doesnt always stay on screen and doesnt appear when creating file dialogs
root = Tk()
root.withdraw()
"""
try:
    #Play the background music
    #mixer.init() #Initialize the music system
    #mixer.music.load("Extra/backgroundMusic.mp3") #Select/load music file
    #mixer.music.set_volume(1) # Set the volume of the music
    #mixer.music.play(-1) # Set the music on an unlimited loop
except:
    pass
    errorMsg("Unable to begin Music")
"""
#Print out introductory text and shortcut keys
print("Welcome to Seel's Paint Program\nTheme is based off of Spongebob\n\nKEYBOARD SHORTCUTS:\n\nBrush: B\nPencil: P\nShapes: S\nEraser: E\nColor Chooser: D\nUndo: Z\nRedo: Y\nOpen: O\nFill: F\nSwitch primary and secondary colors: Right-Click")

# Initiilze pygame and check for proper startup. Print error if it doesnt work
if init() != (6, 0):
    errorMsg("Pygame could not initialized")
    exit()

# Define Preset Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#
# SPLASH SCREEN / LOADING SCREEN
# The screen is actually used to load things such as images and canvases

environ['SDL_VIDEO_CENTERED'] = '1'  # Used to make sure the main window and splashscreen are centered in the display
splashScreenImage = image.load("Images/BackgroundPictures/splashScreenImage.png")  # Load the splash screen image
splashScreen = display.set_mode((800, 450),
                                NOFRAME)  # Set the display size to splashscreen size and remove window borders
splashScreen.blit(splashScreenImage, (0, 0))  # Blit the splashscreen image to the screen
display.flip()  # display what was blitted to the display

# Init the fonts for the interface functions and main file. This allows the use of fonts
initFont()

#Main font for the program and loading screen
arialFont = font.SysFont("Arial", 14)

for loadPeriod in range(5): # Start the splashscreen loading process
    if loadPeriod == 0: #Load stamps if in the first load period
        try:
            #stamps
            stamp1Image = image.load("Images/Stamps/stamp1.jpg")
            stamp2Image = image.load("Images/Stamps/stamp2.png")
            stamp3Image = image.load("Images/Stamps/stamp3.png")
            stamp4Image = image.load("Images/Stamps/stamp4.svg")
            stamp5Image = image.load("Images/Stamps/stamp5.png")
            stamp6Image = image.load("Images/Stamps/stamp6.png")
            stamp7Image = image.load("Images/Stamps/stamp7.svg")
            stamp8Image = image.load("Images/Stamps/stamp8.svg")
            stamp9Image = image.load("Images/Stamps/stamp9.png")
            stamp10Image = image.load("Images/Stamps/stamp10.png")
        except:
            errorMsg("Ran into problem loading stamps") #If loading stamps doesnt work, create and error message
        # Write loading text
        displayText = arialFont.render("Loading Stamps...", True, (70, 190, 214))
        splashScreen.blit(displayText, (355, 400))

    elif loadPeriod == 1: #Load tool images in the second loading period
        # load Tool Images
        try:
            # Load the main tool images
            pencilToolImage = image.load("Images/ToolPictures/pencilTool.png")
            eraserToolImage = image.load("Images/ToolPictures/eraserTool.png")
            backFillToolImage = image.load("Images/ToolPictures/backfillTool2.png")
            highlighterToolImage = image.load("Images/ToolPictures/highlighterTool.png")
            sprayToolImage = image.load("Images/ToolPictures/spraypaintTool.png")
            stampToolImage = image.load("Images/ToolPictures/stampTool.png")
            zoomToolImage = image.load("Images/ToolPictures/zoomTool.png")
            brushToolImage = image.load("Images/ToolPictures/brushTool.png")
            dropperToolImage = image.load("Images/ToolPictures/dropperTool.png")
            textToolImage = image.load("Images/ToolPictures/textTool.png")

            fillToolImage = image.load("Images/ToolPictures/fillTool.png")

            openToolImage = image.load("Images/ToolPictures/openTool.png")
            saveToolImage = image.load("Images/ToolPictures/saveTool.png")

            copyPasteImage = image.load("Images/ToolPictures/copyPaste.png")

            undoToolImage = image.load("Images/ToolPictures/undoTool.png")
            redoToolImage = image.load("Images/ToolPictures/redoTool.png")

            changeAccentColorImage = image.load("Images/ToolPictures/changeAccentColor.png")

            # Load the brush/zoom size button images
            brushSize2Image = image.load("Images/ToolPictures/brushSize2.png")
            brushSize5Image = image.load("Images/ToolPictures/brushSize5.png")
            brushSize10Image = image.load("Images/ToolPictures/brushSize10.png")
            brushSize20Image = image.load("Images/ToolPictures/brushSize20.png")
            brushSize30Image = image.load("Images/ToolPictures/brushSize30.png")

            #Load the images for the shape tools
            shapeFilledImage = image.load("Images/ToolPictures/ShapeTools/shapeFilled.png")
            shapeEmptyImage = image.load("Images/ToolPictures/ShapeTools/shapeEmpty.png")

            shapeToolImage = image.load("Images/ToolPictures/ShapeTools/shapesImage.png")
            circleToolImage = image.load("Images/ToolPictures/ShapeTools/circleTool.png")
            rectangleToolImage = image.load("Images/ToolPictures/ShapeTools/rectangleTool.png")
            triangleToolImage = image.load("Images/ToolPictures/ShapeTools/triangleTool.png")
            ellipseToolImage = image.load("Images/ToolPictures/ShapeTools/ellipseTool.png")
            lineToolImage = image.load("Images/ToolPictures/ShapeTools/lineTool.png")
            polygonToolImage = image.load("Images/ToolPictures/ShapeTools/polygonTool.png")


        except:
            errorMsg("Ran into problem importing tool images") # Create error message if loading the images from above fails

        # Write Loading text
        splashScreen.blit(splashScreenImage, (0, 0)) # Overwrite the previous screen
        displayText = arialFont.render("Loading Tool Images...", True, (70, 190, 214))
        splashScreen.blit(displayText, (355, 400))

    elif loadPeriod == 2:
        # Load canvases for Color Palette
        initBlackGradient() # initialize black gradient
        setPalettePos(910, 25) #Set Palette Position on screen

        # Write loading text
        splashScreen.blit(splashScreenImage, (0, 0)) # Overwrite the previous screen
        displayText = arialFont.render("Loading Palette...", True, (70, 190, 214))
        splashScreen.blit(displayText, (355, 400))

    elif loadPeriod == 3:
        try:
            # Load background images
            backgroundImage = image.load("Images/BackgroundPictures/SpongeBobBackground2.png")
            houseBackgroundImage = image.load("Images/BackgroundPictures/houseBackground.png")
            krustyKrabBackgroundImage = image.load("Images/BackgroundPictures/krustyKrabBackground.jpg")
            simpleBackgroundImage = image.load("Images/BackgroundPictures/simpleBackground.jpg")
            stageBackgroundImage = image.load("Images/BackgroundPictures/stageBackground.jpg")
            themeLogoImage = image.load("Images/BackgroundPictures/themeLogo.png")
        except:
            errorMsg("Problem loading background images") # Error Message of loading background images fails
            pass

        # Write loading text
        splashScreen.blit(splashScreenImage, (0, 0)) # Overwrite the previous screen
        displayText = arialFont.render("Loading backgrounds...", True, (70, 190, 214))
        splashScreen.blit(displayText, (355, 400))

    elif loadPeriod == 4:
        #fonts
        comicSans = font.SysFont("Comic Sans", 14)

        # Write loading text
        splashScreen.blit(splashScreenImage, (0, 0)) # Overwrite the previous screen
        displayText = arialFont.render("Loading Fonts...", True, (70, 190, 214))
        splashScreen.blit(displayText, (355, 400))

    display.flip() # Copy everything blitted to the display at the end of every load cycle
    time.delay(500) # Add slight delay so loading can be seen

# Define the window size
size = (1200, 600)

# VARIABLES and small setup
# Colors
backgroundColor = WHITE
mainColor = BLUE
secondaryColor = RED
swatchesColor = (255, 0, 0)

#Temporary color variable used to store main color when changing the interface accent color
tempColor = BLUE

#Set the color and outlien color of the button
setButtonColor(WHITE)
setButtonOutline(interfaceAccentColor)

# Used to check if the accent color is being changed
changingAccentColor = False

# Rects
canvasRect = Rect(350, 30, 500, 500) # Rect for canvas

# Surfaces
canvas = Surface((canvasRect[2], canvasRect[3])) #Actual canvas on which everything is drawn
canvas.fill(WHITE) #Fill the canvas white at the start
backgroundCanvas = Surface((canvasRect[2], canvasRect[3]))
backgroundCanvas.fill(WHITE)

addUndo(canvas.copy()) #Begin the undolist by adding the blank canvas

screenCopy = canvas.copy() #Create the screen copy variable

#Create a tool holder area for the tools which is drawn during every main loop iteration
toolPalette = Surface((125,450))
toolPalette.fill(WHITE)
draw.rect(toolPalette,interfaceAccentColor,[0,0,125,450],1)

# Tool Varibles
tool = "pencil" #Store which tool is currently selected
toolSize = 20 #Used to store size of freehand tools

#Shape tool variables
fillToggle = False # Used to check if shapes should be filled or not
shapeThickness = 3 # By default it is 3 but if filled it is changed to 0 if filled

#Text tool variables
textString = "" # String to store text for text tool
writingText = False # Tells program if text is being written for the text tool
pressedKey = None # Store the pressed key converted from ascii for the text tool
pressedKeyAscii = None #Store the pressed key not converted from ascii for the text tool
keyPressed = False # Check if a key has been pressed for the text tool
keysHeld = [] #gets keys being pressed down currently (ex shift)
shiftHeld = False #indicates if shift key is held

#Polygon tool variables
makingPolygon = False # Tells program if the user is currently making a polygon
polygonPointList = [] # Stores all the points for the polygon

#Variables for importing an image
placingImportedImage = False # Checks if the imported image is being placed on screen
importImg = None #Stores the imported image
imgHeight = 0 #varibles for image height and width
imgWidth = 0

#Varibles for copy and pasting area
selectingArea = False # varible to indicate if selecting an area
copySurface = Surface((0,0)) # Surface for copied surface

#Zoom tool
zoomAmount = 50 # The amount the user is zooming in to the screen. Lower is closer

# VARIABLE END

# Set the screen
screen = display.set_mode(size) #Set display size/mode
display.set_caption("PaintProgram")  # Set the display caption

running = True # Set the running variable True which will let the program enter the main loop

screen.fill(WHITE)  # Set window color to white initially

#screen.blit(backgroundImage, (0, 0)) #Blit the background image to the screen
#screen.blit(transform.smoothscale(themeLogoImage,(250,150)),(905,410)) #Blit a logo based off the theme to the screen

myClock = time.Clock()  # Create clock for tick management

initRangePalette(screen) # Initiialize range palette.
#The initRangePaleete is not up where the initBlackGradient is for an important reason
#Its down here so the range palette can be blitted to the main screen for the first time

mx,my = mouse.get_pos() #Create the mx,my variables and set them to mouse position
clickX = mx
clickY = my

screenCopy = screen.copy() #Create the screen copy variable used mainly by shapes, stamps and text tools

while running: # Enter main loop
    # Get information about the mouse
    omx,omy = mx,my
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    #Find the mx and my point reletive to the top and left side of the canvas. This gives the position of the mouse on the
    c_mx,c_my = mx-350,my-30
    c_omx, c_omy = omx - 350, omy - 30

    #Blit the old screen to the display for the zoom tool so there isnt anything permenantly drawn
    if tool == "zoom":
        screen.blit(screenCopy, (0, 0))

   #DRAW INFO BOX UNDER THE CANVAS
    draw.rect(screen, WHITE, [349, 533, 502, 30], 0)
    draw.rect(screen, interfaceAccentColor, [349, 533, 502, 30], 1)
    #Print out mouse into into the info box under the canvas
    mouseInfo = arialFont.render("Mouse: " + str(mouse.get_pos()) + "   Color: " + str(screen.get_at((mx,my))), True, interfaceAccentColor)
    screen.blit(mouseInfo, (605, 538))

    # Send information to interface functions about which tool is selected and the button color
    getTool(tool)
    setButtonOutline(interfaceAccentColor)

    # Draw border around the canvas
    draw.rect(screen, interfaceAccentColor,
              [canvasRect[0] - 1, canvasRect[1] - 1, canvasRect[2] + 2, canvasRect[3] + 2],
              1)

    #### BLIT THE CANVAS DURING EACH ITERATION
    screen.blit(canvas, (canvasRect[0], canvasRect[1]))


    if KMOD_SHIFT and key.get_mods():
        shiftHeld = True #Check if shift Key is pressed and set varible to true if it is
    else:
        shiftHeld = False #Set to false if shift not pressed


    # Use a loop to iterate through user input events
    for evt in event.get():
        if evt.type == QUIT: # If the close button is pressed, close the program
            running = False

        elif evt.type == MOUSEBUTTONDOWN: #Deal with all input events that involve the mouse button being pushed/scrolled
            if mouse.get_pressed()[0] == 1: #If the left click is pressed

                #Get initial click position and a screen copy for use in the shape tools and the stamp tool
                if tool == "rectangle" or tool == "ellipse" or tool == "circle" or tool == "triangle" or tool == "line" or "stamp" in tool:
                    screenCopy = canvas.copy()
                    clickX, clickY = c_mx, c_my

                if tool == "selectArea" and selectingArea:
                    screenCopy = canvas.copy()
                    clickX, clickY = c_mx, c_my


                #If your are not writing text and th text tool is selected this allows you to begin
                if tool == "text" and canvasRect.collidepoint(mx,my) and writingText == False:
                    textString = "" #Set the string for the text to blank
                    screenCopy = canvas.copy() #get a screen copy to cover what was blitted during previous iterations
                    clickX, clickY = c_mx, c_my #Get the click point relative to inside the canvas where the text will be written
                    writingText = True # Indicate to other parts of the program that your are writing text

                #Start drawing a polygon if not already drawing one
                elif tool == "polygon" and makingPolygon == False and canvasRect.collidepoint(mx,my):
                    screenCopy = canvas.copy() #get a screen copy to cover what was blitted during previous iterations
                    makingPolygon = True # indicate to program that polygon is being drawn
                    polygonPointList = [] # Set polygon point list as blank
                    polygonPointList.append([c_mx,c_my]) #Add initial click point to the point list

                #Add to polygon pointlist if you click on the canvas while makingPolygon is true.
                elif makingPolygon and tool == "polygon" and canvasRect.collidepoint(mx,my):
                    polygonPointList.append([c_mx,c_my])

                elif tool == "fill" and canvasRect.collidepoint(mx,my):
                    try:
                        rc = canvas.get_at((c_mx, c_my))  # gets the colour of pixel where the user clicked
                        spots = [(c_mx, c_my)]  # the point clicked is part of the spots list
                        newSpots = []
                        while len(spots) > 0:  # when the spots list has at least one element
                            newSpots = []  # list of new spots
                            for fx, fy in spots:
                                if 0 < fx < 500 and 0 < fy < 500 and canvas.get_at(
                                        (fx, fy)) == rc:  # if fx and fy are within the range of the canvas
                                    canvas.set_at((fx, fy),
                                                  mainColor)  # and the colour of the pixel of fx,fy is the same colour as

                                    # right    #left      #down    #up
                                    newSpots += [(fx + 1, fy), (fx - 1, fy), (fx, fy + 1),
                                                 (fx, fy - 1)]  # these are the 4 points we fill
                                    # from the initial point
                                spots = newSpots  # each time, from the newSpots, they become spots and the right, left, up and down of
                                # these points are counted as newSpots and we colour in those pixels
                    except MemoryError:
                        pass


            #Switch the primary and secondary colors if right clicked
            elif mouse.get_pressed()[2] == 1:
                temp = secondaryColor
                secondaryColor = mainColor
                mainColor = temp

            elif evt.button == 4:  # check if scrolling up
                #Change Zoom and Tool Size values depending on what tool is selected
                if tool == "pencil" or tool == "eraser" or tool == "colorEraser" or tool == "spray" or tool == "highlighter" or tool == "brush":
                    toolSize += 1
                    if toolSize > 200: # Set size limits for the variables
                        toolSize = 200 #change size of tools if scrolling

                elif tool == "zoom":
                    zoomAmount+=1
                    if zoomAmount > 100: # Set size limits for the variables
                        zoomAmount = 100 # change zoom distence if scrolling
            elif evt.button == 5:  # check if scrolling down
                # Change Zoom and Tool Size values depending on what tool is selected
                if tool == "pencil" or tool == "eraser" or tool == "colorEraser" or tool == "spray" or tool == "highlighter" or tool == "brush":
                    toolSize -= 1
                    if toolSize <= 0: # Set size limits for the variables
                        toolSize = 1

                elif tool == "zoom":
                    zoomAmount-=1
                    if zoomAmount <=5: # Set size limits for the variables
                        zoomAmount = 5

            if tool == "pencil" or tool == "zoom" or tool == "eraser" or tool == "brush" or tool == "colorEraser" or tool == "spray" or tool == "highlighter" or tool == "fill" and canvasRect.collidepoint(mx,my):
                addUndo(canvas.copy()) #add to undoList if above tools are pressed

            if placingImportedImage:
                placingImportedImage = False #if mouse clicked when placing image then stop placing and add to undoList
                addUndo(canvas.copy())

        elif evt.type == MOUSEBUTTONUP:
            if tool == "zoom":
                screen.blit(screenCopy,(0,0))#Blit screen copy when done zooming

            if "stamp" in tool or tool == "rectangle" or tool == "ellipse" or tool == "triangle" or tool == "circle" or tool == "line" and canvasRect.collidepoint(mx,my):
                addUndo(canvas.copy()) # if mouse button is lifted when using above tools, add to undoList

            if selectingArea and tool == "selectArea" and canvasRect.collidepoint(mx,my):
                placingImportedImage = True
                importImg = copySurface
                mouse.set_pos(canvasRect[0],canvasRect[1])
                tool = ""

        elif evt.type == KEYDOWN:
            if tool == "polygon" and evt.key == 13:
                makingPolygon = False
                addUndo(canvas.copy()) #Stop making polygon if enter is pressed and add to undoList
                canvas.blit(screenCopy, (0, 0))  # cover everything from previous iteration
                if len(polygonPointList) == 1:  # draw a dot if there is only one point in the polygon point list
                    draw.line(canvas, mainColor, [polygonPointList[0][0], polygonPointList[0][1]],
                              [polygonPointList[0][0], polygonPointList[0][1]], 1)
                elif len(polygonPointList) == 2:  # draw a line if there is two points in the pointlist
                    draw.line(canvas, mainColor, [polygonPointList[0][0], polygonPointList[0][1]],
                              [polygonPointList[1][0], polygonPointList[1][1]], 3)
                elif len(polygonPointList) > 2:  # If there is more than two points, connect them to draw a polygon
                    draw.polygon(canvas, mainColor, polygonPointList, shapeThickness)

            #if enter is pressed stop writing and add to undoList
            elif tool == "text" and evt.key == 13:
                writingText = False
                textString = ""
                addUndo(canvas.copy())

            elif changingAccentColor and evt.key == 13:
                changingAccentColor = False
                mainColor = tempColor #if enter is pressed when changing accent color. Stop changing it
                canvas.blit(screenCopy, (0, 0))  # cover the previous iteration

                if pressedKeyAscii == K_BACKSPACE:  # if the key is backspace, remove the last character of the textString
                    textString = textString[:-1]
                    canvas.blit(font.SysFont("Arial", 24).render(textString, True, mainColor),
                                (clickX, clickY))  # Blit the new textString to the canvas
                    keyPressed = False  # set key pressed as false foe the next iteration
                elif pressedKeyAscii != 304:  # IF THE INPUTTED KEY ISNT SHIFT
                    if shiftHeld:  # IF SHIFT IS HELD, ADD UPPERCASE LETTERS
                        textString += pressedKey.upper()  # if it is not backspace add the pressed key to the textString
                        canvas.blit(font.SysFont("Arial", 24).render(textString, True, mainColor),
                                    (clickX, clickY))  # Blit the new textString to the canvas
                        keyPressed = False  # set key pressed as false foe the next iteration
                    else:  # If shift not held add lowercase letter
                        textString += pressedKey  # if it is not backspace add the pressed key to the textString
                        canvas.blit(font.SysFont("Arial", 24).render(textString, True, mainColor),
                                    (clickX, clickY))  # Blit the new textString to the canvas
                        keyPressed = False  # set key pressed as false foe the next iteration
                else:  # if none of the conditions met then still write the text out so it doesnt dissappear because of the canvas blitting
                    canvas.blit(font.SysFont("Arial", 24).render(textString, True, mainColor),
                                (clickX, clickY))  # Blit the new textString to the canvas
                    keyPressed = False

            elif tool == "text":
                pressedKey = chr(evt.key)
                pressedKeyAscii = evt.key #varibles used to send the key input to textString when typing text with the text tool
                keyPressed = True

            # Keyboard Shortcuts. Work if your not using the text tool or making the polygon
            if not writingText or not makingPolygon and tool != "text":
                if evt.key == K_z:
                    undo(canvas) #Undo
                if evt.key == K_y:
                    redo(canvas) #Redo
                if evt.key == K_b:
                    tool = "brush" #Set tool to brush
                if evt.key == K_p:
                    tool = "pencil" #set tool to pencil
                if evt.key == K_s:
                    tool = "shapes" #set tool to shapes
                if evt.key == K_e:
                    tool = "eraser" #set tool to eraser
                if evt.key == K_d:
                    tool = "colorChooser" #set tool to color chooser
                if evt.key == K_o: #Open another image
                    try:
                        fname = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.bmp")])
                        importImg = image.load(fname)
                        placingImportedImage = True
                        screenCopy = canvas.copy()
                        tool = ""
                        mouse.set_pos(canvasRect[0], canvasRect[1])
                        Tk.destroy()  # needed or else pygame window cannot be closed after importing or exporting image
                    except:
                        errorMsg("Problem opening image")
                        pass
                if evt.key == K_f:
                    tool = "fill" #set tool to canvas fill

    #Check if canvas is clicked on. Contains most of the tools for the program
    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect) #Makes sure nothing outside the canvas area is altered

        if tool == "pencil": #Use the old mouse position and new mouse position to draw a line for the pencil tool
            draw.line(canvas, mainColor, [c_omx, c_omy], [c_mx, c_my], toolSize//2)

        elif tool == "spray":
            for dots in range(toolSize * 2): #create a number of dots according to the tool size
                randX = randint(-toolSize,toolSize) #Generate random coordinates based on the toolsize range
                randY = randint(-toolSize,toolSize)
                if sqrt(randY**2 +randX**2) < toolSize: #check if it falls within a circle using the circle formula
                    draw.line(canvas,mainColor,[c_mx+randX,c_my+randY],[c_mx+randX,c_my+randY],1) #draw a point if it does
                else:
                    dots -= 1 # if it doesnt then set the loop back an iteration until it does

        elif tool == "brush":
            dx = c_mx - c_omx #Get the difference between the old and new mouse position
            dy = c_my - c_omy
            dist = int(sqrt(dx ** 2 + dy ** 2)) #Get the distence using the distence equation
            for i in range(1, dist + 1): # for ever position in the distence iterate through the loop
                cx = int(c_omx + i * dx / dist)  #Determine the position of the circle for each iteration
                cy = int(c_omy + i * dy / dist)
                draw.circle(canvas, mainColor, [cx, cy], toolSize//4, 0) #Draw a circle at the point determined above

        elif tool == "highlighter":
            if omx!=mx or omy!=my: #Make sure the same point isnt drawn on twice so it doesnt overlap and create a solid color
                highlighterSurface = Surface((500,500),SRCALPHA) #Make highlighter surface that is transparent
                draw.line(highlighterSurface,(mainColor[0],mainColor[1],mainColor[2],75),[c_omx,c_omy],[c_mx,c_my],toolSize) #Draw translucent line on the highlighter surface
                canvas.blit(highlighterSurface,(0,0)) #Blit the highlighter surface to canvas so the opaque highlighter doesnt completely cover whats beneath

        elif tool == "eraser":
            for x in range(-toolSize,toolSize): #Use a nested loop to check area above,below,right and left of the clicked point
                for y in range(-toolSize,toolSize):
                    try:
                         canvas.set_at((c_mx+x,c_my+y),(backgroundCanvas.get_at((c_mx+x,c_my+y))[0],backgroundCanvas.get_at((c_mx+x,c_my+y))[1],backgroundCanvas.get_at((c_mx+x,c_my+y))[2]))
                         # Set the color at the point checked to the value it should be based on the background
                    except IndexError: #If there is an index error and the checking goes off of the canvas then just pass
                        pass

        elif tool == "colorEraser":
            #Check if the area around is the same color as the mainColor
            #If a pixel is the same color, it will be set white / "Erased"
            for x in range(-toolSize,toolSize): #Use a nested loop to check area above,below,right and left of the clicked point
                for y in range(-toolSize,toolSize):
                    try:
                        if canvas.get_at((c_mx+x,c_my+y)) == mainColor: # Checks if the pixel point has the same color as mainColor
                            canvas.set_at((c_mx + x, c_my + y), (backgroundCanvas.get_at((c_mx + x, c_my + y))[0],
                                                                 backgroundCanvas.get_at((c_mx + x, c_my + y))[1],
                                                                 backgroundCanvas.get_at((c_mx + x, c_my + y))[2])) #Set the color at the point checked to the value it should be based on the background
                    except IndexError: #If there is an index error and the checking goes off of the canvas then just pass
                        pass

        elif tool == "colorChooser":
            mainColor = screen.get_at((mx,my))#Get the color at the mouse position
            draw.rect(screen,mainColor,[mx,my-20,20,20],0) #Draw a rect with that color to display it beside the mouse
            draw.rect(screen, BLACK, [mx, my - 20, 20, 20], 1)

        elif tool == "rectangle":
            canvas.blit(screenCopy, (0, 0)) #blit the screen copy to cover the last iteration
            #draw rectangle from original click point to the current mouse position by finding the difference in distence
            draw.rect(canvas, mainColor, [clickX, clickY, c_mx - clickX, c_my - clickY], shapeThickness)

        elif tool == "ellipse":
            canvas.blit(screenCopy, (0, 0))
            try:
                #For each calculate what the top left and bottom right points of the rect will be because it does
                #not behave in the same way as the draw.rect tool.

                #ellipse in the bottom right direction
                if c_mx > clickX and c_my > clickY:
                    draw.ellipse(canvas,mainColor,[clickX,clickY,c_mx-clickX,c_my-clickY],shapeThickness)

                #ellipse in the bottom left direction
                elif c_mx < clickX and c_my > clickY:
                    draw.ellipse(canvas,mainColor,[clickX-(clickX-c_mx),clickY,clickX-c_mx,c_my-clickY],shapeThickness)

                #ellipse in the top left directon
                elif c_mx < clickX and c_my < clickY:
                    draw.ellipse(canvas,mainColor,[c_mx,c_my,clickX-c_mx,clickY-c_my],shapeThickness)

                #ellipse in the top right direction
                elif c_mx > clickX and c_my < clickY:
                    draw.ellipse(canvas,mainColor,[clickX,clickY-(clickY-c_my),c_mx-clickX,clickY-c_my],shapeThickness)

            except: #Pass if there is an error due to the shapeThickness being larger than the radius
                pass

        elif tool == "circle":
            canvas.blit(screenCopy, (0, 0))
            # determine the radius of the circle to make sure shapeThickness does not exceed it and to pass into the draw.circle function
            radius = round(sqrt((clickX-c_mx)**2+(clickY-c_my)**2))
            #                                                   make sure the shapeThickness is not bigger than the radius
            draw.circle(canvas,mainColor,[clickX,clickY],radius,min(radius,shapeThickness))
            #The initial click point is the center

        elif tool == "line":
            canvas.blit(screenCopy, (0, 0))
            #Draw a line from the click point to the current mouse position
            draw.line(canvas,mainColor,[clickX,clickY],[c_mx,c_my],3)

        elif tool == "triangle":
            canvas.blit(screenCopy, (0, 0))
            draw.polygon(canvas,mainColor,[[clickX-((clickX-c_mx)//2),clickY],[c_mx,c_my],[clickX,clickY-(clickY-c_my)]],shapeThickness)
            #calculate the triangle polygon points as the bottom right corner, bottom left corner, and the bisector of the top edge of a
            #rectangle created between the click position and current mouse position

        # DRAW STAMPS IF TOOL = the selected stamp
        elif tool == "stamp1":
            canvas.blit(screenCopy,(0,0)) #overwrite previous iteration
            canvas.blit(transform.smoothscale(stamp1Image,(90,60)),(c_mx,c_my)) #Draw a resized scaled down stamp image
        elif tool == "stamp2":
            canvas.blit(screenCopy,(0,0))
            canvas.blit(transform.smoothscale(stamp2Image,(90,70)),(c_mx,c_my))
        elif tool == "stamp3":
            canvas.blit(screenCopy,(0,0))
            canvas.blit(transform.smoothscale(stamp3Image,(90,65)),(c_mx,c_my))
        elif tool == "stamp4":
            canvas.blit(screenCopy,(0,0))
            canvas.blit(transform.smoothscale(stamp4Image,(75,70)),(c_mx,c_my))
        elif tool == "stamp5":
            canvas.blit(screenCopy,(0,0))
            canvas.blit(transform.smoothscale(stamp5Image,(75,70)),(c_mx,c_my))
        elif tool == "stamp6":
            canvas.blit(screenCopy,(0,0))
            canvas.blit(transform.smoothscale(stamp6Image,(90,70)),(c_mx,c_my))
        elif tool == "stamp7":
            canvas.blit(screenCopy,(0,0))
            canvas.blit(transform.smoothscale(stamp7Image,(90,100)),(c_mx,c_my))
        elif tool == "stamp8":
            canvas.blit(screenCopy,(0,0))
            canvas.blit(transform.smoothscale(stamp8Image,(90,100)),(c_mx,c_my))
        elif tool == "stamp9":
            canvas.blit(screenCopy,(0,0))
            canvas.blit(transform.smoothscale(stamp9Image,(110,70)),(c_mx,c_my))
        elif tool == "stamp10":
            canvas.blit(screenCopy,(0,0))
            canvas.blit(transform.smoothscale(stamp10Image,(90,70)),(c_mx,c_my))

        elif tool == "selectArea" and selectingArea:
            if c_mx > clickX and c_my > clickY: # You can select the area if the click point is to the left and above the end point
                canvas.blit(screenCopy,(0,0)) #Cover previous iteration
                draw.rect(canvas, BLUE, [clickX, clickY, c_mx - clickX, c_my - clickY], 2)
                tempSurface = Surface((500,500),SRCALPHA) #Draw rectangle to indicate selected area
                draw.rect(tempSurface, (0,0,200,50), [clickX, clickY, c_mx - clickX, c_my - clickY], 0)
                canvas.blit(tempSurface,(0,0))

                copyRect = Rect(clickX, clickY, c_mx - clickX, c_my - clickY)  # COPY THE SELECTED AREA
                copySurface = Surface((c_mx-clickX,c_my-clickY))  #USing the rect calculaton from above
                copySurface.blit(screenCopy.subsurface(copyRect),(0,0))


    if tool == "text" and writingText:
        if keyPressed: # if the event loop says the key is pressed
            canvas.blit(screenCopy, (0, 0)) #cover the previous iteration

            if pressedKeyAscii == K_BACKSPACE: # if the key is backspace, remove the last character of the textString
                textString = textString[:-1]
                canvas.blit(font.SysFont("Arial", 24).render(textString, True, mainColor), (clickX, clickY))#Blit the new textString to the canvas
                keyPressed = False  # set key pressed as false foe the next iteration
            elif pressedKeyAscii != 304: #IF THE INPUTTED KEY ISNT SHIFT
                if shiftHeld: # IF SHIFT IS HELD, ADD UPPERCASE LETTERS
                    textString += pressedKey.upper() #if it is not backspace add the pressed key to the textString
                    canvas.blit(font.SysFont("Arial", 24).render(textString,True,mainColor),(clickX,clickY)) #Blit the new textString to the canvas
                    keyPressed = False #set key pressed as false foe the next iteration
                else: #If shift not held add lowercase letter
                    textString += pressedKey  # if it is not backspace add the pressed key to the textString
                    canvas.blit(font.SysFont("Arial", 24).render(textString, True, mainColor),(clickX, clickY))  # Blit the new textString to the canvas
                    keyPressed = False  # set key pressed as false foe the next iteration
            else: #if none of the conditions met then still write the text out so it doesnt dissappear because of the canvas blitting
                canvas.blit(font.SysFont("Arial", 24).render(textString, True, mainColor),
                            (clickX, clickY))  # Blit the new textString to the canvas
                keyPressed = False

    if tool != "text": #IF tool is changed dont let more be written to the screen
        writingText = False
        textString = ""

    if tool == "polygon" and makingPolygon:
        canvas.blit(screenCopy, (0, 0)) #cover everything from previous iteration
        if len(polygonPointList) == 1: #draw a dot if there is only one point in the polygon point list
            draw.line(canvas,mainColor,[polygonPointList[0][0],polygonPointList[0][1]],[polygonPointList[0][0],polygonPointList[0][1]],1)
        elif len(polygonPointList) == 2: # draw a line if there is two points in the pointlist
            draw.line(canvas, mainColor, [polygonPointList[0][0], polygonPointList[0][1]],
                      [polygonPointList[1][0], polygonPointList[1][1]], 3)
        elif len(polygonPointList) > 2: # If there is more than two points, connect them to draw a polygon
            draw.polygon(canvas,mainColor,polygonPointList,shapeThickness)
        #This was done because you cant draw a polygon with one or two points only
        for point in polygonPointList:
            draw.circle(canvas,mainColor,point,5,0) #Draw circles to indicate defined points. Circles overwritten when enter is pressed

    if placingImportedImage: #place the imported image on the screen until placingImportedImage is set false in the event loop
        canvas.blit(screenCopy, (0, 0))  #cover previous iteration
        canvas.blit(importImg,(c_mx,c_my)) #Blit the imported image to the mouse position




    screen.set_clip(None) #set screen clip to none so rest of the screen can be edited now

    #Blit a box around the tool buttons
    draw.rect(toolPalette, interfaceAccentColor, [0, 0, 125, 450], 1)
    screen.blit(toolPalette,(20,30))
    #Blit the box around the tool controls
    draw.rect(screen,WHITE,[150,30,175,450],0)
    draw.rect(screen, interfaceAccentColor, [150, 30, 175, 450], 1)

    #Draw buttons used to select the freehand tools
    if drawButton(screen, [25, 35], [50, 50], None, None,False, None, "pencil", "Draw on the canvas with a pencil",pencilToolImage):
        tool = "pencil"
    if drawButton(screen, [90, 35], [50, 50], None, None,False, None, "brush", "Paint on the canvas with a brush",brushToolImage):
        tool = "brush"
    if drawButton(screen, [25, 95], [50, 50], None, None,False, None, "spray", "Draw on the canvas with spray paint",sprayToolImage):
        tool = "spray"
    if drawButton(screen, [90, 95], [50, 50], None, None,False, None, "highlighter", "Highlight what you drew",highlighterToolImage):
        tool = "highlighter"
    if drawButton(screen, [25, 165], [50, 50], None, None,False, None, "eraser", "Erase what you drew",eraserToolImage):
        tool = "eraser"
    if drawButton(screen, [90, 165], [50, 50], None, None,False, None, "colorEraser", "Erase a specific color (active color)",eraserToolImage):
        tool = "colorEraser"
    draw.rect(screen, mainColor, [92, 202, 10, 10], 0) #Draw what specifc color the coloreraser will erase
    draw.rect(screen, BLACK, [92, 202, 10, 10], 1)

    # If freehand tools are slected use this to display tool size and allow you to choose tool size
    if tool == "eraser" or tool == "colorEraser" or tool == "highlighter" or tool == "spray" or tool == "brush" or tool == "pencil":
        screen.blit(arialFont.render("Brush Size: "+ str(toolSize),True,interfaceAccentColor),(197,35))
        screen.blit(arialFont.render("Scroll for larger sizes", True, interfaceAccentColor), (177, 240))
        #Draw buttons to select standard tool sizes
        if drawButton(screen, [170, 60], [50, 50], None, None,False, None, "","Change tool size to 2", brushSize2Image):
            toolSize = 2
        if drawButton(screen, [255, 60], [50, 50], None, None,False, None, "","Change tool size to 5",brushSize5Image):
            toolSize = 5
        if drawButton(screen, [170, 120], [50, 50], None, None,False, None, "","Change tool size to 10", brushSize10Image):
            toolSize = 10
        if drawButton(screen, [255, 120], [50, 50], None, None,False, None, "","Change tool size to 20", brushSize20Image):
            toolSize = 20
        if drawButton(screen, [210, 180], [50, 50], None, None,False, None, "","Change tool size to 30", brushSize30Image):
            toolSize = 30


    #Draw button for zoom tool
    if drawButton(screen, [25, 235], [50, 50], None, None,False, None, "zoom", "Zoom in to your screen", zoomToolImage):
        tool = "zoom"
        screenCopy = screen.copy()
    if tool == "zoom":
        #If zoom tool is selected then tell user the zoom size and allow them to adjust it with buttons aswell.
        screen.blit(arialFont.render("Zoom Size: " + str(zoomAmount), True, interfaceAccentColor), (197, 35))
        screen.blit(arialFont.render("Lower is closer", True, interfaceAccentColor), (197, 55))
        screen.blit(arialFont.render("Scroll for more control", True, interfaceAccentColor), (177, 75))
        #let user select the zoom distence with buttons
        if drawButton(screen, [170, 120], [50, 50], None, None,False, None, "","Change zoom size to 10", brushSize10Image):
            zoomAmount = 10
        if drawButton(screen, [255, 120], [50, 50], None, None,False, None, "","Change zoom size to 20", brushSize20Image):
            zoomAmount = 20
        if drawButton(screen, [210, 180], [50, 50], None, None,False, None, "","Change zoom size to 30", brushSize30Image):
            zoomAmount = 30

    #Draw button for color chooser tool
    if drawButton(screen, [90, 235], [50, 50], None, None,False, None, "colorChooser", "Select a color off the screen", dropperToolImage):
        tool = "colorChooser"

    #Draw buttons for shape tools
    if drawButton(screen, [25, 305], [50, 50], None, None,False, 40, "shapes", "Access the various included shape tools",shapeToolImage):
        tool = "shapes"
    #if shapes is selected then make these buttons to select specific tools and make "shapes" button active
    if tool == "shapes" or tool == "rectangle" or tool == "ellipse" or tool == "circle" or tool == "triangle" or tool == "polygon" or tool == "line":
        if drawButton(screen, [25, 305], [50, 50], None, None,True, 40, "shapes","Access the various included shape tools", shapeToolImage):
            tool = "shapes"
        if drawButton(screen, [170, 35], [50, 50], None, None,False, None, "rectangle","Draw Rectangles on the canvas", rectangleToolImage):
            tool = "rectangle"
        if drawButton(screen, [255, 35], [50, 50], None, None,False, None, "ellipse","Draw Ellipses on the canvas", ellipseToolImage):
            tool = "ellipse"
        if drawButton(screen, [170, 105], [50, 50], None, None,False, None, "circle","Draw Circles on the canvas", circleToolImage):
            tool = "circle"
        if drawButton(screen, [255, 105], [50, 50], None, None,False, None, "triangle","Draw triangles on the canvas", triangleToolImage):
            tool = "triangle"
        if drawButton(screen, [170, 175], [50, 50], None, None,False, None, "polygon","Draw Polygons on the canvas", polygonToolImage):
            tool = "polygon"
            polygonPointList = []
        if drawButton(screen, [255, 175], [50, 50], None, None,False, None, "line","Draw Lines on the canvas", lineToolImage):
            tool = "line"

        #Toggle filled shapes on and off
        if drawButton(screen, [170, 235], [50, 50], None, None,fillToggle,None,"", "Turn filled shapes on",shapeFilledImage):
            fillToggle = True #Toogle filled shapes on to activate and deactivate button depending on its value
            shapeThickness = 0 #set the shapes to filled


        if drawButton(screen, [255, 235], [50, 50], None, None,not fillToggle,None,"", "Turn filled shapes off",shapeEmptyImage):
            fillToggle = False #Toogle filled shapes on to activate and deactivate button depending on its value
            shapeThickness = 3 #set shapes to not filled


    #Create button for the canvas fill function
    if drawButton(screen, [90, 305], [50, 50], None, None,False, 40, "backFill", "Fill in areas of the screen",backFillToolImage):
        tool = "backFill"

    #if the canvas fill is selected then display buttons
    if tool == "backFill":
        #Click buttons to fill canvas with either primary or secondary colors
        if drawButton(screen, [170, 35], [50, 50], mainColor, None,True, None, "mainColorFill","Fill Canvas with the primary color", None):
            canvas.fill(mainColor)
            backgroundCanvas.fill(mainColor)
        if drawButton(screen, [255, 35], [50, 50], secondaryColor, None,True, None, "secondaryColorFill","Fill Canvas with the secondary color", None):
            canvas.fill(secondaryColor)
            backgroundCanvas.fill(secondaryColor)

        #click buttons to fill canvas with different background pictures. ALSO blit it to background canvas for use when erasing whats drawn on the image
        if drawButton(screen, [170, 105], [50, 50], None, None,False, 50, "","Fill Canvas with this background", simpleBackgroundImage):
            canvas.blit(transform.scale(simpleBackgroundImage,(600,500)),(0,0))
            backgroundCanvas.blit(transform.scale(simpleBackgroundImage, (600, 500)), (0, 0))
        if drawButton(screen, [255, 105], [50, 50], None, None,False, 50, "","Fill Canvas with this background", krustyKrabBackgroundImage):
            canvas.blit(transform.scale(krustyKrabBackgroundImage,(600,500)),(0,0))
            backgroundCanvas.blit(transform.scale(krustyKrabBackgroundImage, (600, 500)), (0, 0))
        if drawButton(screen, [170, 175], [50, 50], None, None,False, 50, "","Fill Canvas with this background", stageBackgroundImage):
            canvas.blit(transform.scale(stageBackgroundImage,(600,500)),(0,0))
            backgroundCanvas.blit(transform.scale(stageBackgroundImage, (600, 500)), (0, 0))
        if drawButton(screen, [255, 175], [50, 50], None, None,False, 50, "","Fill Canvas with this background", houseBackgroundImage):
            canvas.blit(transform.scale(houseBackgroundImage,(600,500)),(0,0))
            backgroundCanvas.blit(transform.scale(houseBackgroundImage, (600, 500)), (0, 0))

        screen.blit(arialFont.render("Filters:",True,interfaceAccentColor),(170,245))
        screen.blit(arialFont.render("Filters make the current ", True, interfaceAccentColor), (172, 320))
        screen.blit(arialFont.render("canvas The new background", True, interfaceAccentColor),
                    (160, 340))
        #Sepia Filter Tool
        if drawButton(screen, [170, 265], [50, 50],(212,190,115), None,False, 50, "","Put a Sepia Filter on the canvas", None):
            for x in range(500):
                for y in range(500):# use nested loop to iterate through all the canvas pixels
                    r, g, b, a = canvas.get_at((x, y))# get the rgb values at the current point
                    r2 = min(255, int(r * .393 + g * .769 + b * .189))
                    g2 = min(255, int(r * .349 + g * .686 + b * .168)) #Do calculations for sepia filter
                    b2 = min(255, int(r * .272 + g * .534 + b * .131))
                    canvas.set_at((x, y), (r2, g2, b2)) # Set the rgb values at the current point as the calculated values
            backgroundCanvas.blit(canvas,(0,0)) #Set background to canvas because you shouldn't be able to erase the filter

        if drawButton(screen, [255, 265], [50, 50], (150, 150, 150), None, False, 50, "","Put a Black and White Filter on the canvas", None):
            for x in range(500):
                for y in range(500): #Iterate thorough all the canvas pixels
                    r, g, b, a = canvas.get_at((x, y)) #Get the rgba values at the specfic point
                    gray = int((r+g+b)/3) #Do the calculations for the grey scale
                    canvas.set_at((x,y),(gray,gray,gray,a)) #Set the rgb at the specific point to calculated values
            backgroundCanvas.blit(canvas,(0, 0))  # Set background to canvas because you shouldn't be able to erase the filter

        if drawButton(screen, [213, 370], [50, 50], None, None, False, 40, "","Import an image for your background", openToolImage):
            try:
                # Get file name from dialog box
                fname = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.bmp")])
                importImg = image.load(fname)  # Import the selected image

                canvas.blit(transform.scale(importImg, (500, 500)), (0, 0))
                backgroundCanvas.blit(transform.scale(importImg, (500, 500)), (0, 0))

            except:
                errorMsg("Problem opening image")  # display error if problem
                pass

    #Button for text tool selection
    if drawButton(screen, [25, 365], [50, 50], None, None,False, None, "text", "Write text on the canvas",textToolImage):
        tool = "text"

    #Button to select the stamp tool
    if drawButton(screen, [90, 365], [50, 50], None, None,False, None, "stamp", "Put stamps on screen",stampToolImage):
        tool = "stamp"

    if "stamp" in tool:
        # if stamp tool is selected, let the user select stamps and set the "stamp" button above as active
        if drawButton(screen, [90, 365], [50, 50], None, None, True, None, "stamp", "Put stamps on screen",stampToolImage):
            tool = "stamp"
        if drawButton(screen, [170, 35], [50, 50], None, None,False, 50, "stamp1","Draw this stamp on the canvas", stamp1Image):
            tool = "stamp1"
        if drawButton(screen, [255, 35], [50, 50], None, None,False, 50, "stamp2","Draw this stamp on the canvas", stamp2Image):
            tool = "stamp2"
        if drawButton(screen, [170, 105], [50, 50], None, None,False, 50, "stamp3","Draw this stamp on the canvas", stamp3Image):
            tool = "stamp3"
        if drawButton(screen, [255, 105], [50, 50], None, None,False, 50, "stamp4","Draw this stamp on the canvas", stamp4Image):
            tool = "stamp4"
        if drawButton(screen, [170, 175], [50, 50], None, None,False, 50, "stamp5","Draw this stamp on the canvas", stamp5Image):
            tool = "stamp5"
        if drawButton(screen, [255, 175], [50, 50], None, None,False, 50, "stamp6","Draw this stamp on the canvas", stamp6Image):
            tool = "stamp6"
        if drawButton(screen, [170, 245], [50, 50], None, None,False, 50, "stamp7","Draw this stamp on the canvas", stamp7Image):
            tool = "stamp7"
        if drawButton(screen, [255, 245], [50, 50], None, None,False, 50, "stamp8","Draw this stamp on the canvas", stamp8Image):
            tool = "stamp8"
        if drawButton(screen, [170, 315], [50, 50], None, None,False, 50, "stamp9","Draw this stamp on the canvas", stamp9Image):
            tool = "stamp9"
        if drawButton(screen, [255, 315], [50, 50], None, None,False, 50, "stamp10","Draw this stamp on the canvas", stamp10Image):
            tool = "stamp10"
    #Select the fill tool
    if drawButton(screen, [25, 425], [50, 50], None, None, False, None, "fill", "Fill in areas on the canvas",fillToolImage):
        tool = "fill"

    if drawButton(screen, [90, 425], [50, 50], None, None, False, 40, "selectArea", "Copy and Paste an area on the canvas",copyPasteImage):
        tool = "selectArea"
        selectingArea = True

    #draw box around undo and redo buttons
    draw.rect(screen,WHITE,[20,540,125,60],0)
    draw.rect(screen, interfaceAccentColor, [20, 540, 125, 60], 1)
    if drawButton(screen, [25, 545], [50, 50], None, None, False, 50, "undo","Undo your last change", undoToolImage):
        undo(canvas) #use undo function
        time.delay(200) #delay to make sure it is not spammed by holding the mouse button down
    if drawButton(screen, [90, 545], [50, 50], None, None, False, 50, "redo", "Redo your last undo",redoToolImage):
        redo(canvas) #use redo function
        time.delay(200)



    draw.rect(screen, WHITE, [150, 540, 125, 60], 0)
    draw.rect(screen, interfaceAccentColor, [150, 540, 125, 60], 1)

    #Open image if button is pressed
    if drawButton(screen, [155, 545], [50, 50], None, None, False, 35, "open", "Open an image from your computer",openToolImage):
        try:
            #Get file name from dialog box
            fname = filedialog.askopenfilename(filetypes=[("Images","*.png;*.jpg;*.jpeg;*.bmp")])
            importImg = image.load(fname) #Import the selected image
            imgHeight = importImg.get_rect().size[0] #Get dimensions of image for resizing
            imgWidth = importImg.get_rect().size[1]

            placingImportedImage = True # set this to true to allow user to place image where they want
            screenCopy = canvas.copy() # get screen to cover previous iterations when placing
            tool="" #set tool to none to avoid interruptions when placing
            mouse.set_pos(canvasRect[0],canvasRect[1]) #set the mouse position at top right of canvas to begin placing

        except:
            errorMsg("Problem opening image") #display error if problem
            pass

    if drawButton(screen, [220, 545], [50, 50], None, None, False, 50, "save", "Save the canvas image to your computer",saveToolImage):
        try:
            fname = filedialog.asksaveasfilename(defaultextension=".png") # get place where the user wants to save and the filename
            image.save(canvas,fname) #save the file to the user specified place
        except:
            errorMsg("Problem saving image") #display error if problem
            pass

    ##DRAW INFO ON THE TOOL BOX WHEN USING TOOLS
    #Draw on info box when using the polygon tool
    #Done here because the tool info box is drawn after the area where these tools are used, so it would overlap
    if tool == "polygon" and makingPolygon == True:
        screen.blit(arialFont.render("Click points to make polygon", True, interfaceAccentColor), (157, 315))
        screen.blit(arialFont.render("Press 'Enter' to stop", True, interfaceAccentColor), (181, 330))

    #Draw info when using the open tool and positioning the image
    if placingImportedImage:
        screen.blit(arialFont.render("Position the image", True, interfaceAccentColor), (185, 200))
        screen.blit(arialFont.render("Click your mouse to stop", True, interfaceAccentColor), (170, 215))

    if writingText:
        screen.blit(arialFont.render("Type your text", True, interfaceAccentColor), (190, 200))
        screen.blit(arialFont.render("Press enter to stop", True, interfaceAccentColor), (182, 215))

    #draw rectangle around the color palette
    draw.rect(screen,WHITE,[905,20,295,265],0)
    draw.rect(screen, interfaceAccentColor, [905, 20, 295, 265], 1)
    #Draw color Palette
    if drawFullPalette(mx, my, screen): # if the maincolorpalette is clicked on then get the color at the mouse position
        mainColor = screen.get_at((mx, my))
        draw.circle(screen, (200, 200, 200), [mx, my], 5, 2) #draw indicator circle at the click point
        mouse.set_visible(False)

        if tool == "text" and writingText: #If color is changed when writing text
            canvas.blit(screenCopy,(0,0)) #overwrite last iteration
            canvas.blit(font.SysFont("Arial", 24).render(textString, True, mainColor), #Use the new mainColor as the color and rewrite
                        (clickX, clickY))  # Blit the new textString to the canvas
    else:
        mouse.set_visible(True)

    #draw button to change the interface accent color and also draw the border around it
    draw.rect(screen, WHITE, [1145, 545, 55, 55], 0)
    draw.rect(screen,interfaceAccentColor,[1145,545,55,55],1)
    if drawButton(screen,[1150,550],[45,45],None,None,False,50,None,"Change inteface accent color (default: Blue)",changeAccentColorImage):
        changingAccentColor = True
        tempColor = mainColor #get this color to change main Color back after done changing accent colors

    #display instructions to the user when changing accent color and set accent color as mainColor while changing
    # setting interface color as mainColor allows the user to get a preview and use all palettes easily
    if changingAccentColor:
        screen.blit(arialFont.render("Use the Palette to choose", True, interfaceAccentColor), (152, 200))
        screen.blit(arialFont.render("your accent color", True, interfaceAccentColor), (152, 215))
        screen.blit(arialFont.render("'Enter' to stop", True, interfaceAccentColor), (152, 230))
        tool = ""
        interfaceAccentColor = mainColor

    if tool == "selectArea":
        screen.blit(arialFont.render("Select an area", True, interfaceAccentColor), (193, 200))
        screen.blit(arialFont.render("Then place the image", True, interfaceAccentColor), (175, 215))

    #Draw out the primary and secondary colors and allow you to switch between them
    draw.rect(screen,WHITE,[905,285,70,70],0)
    draw.rect(screen, interfaceAccentColor, [905, 285, 70, 70], 1)
    #if either the primary or secondary color buttons are pressed, switch the colors with one another
    if drawButton(screen,[930,310],[40,40],secondaryColor,BLACK,True,None,None,"Swap primary and secondary colors",None) or drawButton(screen,[910,290],[40,40],mainColor,BLACK,True,None,None,"Swap primary and secondary colors",None):
        temp = secondaryColor
        secondaryColor = mainColor
        mainColor = temp
        time.delay(200)

    #Display the main color and the box around it
    draw.rect(screen, WHITE, [975, 285, 225, 70], 0)
    draw.rect(screen, interfaceAccentColor, [975, 285, 225, 70], 1)
    drawButton(screen, [980, 290], [215, 60], mainColor, BLACK, True, None, None, "This is your primary color",None)

    # Display a few selectable standard colors and a box around them
    draw.rect(screen, WHITE, [905, 355, 295, 40], 0)
    draw.rect(screen, interfaceAccentColor, [905, 355, 295, 40], 1)

    # display buttons for a few standard colors
    if drawButton(screen, [917, 360], [30, 30], RED,None, True, None, None, "Choose Red",None):
        mainColor = RED
    if drawButton(screen, [957, 360], [30, 30], BLUE,None, True, None, None, "Choose Blue",None):
        mainColor = BLUE
    if drawButton(screen, [997, 360], [30, 30], GREEN,None, True, None, None, "Choose Green",None):
        mainColor = GREEN
    if drawButton(screen, [1037, 360], [30, 30], (255, 128, 2),None, True, None, None, "Choose Orange",None):
        mainColor = (255, 128, 2)
    if drawButton(screen, [1077, 360], [30, 30], (229, 2, 255),None, True, None, None, "Choose Purple",None):
        mainColor = (229, 2, 255)
    if drawButton(screen, [1117, 360], [30, 30], (2, 238, 255),None, True, None, None, "Choose Turquoise",None):
        mainColor = (2, 238, 255)
    if drawButton(screen, [1157, 360], [30, 30], (255,255,0),None, True, None, None, "Choose Yellow",None):
        mainColor = (255,255,0)


    #Display Frames Per Second in the top right corner
    draw.rect(screen,WHITE,[1148,1,52,20],0)
    draw.rect(screen, interfaceAccentColor, [1148, 1, 52, 20], 1)
    screen.blit(arialFont.render("FPS: " + str(round(myClock.get_fps())), True, interfaceAccentColor),
                [1150, 3])

    #Zoom tool is done it bottom so that it can be seen above everything
    #This ensures nothing covers the displayed zoomed area
    if tool == "zoom" and canvasRect.collidepoint(mx,my):
        try: #Just in case it trys to read areas that dont exist
            screen.set_clip(None)
            xValue = mx - zoomAmount //2 #Get the top left point of the square zoom area
            yValue = my - zoomAmount //2
            if mb[0] == 1:
                canvas.set_at((c_mx,c_my),mainColor) #Draw pixels on canvas by pressing down mouse button when zoomed
            zoomedPart = Rect(xValue, yValue, zoomAmount, zoomAmount) #create rect of zoomed area
            zoomedImage = screen.subsurface(zoomedPart).copy() #get the zoomed image as a subsurface
            zoomedImage = transform.scale(zoomedImage, (200, 200)) #scale the zoomed image to a larger size

            screen.blit(zoomedImage, (mx, my)) #blit the zoomed image at the mouse position and draw an indicating box around it
            draw.rect(screen, interfaceAccentColor, [mx, my, 200, 200], 1)
        except:
            pass
    myClock.tick(120)  # Set a tick rate for the program. Allows up to 120 fps
    display.flip()  # Display everything drawn to the screen

quit()
