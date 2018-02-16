import sys, pygame, time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Lato", 20)

# S/W SPI config
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
#mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# H/W SPI config
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

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
    newVal = int( ((float(val+1))/float(1024)) * float(height-offset) ) + offset
    return newVal

def drawDescriptor():
	x = pygame.mouse.get_pos()[0]
	y = pygame.mouse.get_pos()[1]
	pygame.draw.line(screen, BLUE, (x,0), (x,height), 1)
	textsurface = font.render(str(points[x-1]), False, BLUE)
	fontHeight = font.get_height()
	screen.blit(textsurface,(x,y-fontHeight))
	
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    loopNum = loopNum + 1
    reading = mcp.read_adc(0)
    plotVal = translate(reading)
    addDot(plotVal)
    screen.fill(BLACK)
    drawDots()
    drawDescriptor()
    pygame.display.flip()
    time.sleep(interval)
    
