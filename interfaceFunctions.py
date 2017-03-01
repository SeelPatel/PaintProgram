# Python
# Created by Seel Patel

from pygame import *
from otherFunctions import *

#some standard colors
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
WHITE = (0, 0, 0)

#main button colors
buttonColorMain = (255, 0, 0)
buttonOutlineMain = (0, 0, 0)
#color selected on the range palette. (palette with rainbowlike gradient)
rangeColor = (0, 0, 255)

#The accent color of the interface
interfaceAccentColor = (0,0,255)

#The color palette surface and rect
Palette = Surface((285, 255), SRCALPHA)
PaletteRect = Rect(300, 10, 285, 255)

# The main area of the color palette which displays the colors
selectPaletteRect = Rect(0, 0, 0, 0)

#Undo and redo list
undoList = []
redoList = []

#Font
arialFont = None

#Get the selected tool
selectedTool = None

def initFont():
    font.init() #initialize font
    global arialFont
    arialFont = font.SysFont("Arial", 14) #set arial font


def getTool(tool):
    global selectedTool
    selectedTool = tool #get selected tool from main file


def setPalettePos(x, y):
    global PaletteRect
    global selectPaletteRect
    PaletteRect = Rect(x, y, 285, 255) #set the main palette position on the screen
    selectPaletteRect = Rect(PaletteRect[0], PaletteRect[1], 255, 255)


def setButtonColor(color):
    global buttonColorMain
    buttonColorMain = color #set color of buttons


def setButtonOutline(color):
    global buttonOutlineMain
    buttonOutlineMain = color #set color of button outline


def initRangePalette(screen):
    global rangePalette # Range palette is the rainbow gradient paleete
    global rangePaletteRect

    rangePalette = Surface((25, 255), SRCALPHA) #set the rangePalette surface
    yPos = 0 #set y postion for loop
    pColor = (255, 0, 0) # set starting color for the first iteration and the top pf the range palette

    for count in range(6):
        for cY in range(41):
            if count == 0:
                pColor = (pColor[0], pColor[1] + 6, pColor[2]) # add to green
            if count == 1:
                pColor = (pColor[0] - 6, pColor[1], pColor[2]) #take from red
            if count == 2:
                pColor = (pColor[0], pColor[1], pColor[2] + 6) #add to blue
            if count == 3:
                pColor = (pColor[0], pColor[1] - 6, pColor[2]) #take from green
            if count == 4:
                pColor = (pColor[0] + 6, pColor[1], pColor[2]) # add to red
            if count == 5:
                pColor = (pColor[0], pColor[1], pColor[2] - 6) # take from blue

            yPos += 1 # add to the position where the line below is being drawn
            draw.line(rangePalette, pColor, [0, yPos + 3], [25, yPos + 3], 10)

    #Blit the palette to the screen before the iteration of the main loop in PaintProgram.py
    screen.blit(rangePalette, (PaletteRect[0] + 260, PaletteRect[1]))

    # Instead of finding an RGB range image, I decided to create one, because i have previous experience with how RGB works
    #I did the calculations off of the data found on this website.
    # http: // www.w3schools.com / colors / colors_picker.asp
    #As you go down the rgb range, you change Red, Green and Blue in a specific order to create a rainbow range effect
    #You start with a solid red and then you add to the green, and then you take away red, and so on until you are back at red


#create a black gradient from bottom to top with varying opacities
def initBlackGradient():
    global blackGradient
    blackGradient = Surface((255, 255), SRCALPHA)# create the surface

    for y in range(255): # start from transparent and work down to full black to create a gradient used in the palette
        draw.line(blackGradient, (0, 0, 0, y), [0, y], [255, y], 1)


def drawRangePalette(mx, my, screen):
    global rangeColor #range color that is used to draw the main palette where the user selects their color from

    #create rect and blit the range palette I generated in the range palette init function to the screen
    rangePaletteRect = Rect(PaletteRect[0] + 260, PaletteRect[1], 25, 255)
    screen.blit(rangePalette, (PaletteRect[0] + 260, PaletteRect[1]))

    #check if the range palette was clicked on and draw a line at the click point to indicate position
    if rangePaletteRect.collidepoint(mx, my) and mouse.get_pressed()[0] == 1:
        screen.blit(rangePalette, (PaletteRect[0] + 260, PaletteRect[1])) #has to be blit again so user doesnt get color of line at any point
        rangeColor = screen.get_at((mx, my)) #set the range color for the main color palette
        draw.line(screen, (250, 250, 250), [rangePaletteRect[0] + 3, my], [rangePaletteRect[0] + 21, my], 5) #Draw the line for position indication


def drawColorGradient(rangeColor):
    #take the range color from the above function and create a gradient that will mix in with the black gradient to create a color palette
    for x in range(255):
        #Draw lines from full alpha to none across a surface to create a gradient
        draw.line(Palette, (min(255, rangeColor[0] + x), min(255, rangeColor[1] + x), min(255, rangeColor[2] + x)),
                  [255 - x, 0], [255 - x, 255], 1)

#The palette is inspired by and works the same way as the one in photoshop does
def drawFullPalette(mx, my, screen):
    drawColorGradient(rangeColor) #Draw the color gradient from the above function
    screen.blit(Palette, (PaletteRect[0], PaletteRect[1])) #blit the actual palette to the screen
    # blit the generated black palette to the screen
    screen.blit(blackGradient, (PaletteRect[0]+1, PaletteRect[1])) #The +1 offsets the black gradient to the right to align it with the color gradient
    drawRangePalette(mx, my, screen)
    if selectPaletteRect.collidepoint(mx, my) and mouse.get_pressed()[0] == 1: # If the main palette is clicked on the function returns true
        return True

#function I created to draw buttons.
def drawButton(screen, point, dimensions, overrideColor, overrideOutlineColor, buttonActive, imageScale, toolTag, tooltip,image):
    mx, my = mouse.get_pos() #mouse details
    mb = mouse.get_pressed()

    buttonRect = Rect(point[0], point[1], dimensions[0], dimensions[1]) #rect of the button

    if overrideColor != None: #set overide color if one is provided
        buttonColor = overrideColor # if not provided go with standard button color
    else:
        buttonColor = buttonColorMain

    if overrideOutlineColor != None: #same as overide color but for button outline
        buttonOutline = overrideOutlineColor
    else:
        buttonOutline = buttonOutlineMain

    # Hovering Over Button
    if buttonRect.collidepoint(mx, my) and mb[0] != 1: #check if hovering
        tempSurface = Surface((dimensions[0], dimensions[1]),SRCALPHA) #create translucent black surface to blit on button
        draw.rect(tempSurface, [0, 0, 0, 50],                       #This is to make it darker when it is hovered over
                  [0, 0, dimensions[0], dimensions[1]], 0)
        screen.blit(tempSurface,(point[0],point[1]))

    #Pressing the button
    elif buttonRect.collidepoint(mx,my) and mb[0] == 1: #check if pressed
        tempSurface = Surface((dimensions[0], dimensions[1]),SRCALPHA) #Create a dark translucent surface
        draw.rect(tempSurface,  [0,0,0,75],                         #to make the button event darker when it is pressed
                  [0, 0, dimensions[0], dimensions[1]], 0)
        draw.rect(screen,buttonColor,buttonRect,0)
        screen.blit(tempSurface,(point[0],point[1]))
    else:
        draw.rect(screen,buttonColor,buttonRect,0)

    #Button On
    if toolTag == selectedTool or buttonActive: #check if the toolTag is the selected current tool or if the button is manually set active
        tempSurface = Surface((dimensions[0], dimensions[1]), SRCALPHA)
        draw.rect(tempSurface, [0, 0, 0, 25],                   # if the above conditions are true draw an outline around the buttn
                  [0, 0, dimensions[0], dimensions[1]], 0)      # and make it darker to indicate that it is selected/on
        draw.rect(screen, buttonColor, buttonRect, 0)
        screen.blit(tempSurface, (point[0], point[1]))
        draw.rect(screen,buttonOutline,buttonRect,1)

    if buttonRect.collidepoint(mx,my):
        toolTipText = arialFont.render(tooltip,True,buttonOutlineMain)
        screen.blit(toolTipText,(355,538)) #if you hover over the button it displays a tool tip in the
                                            # info bar under the canvas. This tooltip is passed into the function

    #if an image is provided then it is displayed on the button.
    if image != None:
        try:
            if imageScale != None: # if the user did specify a scale for the image it is scaled to that and blitted in the center
                image = transform.smoothscale(image, (imageScale, imageScale))
                #calculate center and blit the image there
                screen.blit(image, (point[0] + (dimensions[0] - imageScale) // 2, point[1] + (dimensions[1] - imageScale) // 2))
            else:
                #if no scale is specified then the image is scaled to 30,30 and blitted in the center
                image = transform.smoothscale(image,(30,30))
                screen.blit(image,(point[0]+(dimensions[0]-30)//2,point[1]+(dimensions[1]-30)//2))
        except:
            errorMsg("Unable to display button image") #error if it couldnt be displayed

    #if the button is pressed then return true and otherwise return false
    if mb[0] == 1 and buttonRect.collidepoint(mx,my):
        return True
    else:
        return False


# def drawCircleButton() do later
def undo(canvas):
    #Revert to the last item in the undo list and add current display to the redoList
    if len(undoList) > 1:
        redoList.append(canvas.copy())
        del undoList[-1] #delete the previous item in the undoList
        canvas.blit(undoList[-1], (0, 0)) #blit the canvas from the undolist to the screen

#function for adding to the undo list
def addUndo(canvas):
    global redoList
    undoList.append(canvas) #add to list
    redoList = [] #if adding to the undoList make the previous redoList blank

#Redoing your undo
def redo(canvas):
    if len(redoList) > 0: # if the redo list has an item
        undoList.append(redoList[-1]) #add the last item in the list to the undolist and blit it to the canvas
        canvas.blit(redoList[-1], (0, 0))
        del redoList[-1] #delete the last item in the list

