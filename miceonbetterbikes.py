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
    def __init__(self, posX, posY, posInfo, color, tag):
        self.posX = posX
        self.posY = posY
        self.posInfo = posInfo
        self.color = color
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
            placedCell = Cell(positionX, positionY, [positionX, positionY], (50,200,50), "walk")
            cells.append(placedCell)
            nacrtaj(placedCell)

def mazeCreation():
    # START
    for element in cells:
        if(element.posInfo == [0,0]):
            element.color = ("green")
            element.tag = "start"
            nacrtaj(element)

    # WALLS
    for i in range(16):
        randomNumA = random.randrange(1,16)
        randomNumB = random.randrange(1,16) 

        for element in cells:
            if(element.posInfo == [randomNumA, randomNumB]):
                element.color = ('gray')
                element.tag = "wall"
                nacrtaj(element)
    
    #FINISH
    for element in cells:
        if(element.posInfo == [randomNumA, randomNumB]):
            element.color = ('blue')
            element.tag = "finish"
            nacrtaj(element)
        


placeCells()
mazeCreation() 

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