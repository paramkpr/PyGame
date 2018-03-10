import pygame
pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill([255, 255, 255]) # Sets background color to white. 
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()

WHITE = [255, 255, 255]
RED = (230,30,30)
BLUE = (30,30,230)
BLACK = (0,0,0)

# Game Board
verticalLine_1 = pygame.draw.line(gameDisplay, BLACK, (244,100),(244,500), 3) 
verticalLine_2 = pygame.draw.line(gameDisplay, BLACK, (556,100),(556,500), 3)
horizontalLine_1 = pygame.draw.line(gameDisplay, BLACK, (100,230), (700,230), 3)
horizontalLine_2 = pygame.draw.line(gameDisplay, BLACK, (100,366), (700,366), 3)


lost = False

while not lost:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lost = True
            quit()
    pygame.display.update()
    clock.tick(60)

    mouse_state = pygame.mouse.get_pressed()
    print(mouse_state)
    global mouse_position
    mouse_position = list(pygame.mouse.get_pos())
    mouse_position_x = int(mouse_position[0])
    mouse_position_y = int(mouse_position[1])
           
    # Draws a Nut on click 
    if mouse_state == (1,0,0):
        pygame.draw.circle(gameDisplay, RED, mouse_position, 30, 2)

    #Cross Sprite
    class cross(pygame.sprite.Sprite):

        def __init__(self, color, width, height):
            super().__init__() # Calls constructor from parent class
            self.image = pygame.Surface([30,30])
            self.image.fill(WHITE)
            self.image.set_colorkey(WHITE)
            self.image = pygame.image.load("res/cross.png").convert_alpha()

        def nut(self, abscissa, ordinate):
            gameDisplay.blit(self.image, (abscissa, ordinate))
            
    playerCross = cross(WHITE, 30, 30)

    #Draws Cross
    if mouse_state == (0,0,1):
        playerCross.nut(mouse_position_x, mouse_position_y)

pygame.quit()
