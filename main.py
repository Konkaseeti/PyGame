import pygame

#pygame setup
pygame.init()

tileSize = 32
srcPath = "E:/Projects/Python/PyGame/assets/"

screen = pygame.display.set_mode((1200,600))
displayArea = pygame.Surface((800,600))

grass1 = pygame.image.load(srcPath + "tile/g1.png").convert()


clock = pygame.time.Clock()
running = True

#return coordinates for centering
def center(obj1,obj2):
    """obj1 - obj being centered to.
       obj2 - obj being centered."""
    
    coordinates = (((obj1.get_width()/2)-obj2.get_width()/2),(obj1.get_height()/2)-obj2.get_height()/2 )
    return coordinates


class Tilemap:

    sp = False
    w = 0
    h = 0
    x = 0
    y = 0
    pos = pygame.Vector2(x,y)

    def __init__(self,arr,spawnpoint = False):

        if spawnpoint is True:
            self.sp = True
        else:
            self.sp = False

        self.w = len(arr[0])
        self.h = len(arr)

        self.map = arr
        self.surface = pygame.Surface((self.w*32,self.h*32))

        tx = 0   
        ty = 0

        for row in self.map:
            tx = 0
            for tile in row:
                self.surface.blit(tile,(tx,ty))
                tx += tileSize
            ty += tileSize

    def centerTo(self,obj):
        self.x = (obj.get_width()/2)-(self.surface.get_width()/2)
        self.y = (obj.get_height()/2)-(self.surface.get_height()/2)

        self.pos = pygame.Vector2(self.x,self.y )
        return self.pos

    def pos(self,xpos = None , ypos = None):
        if xpos != None:
            self.x = xpos
        if ypos != None:
            self.y = ypos

        self.pos = pygame.Vector2(self.x,self.y )
        return self.pos    
        
    

    
class Player:
    p = pygame.image.load(srcPath + "Player/man.png").convert_alpha()

    #player Size based on image used.
    w = p.get_width()
    h = p.get_height()
    #player Position
    x = (screen.get_width()/2) - (w/2) #ex. (1444/2) - (32/2) = 706
    y = (screen.get_height()/2) - (h/2) #ex. (720/2) - (32/2) = 344
    
    pos = pygame.Vector2(x,y)

    def update():
        #update player position
        pos = pygame.Vector2(Player.x,Player.y)    



        

point = Tilemap(
    [
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1],
        [grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1,grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1, grass1]
    ],
    True
)
  


#Setup before Game Loop
if point.sp is True:
    point.centerTo(displayArea)


#Game Loop
while running:

    #poll for eventsss
    for event in pygame.event.get():

        #close program if X in top left is pressed
        if event.type == pygame.QUIT:
            running = False

    #fill screen with color to clear from last frame
    screen.fill("white")
    displayArea.fill("red")

    #render game here \/

    #Blit is to draw elements to the 'screen'
    screen.blit(displayArea,(center(screen,displayArea)))
    
    #detecting key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        Player.pos.y -= 200 * dt
    if keys[pygame.K_s]:
        Player.pos.y += 200 * dt
    if keys[pygame.K_a]:
        Player.pos.x -= 200 * dt
    if keys[pygame.K_d]:
        Player.pos.x += 200 * dt
    #render game here /\

    Player.update()

    screen.blit(point.surface,center(screen,point.surface))
    screen.blit(Player.p,Player.pos)

    pygame.display.flip()
    dt = clock.tick(60) / 1000


pygame.quit()

