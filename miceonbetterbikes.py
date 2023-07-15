import pygame
import random
# pygame setup

pygame.init()
# FONT
text_font = pygame.font.SysFont("timesnewroman", 10)

surface = pygame.display.set_mode((528, 528))
clock = pygame.time.Clock()
running = True

cells = []

class Cell:
    visina = 32
    duzina = 32
    color = (0,0,0)
    def __init__(self, posX, posY, posInfo, tag):
        self.posX = posX
        self.posY = posY
        self.posInfo = posInfo
        self.tag = tag
       

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    surface.blit(img, (x,y))

def nacrtaj(celija):
    pygame.draw.rect(surface, celija.color, pygame.Rect(celija.posX * 33, celija.posY  * 33, celija.visina, celija.duzina))
    draw_text(str(celija.posInfo), text_font, (0,0,0), celija.posX * 33, celija.posY * 33) 
   

def placeCells():
    for positionX in range(0, 16):
        for positionY in range(0, 16):
            placedCell = Cell(positionX, positionY, [positionX, positionY], "wall")
            cells.append(placedCell)
            nacrtaj(placedCell)

def mazeCreation():
    #finishX = 15
    #finishY = 15

    finishX = random.randint(2,15)
    finishY = random.randint(2,15)
    startPoint = [0,0]

    #INITIAL 
    carvePath(startPoint, endPoint([finishX, finishY]))


    #GENERATE
    for element in cells:
        # START
        if(element.posInfo == startPoint):
            element.tag = "start"

        #FINISH
        if(element.posInfo == [finishX, finishY]):
            element.tag = "finish"


def findNeighbours(currentCell):
    neighbourList = []
    top =       [currentCell[0]    , currentCell[1] - 1]#TOP
    topRight =  [currentCell[0] + 1, currentCell[1] - 1]#TOP RIGHT
    right =     [currentCell[0] + 1, currentCell[1]    ]#RIGHT
    downRight = [currentCell[0] + 1, currentCell[1] + 1]#DOWN RIGHT
    down =      [currentCell[0]    , currentCell[1] + 1]#DOWN
    downLeft =  [currentCell[0] - 1, currentCell[1] + 1]#DOWN LEFT
    left =      [currentCell[0] - 1, currentCell[1]    ]#LEFT
    topLeft =   [currentCell[0] - 1, currentCell[1] - 1]#TOP LEFT
    
    neighbourList.append(top)
    neighbourList.append(topRight)
    neighbourList.append(right)
    neighbourList.append(downRight)
    neighbourList.append(down)
    neighbourList.append(downLeft)
    neighbourList.append(left)
    neighbourList.append(topLeft)
    
    return neighbourList

def endPoint(finishPos):
    #DECIDE WHICH CELL STARTS THE PATH
    endPointPos = []

    possibleStartChoice = findNeighbours(finishPos)

    #REMOVE ANY DIRECTIONS THAT ARE OUT OF BOUNDS
    for i in range(8):
        for startChoice in possibleStartChoice:
            if(startChoice[0]  > 15 or startChoice[1] > 15 or startChoice[0]  < 0 or startChoice[1] < 0):
                #print(possibleStartChoice) #FOR DEBUGGING PURPOSES
                possibleStartChoice.remove(startChoice)
                
                

    #CHOOSE A RANDOM DIRECTION FROM FINISH LINE THEN SET A WALK TILE AND THEN RETURN ITS POSITION
    selector = random.randint(0, len(possibleStartChoice) - 1)
    for element in cells:
        if(element.posInfo == possibleStartChoice[selector]):
            element.tag = "walk"
            endPointPos = element.posInfo
            #print(possibleStartChoice) #FOR DEBUGGING PURPOSES

    return endPointPos


def carvePath(startPoint, endPoint):
    print(startPoint, endPoint)

    #GET NEIGHBOURS
    neighbours = findNeighbours(endPoint)
    print(neighbours)
    
    currentExploringDirection = 0



    

    


def tagCells():
    for element in cells:
        if(element.tag == "start"):
            element.color = (33, 209, 79)
            nacrtaj(element)

        if(element.tag == "walk"):
            element.color = (82, 82, 82)
            nacrtaj(element)

        if(element.tag == "wall"):
            element.color = "gray"
            nacrtaj(element)

        if(element.tag == "finish"):
            element.color = (25, 128, 224)
            nacrtaj(element)


    
    

placeCells()
mazeCreation() 
tagCells()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    
     
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()