from turtle import *
print(screensize())

penup()
speed(0)

color('black')
shape("square")

shapesize(1.5, 1.5)

print(position())

posX = -10
posY = 10


setx(posX)

for positionX in range(8): 
    for positionY in range(8):
        # print(positionY)
        if(positionY % 2 == 1):
            color('black')
        else:
            color('white')

        #setpos(positionX * 32, positionY * 32)
        setx((posX + positionX) * 32)
        sety((posY - positionY) * 32)
        cellId = stamp()
        print(screensize())
        #print("cell ID:", cellId)




