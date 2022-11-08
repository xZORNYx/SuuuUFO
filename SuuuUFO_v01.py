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
score = 0

# Load all the external files into pygame
font = pygame.font.Font("Square.ttf", 25)
player_sprite = pygame.image.load("sprites/ufo.png")
pipe_sprite = pygame.image.load("sprites/pipe.png")
pipe_sprite2 = pygame.image.load("sprites/pipe_reverse.png")
sign_sprite = pygame.image.load("sprites/sign_150.png")
bg_sky = pygame.image.load("sprites/background.png")
start_btn = pygame.image.load("sprites/start_btn.png")
youLose_disp = pygame.image.load("sprites/youLose.png")

# Set all the window parameters
screen = pygame.display.set_mode((SCREEN_DIM[0], SCREEN_DIM[1]), 0, 32)
pygame.display.set_caption("SuuuuuUFO")
pygame.display.set_icon(pygame.image.load("sprites/ufo.png"))

def displayScore():
    screen.blit(sign_sprite, (550, 0))    
    text = font.render(str(score), True, WHITE, WOOD)
    textRect = text.get_rect()
    textRect.center = (610, 79)
    screen.blit(text, textRect)

def keypress():
    global playing
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            p_char.jump()
            playing = True

def displayMenu():
    screen.blit(start_btn, (260, 120))

def displayDeathScreen():
    screen.blit(sign_sprite, (285, 255))    
    text = font.render(str(score), True, WHITE, WOOD)
    textRect = text.get_rect()
    textRect.center = (345, 334)
    screen.blit(text, textRect)
    screen.blit(youLose_disp, (210, 60))

class Pipe:
    def __init__(self, x_pos, y_pos, width, height, sprite, sprite_2, x_velocity,):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.sprite = sprite
        self.sprite_2 = sprite_2
        self.x_velocity = x_velocity
    
    def restartPipe(self):
        if self.x_pos <= -150:
            self.x_pos = random.randint(720, 900)
            self.y_pos = random.randint(150, 400)
            
    def update(self):
        self.x_pos -= self.x_velocity
        screen.blit(self.sprite, (self.x_pos, self.y_pos))   
        screen.blit(self.sprite_2, (self.x_pos, self.y_pos - self.height - 150))
        
    def checkCollision(self):
        if p_char.x_pos + p_char.width >= self.x_pos and p_char.x_pos <= self.x_pos + self.width:  # <-- X axis
            if p_char.y_pos + p_char.height >= self.y_pos or p_char.y_pos <= self.y_pos - 150:  # <-- Y axis                  
                p_char.alive = False
                global playing
                playing = False
    
    def draw(self):
        screen.blit(self.sprite, (self.x_pos, self.y_pos))   
        screen.blit(self.sprite_2, (self.x_pos, self.y_pos - self.height - 150))
        

class Player:
    def __init__(self, x_pos, y_pos, width, height, sprite,  acceleration, x_velocity, y_velocity, alive):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.sprite = sprite
        self.acceleration = acceleration
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.alive = alive
        
    def jump(self):
        self.y_velocity = -5.5
    
    def update(self):
        self.y_velocity += self.acceleration
        self.x_pos += self.x_velocity
        self.y_pos += self.y_velocity
        screen.blit(player_sprite, (self.x_pos, self.y_pos))
    
    def draw(self):
        screen.blit(player_sprite, (self.x_pos, self.y_pos))
    
    def die(self):
        pass
        

    
# Instanciation of the pipes in an array
pipes = [
    Pipe(720, random.randint(150, 400), 50, 440, pipe_sprite, pipe_sprite2, 2)
]        

# Instanciation of the player character
p_char = Player(150, 150, 50, 50, player_sprite, 0.25, 0, 1, True)



# Main LOOP
dead = False
playing = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            keypress()
                
    
    screen.blit(bg_sky, (0,0))  # Set the background

    if playing == True:
        p_char.update()

        # Work on all the pipes with a loop
        for pipe in pipes:
            pipe.restartPipe()
            pipe.update()
            pipe.checkCollision()   
            score += 1
    elif p_char.alive == True:    
        displayMenu()
        p_char.draw()
    else : 
        p_char.draw()
        for pipe in pipes:
            pipe.draw()
        displayDeathScreen()
    # Display everything about the score
    displayScore()
    
    
    
    # Update and wait until it starts again
    pygame.display.update()
    pygame.time.delay(10)