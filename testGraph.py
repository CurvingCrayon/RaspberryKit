import sys, pygame, time

pygame.init()



size = width, height = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
points = [10]*width
screen = pygame.display.set_mode(size)
loopNum = 0
interval = 0.05
offset = 10

def addDot(x):
    points.pop(0)
    points.append(x)
          
def dot(x,y):
    pygame.draw.line(screen, GREEN, (x,y), (x,y), 1)
    
def line(x1,y1,x2,y2):
    pygame.draw.line(screen, GREEN, (x1,y1), (x2,y2), 1)
    
def drawDots():
    for i in range(width-1):
        line(i,height - points[i],i+1,height - points[i+1])

def translate(val):
    newVal = ( ((val+1)/1024) * (height-offset) ) + offset
    print(newVal)
    return newVal

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    loopNum = loopNum + 1
    addDot(loopNum)
    screen.fill(BLACK)
    drawDots()
    pygame.display.flip()
    time.sleep(interval)
    
