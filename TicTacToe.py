import pygame
pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
gameDisplay.fill([255, 255, 255])  # Sets background color to white.
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()


WHITE = [255, 255, 255]
RED = (230, 30, 30)
BLUE = (30, 30, 230)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)

# Game Board
verticalLine_1 = pygame.draw.line(gameDisplay, BLACK, (270, 100), (270, 500), 3)
verticalLine_2 = pygame.draw.line(gameDisplay, BLACK, (530, 100), (530, 500), 3)
horizontalLine_1 = pygame.draw.line(gameDisplay, BLACK, (100, 230), (700, 230), 3)
horizontalLine_2 = pygame.draw.line(gameDisplay, BLACK, (100, 366), (700, 366), 3)
ref_rect = pygame.draw.rect(gameDisplay, BLACK,(100, 100, 602, 402), 1)

# Cross Sprite
class Cross(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # Calls constructor from parent class
        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.image = pygame.image.load("res/cross.png").convert_alpha()

    def nut(self, abscissa, ordinate):
        gameDisplay.blit(self.image, (abscissa, ordinate))


playerCross = Cross()  # Creates cross object


# Text Adder
def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


# ___Main Game-loop___
lost = False

while not lost:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            lost = True
            quit()
    pygame.display.update()
    clock.tick(60)

    # Mouse Properties
    mouse_state = pygame.mouse.get_pressed()  # Button State
    mouse_position = tuple(pygame.mouse.get_pos())  # Cursor Position Properties
    mouse_position_x = int(mouse_position[0])
    mouse_position_y = int(mouse_position[1])
    "print(mouse_position)"

    #Key Properties
    key_state = list(pygame.key.get_pressed())[113]
    print(key_state)

    # Draws a Nut on click 
    if mouse_state == (1, 0, 0):
        pygame.draw.circle(gameDisplay, BLACK, mouse_position, 30, 5)  # Nut Sprite

    # Draws Cross 
    if mouse_state == (0, 0, 1):  
        playerCross.nut(mouse_position_x, mouse_position_y)

    # Draws Button
    if 36+78 > mouse_position_x > 36 and 26+47 > mouse_position_y > 26:
        pygame.draw.rect(gameDisplay, BRIGHT_GREEN, (36, 26, 78, 47))
    else:
        pygame.draw.rect(gameDisplay, GREEN, (36, 26, 78, 47))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("Clear!", smallText)
    textRect.center = ((36+(78/2)), (26+(48/2)))
    gameDisplay.blit(textSurf, textRect)

pygame.quit()
quit()
