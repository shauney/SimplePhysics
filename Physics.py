from tkinter import *
import time
import random
import math
from Vector import *

class Particle(object):
    def __init__(self, rad):
        self.positionX = random.randint(20, 380)
        self.positionY = random.randint(20, 380)
        self.velocity = Vector(random.uniform(0.01, 0.5), random.uniform(0.01, 0.5))
        self.rad = rad
        self.item = ""

    def draw(self, canvas):
        self.item = canvas.create_oval(self.positionX-self.rad, self.positionY-self.rad, self.positionX+self.rad, self.positionY+self.rad, width=0, fill='blue')

    def redraw(self, canvas):
        self.checkCollison()
        self.move(self.velocity)
        canvas.coords(self.item, self.positionX-self.rad, self.positionY-self.rad, self.positionX+self.rad, self.positionY+self.rad)
        canvas.update()

    def move(self, vec):
        self.positionX = self.positionX + vec[0]
        self.positionY = self.positionY + vec[1]

    def checkCollison(self):
        # Check X position
        if (self.positionX + self.rad) > x_max:
            self.velocity[0] = abs(self.velocity[0]) * -1
        if (self.positionX - self.rad) < 0:
            self.velocity[0] = abs(self.velocity[0])
        # Check Y position
        if (self.positionY + self.rad) > x_max:
            self.velocity[1] = abs(self.velocity[1]) * -1
        if (self.positionY - self.rad) < 0:
            self.velocity[1] = abs(self.velocity[1])

    def getPositionX(self):
        return self.positionX

    def getPositionY(self):
        return self.positionY

    def getVelocityX(self):
        return self.velocity[0]

    def getVelocityY(self):
        return self.velocity[1]

    def getVelocityVector(self):
        return self.velocity

    def setVelocityVector(self, vec):
        self.velocity = vec

    def setVelocityX(self, newVelocity):
        self.velocity[0] = newVelocity

    def setVelocityY(self, newVelocity):
        self.velocity[1] = newVelocity

    def setPositionX(self, newPosition):
        self.positionX = newPosition

    def setPositionY(self, newPosition):
        self.positionY = newPosition

    def getRadius(self):
        return self.rad


def collideBalls(ballA, ballB):
    # Create a vector from the ball positions
    a = Vector(ballA.getPositionX(), ballA.getPositionY())
    b = Vector(ballB.getPositionX(), ballB.getPositionY())
    # Calculate distance between the balls and get the normal
    ab = a-b
    normal = Normalize(ab)

    # Move balls backwards untill they don't overlap
    while Distance(a, b) < (ballA.getRadius() + ballB.getRadius()):
        ballA.move(normal)
        a = Vector(ballA.getPositionX(), ballA.getPositionY())
        b = Vector(ballB.getPositionX(), ballB.getPositionY())
    

def particleCollide():
    for p1 in particleList:
        for p2 in particleList:
            if not p1 == p2:
                # Calculate distance between particles
                distance = Distance(p1.getVelocityVector(), p2.getVelocityVector())
                p1rad = p1.getRadius()
                p2rad = p2.getRadius()

                # Check distance is not less that both particles radius
                if distance <= (p1rad + p2rad):
                    collideBalls(p1, p2)
                    
    
# Create window and canvas
root = Tk()
canvas = Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Set edge boundries
x_min = 0
y_min = 0
x_max = 400
y_max = 400

# Create particle list
particleList = []

# Create particles and add into the list
particle1 = Particle(10)
particle2 = Particle(10)
particle3 = Particle(10)

particleList.append(particle1)
particleList.append(particle2)
particleList.append(particle3)

# Set random starting vectors and positions for all particles and draw onto canvas
for i in particleList:
    i.setVelocityX(random.uniform(0.01, 2))
    i.setVelocityY(random.uniform(0.01, 2))
    i.setPositionX(random.randint(20, 380))
    i.setPositionY(random.randint(20, 380))
    i.draw(canvas)

# Start animation
while ("true"):
    time.sleep(0.003)
    particleCollide()
    for i in particleList:
        i.redraw(canvas)

root.mainloop()
