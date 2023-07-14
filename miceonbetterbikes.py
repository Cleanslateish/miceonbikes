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
    finishX = random.randrange(2,16)
    finishY = random.randrange(2,16)
    startPos = [0,0]

    #INITIAL 
    connectStartFinish(1,[finishX, finishY])


    #GENERATE
    for element in cells:
        # START
        if(element.posInfo == startPos):
            element.tag = "start"

        #FINISH
        if(element.posInfo == [finishX, finishY]):
            element.tag = "finish"
            #print(finishX, finishY)


        #if(finishX < finishY and finishX != 0):
            #if(element.posInfo == [finishX - 1, finishY]):
                #element.tag = "walk"
       # elif(finishY < finishX and finishY != 0):
           # if(element.posInfo == [finishX, finishY - 1]):
                #element.tag = "walk"


def connectStartFinish(startPos, finishPos):
    #DECIDE WHICH CELL STARTS THE PATH
    possibleStartPath = []
    
    if(finishPos[0] >= 0 and finishPos[0] <= 15 and finishPos[1] >= 0 and finishPos[1] <= 15):
        top =       [finishPos[0], finishPos[1] - 1]    #TOP
        topRight =  [finishPos[0] + 1, finishPos[1] - 1]#TOP RIGHT
        topLeft =   [finishPos[0] - 1, finishPos[1] - 1]#TOP LEFT

        down =      [finishPos[0], finishPos[1] + 1]    #DOWN
        downRight = [finishPos[0] + 1, finishPos[1] + 1]#DOWN RIGHT
        downLeft =  [finishPos[0] - 1, finishPos[1] + 1]#DOWN LEFT

        left =      [finishPos[0] - 1, finishPos[1]]    #LEFT

        right =     [finishPos[0] + 1, finishPos[1]]    #RIGHT


        possibleStartPath.append(top)
        possibleStartPath.append(topRight)
        possibleStartPath.append(topLeft)
        
        possibleStartPath.append(down)
        possibleStartPath.append(downRight)
        possibleStartPath.append(downLeft)
        
        possibleStartPath.append(left)
        
        possibleStartPath.append(right)



        

    selector = random.randint(0, len(possibleStartPath) - 1)

    for element in cells:
        if(element.posInfo == possibleStartPath[selector]):
            element.tag = "walk"
            print(selector)
            print(possibleStartPath[selector])
            print(possibleStartPath)

def tagCells():
    for element in cells:
        if(element.tag == "start"):
            element.color = "green"
            nacrtaj(element)

        if(element.tag == "walk"):
            element.color = (80,200,80)
            nacrtaj(element)

        if(element.tag == "wall"):
            element.color = "gray"
            nacrtaj(element)

        if(element.tag == "finish"):
            element.color = (3, 161, 252)
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