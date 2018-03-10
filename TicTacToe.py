import pygame
pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill([255, 255, 255]) # Sets background color to white. 
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()

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
    mouse_position = pygame.mouse.get_pos()

           
    # Draws a Nut on click 
    if mouse_state == (1,0,0):
        pygame.draw.circle(gameDisplay, RED, mouse_position, 30, 2)

    #Draws Cross
    def drawCross(screen, pos):
        points = [(100,100), (130,70), (130,100), (100,70)]
        pygame.draw.lines(gameDisplay, BLUE, False, points, 2)

    # Draws a Cross on click
    if mouse_state == (0,0,1):
         mouse_position_cross = pygame.mouse.get_pos()
         drawCross(gameDisplay, mouse_position_cross)

         
pygame.quit()
