import pygame, sys
from pygame.locals import *
from math import sin
import random
pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((640,480))
pygame.display.set_caption("Pygame sample.")

fontObj = pygame.font.Font('freesansbold.ttf', 32)

windowSurfaceObj.fill((0,0,0))

def coord2px(x,y):
	val = 5
	x+=val
	x/=val*2*4/3
	y+=val
	y/=val*2
	
	x*=640
	y*=480
	x = int(x)
	y = int(y)
	if 0>x or 640<=x:
		return None,None
		
	if 0>y or 480<=y:
		return None,None
	return x,y

def getColor(x,y):
	x,y = coord2px(x,y)
	if x is None:
		return 0,0,0
		
	return windowSurfaceObj.get_at((x,y))

def setColor(x,y,c):
	x,y = coord2px(x,y)
	if x is None:
		return
		
	windowSurfaceObj.set_at((x,y),c)

def joinColors(c1,c2):
	return map(lambda (a,b):(a+b)/2,zip(c1,c2))

a = random.random()
b = random.random()
c = random.random()
mag = a+b
a /= mag
b /= mag
c /= mag	
V = [
	[a,lambda x,y:(x,y)],
	[b,lambda x,y:(sin(x),sin(y))],
	[c,lambda x,y:(x/float(x*x-y*y),y/float(x*x-y*y))],
]



def genCoefs():
		return random.random(),random.random(),random.random(), \
		random.random(),random.random(),random.random()
	
table = [
	#p	  a	 b  c  d  e  f , color
	[.2, genCoefs()        , (0,255,255)],
	[.2, genCoefs()        , (255,0,255)],
	[.2, genCoefs()        , (255,255,0)],
	[.1, genCoefs()        , (0,0,255)],
	[.1, genCoefs()        , (255,0,0)],
	[.1, genCoefs()        , (0,255,0)],
	[.1, genCoefs()        , (255,255,255)],
]


def randJ():
	r = random.random()
	for j,v in enumerate(table):
		if r<=v[0]:
			return j
		r -= v[0]
	print "Error finding a J"
	return 0;

def F(j,x,y):
	#print j, table[j]
	a,b,c,d,e,f = table[j][1]
	out_x = 0
	out_y = 0
	for wk, Vk in V:
		px,py = Vk(a*x+b*y+c,d*x+e*y+f)
		out_x += wk*px
		out_y += wk*py
	return (out_x,out_y)
	

while True:
    
    px = random.random()*2-1
    py = random.random()*2-1
    pc = getColor(px,py)
    for i in xrange(2):
		j = randJ()
		px,py = F(j,px,py)
		pc = joinColors(pc,table[j][2])
    c = joinColors(pc,getColor(px,py))
    
    setColor(px,py,c)
    
    for event in pygame.event.get():
		
			
        if event.type == QUIT or (event.type == KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()        
    pygame.display.update()
#    fpsClock.tick(30)
/me creat
