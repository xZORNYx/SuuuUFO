import pygame
import random

pygame.init()

# Set all the primary variables
WOOD = (140, 74, 48)
WHITE = (255, 255, 255)
NOTHING = (0, 0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
SCREEN_DIM = (720, 440)
acceleration = 0.15

score = 0

# Load all the external files into pygame
font = pygame.font.Font("Learning/flappy_shit/Square.ttf", 25)

player_sprite = pygame.image.load("Learning/flappy_shit/sprites/ufo.png")
pipe_sprite = pygame.image.load("Learning/flappy_shit/sprites/pipe.png")
pipe_sprite2 = pygame.image.load("Learning/flappy_shit/sprites/pipe_reverse.png")
sign_sprite = pygame.image.load("Learning/flappy_shit/sprites/sign_150.png")
bg_sky = pygame.image.load("Learning/flappy_shit/sprites/background.png")

# Set all the window parameters
screen = pygame.display.set_mode((SCREEN_DIM[0], SCREEN_DIM[1]), 0, 32)
pygame.display.set_caption("SuuuuuUFO")
pygame.display.set_icon(pygame.image.load("Learning/flappy_shit/sprites/ufo.png"))
screen.fill(BLACK)

# Creating a class for the pipes
class Pipe:
    def __init__(self, x_pos, y_pos, width, height, sprite, sprite_2, x_velocity,):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.sprite = sprite
        self.sprite_2 = sprite_2
        self.x_velocity = x_velocity

# Creating a class for the player character
class Player:
    def __init__(self, x_pos, y_pos, width, height, sprite,  x_velocity, y_velocity):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.sprite = sprite
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

# Instanciation of the pipes in an array
pipes = [
    Pipe(720, random.randint(150, 400), 50, 440, pipe_sprite, pipe_sprite2, 2)
]        

# Instanciation of the player character
p_char = Player(150, 100, 50, 50, player_sprite, 0, 1)



# Main LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p_char.y_velocity = -3.5
                
    
            
    screen.blit(bg_sky, (0,0))  # Set the background
    
    # Edit the position of the player and increase it's velocity
    p_char.y_velocity += acceleration 
    p_char.x_pos += p_char.x_velocity
    p_char.y_pos += p_char.y_velocity
    
    


    screen.blit(player_sprite, (p_char.x_pos, p_char.y_pos))   
    
    
    # Work on all the pipes with a loop
    for pipe in pipes:
        # Replace the pipes at the start of their run if it's needed
        if pipe.x_pos <= -150:
            pipe.x_pos = random.randint(720, 900)
            pipe.y_pos = random.randint(150, 400)
            score += 1 # The score is increased here for the moment, to change
            
        # Edit the position of the pipe
        pipe.x_pos -= pipe.x_velocity
        
        # Draw the pipe on it's new position
        screen.blit(pipe.sprite, (pipe.x_pos, pipe.y_pos))   
        screen.blit(pipe.sprite_2, (pipe.x_pos, pipe.y_pos - pipe.height - 150))    
            
        # check pipe collision with player
        if p_char.x_pos + p_char.width >= pipe.x_pos and p_char.x_pos <= pipe.x_pos + pipe.width:  # <-- X axis
            if p_char.y_pos + p_char.height >= pipe.y_pos or p_char.y_pos <= pipe.y_pos - 150:  # <-- Y axis                   
                running = False
    
    # Display everything about the score
    screen.blit(sign_sprite, (550, 0))    
    text = font.render(str(score), True, WHITE, WOOD)
    textRect = text.get_rect()
    textRect.center = (610, 79)
    screen.blit(text, textRect)
    
    # Update and wait until it starts again
    pygame.display.update()
    pygame.time.delay(10)