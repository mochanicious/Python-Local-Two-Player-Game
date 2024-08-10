# Aditya Saxena
# 10/08/2024
#Description: Space-ships one vs one, double player
import pygame
import random

# Initialize pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooters")

# Set the window icon
ICON = pygame.image.load("icon.png")
pygame.display.set_icon(ICON)

# Set up the game elements
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound("Assets_Grenade+1.mp3")
BULLET_FIRE_SOUND = pygame.mixer.Sound("Assets_Gun+Silencer.mp3")
WINNER_SOUND = pygame.mixer.Sound("Confetti.mp3")
WAHH = pygame.mixer.Sound("wah.mp3")
MUSIC = pygame.mixer.Sound("moosic.mp3")

FPS = 60
VEL = 4
B_VEL = 6
AMMO = 5
SPACE_H = 100
SPACE_W = 75
B_H = 10
B_W = 5
HEALTH_FONT = pygame.font.Font("Pixeltype.ttf", 40)
WINNER_FONT = pygame.font.Font("Pixeltype.ttf", 100)

ONE_HIT = pygame.USEREVENT + 1
TWO_HIT = pygame.USEREVENT + 2

# Load images
ONE_SHIP_IMAGE = pygame.image.load("firstspaceship.png")
ONE_SHIP = pygame.transform.scale(ONE_SHIP_IMAGE, (SPACE_H, SPACE_W))
TWO_SHIP_IMAGE = pygame.image.load("secondspaceship.png")
TWO_SHIP = pygame.transform.scale(TWO_SHIP_IMAGE, (SPACE_H, SPACE_W))
SPACE = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))
SKY = pygame.transform.scale(pygame.image.load("sky.png"), (WIDTH, HEIGHT))
WATER = pygame.transform.scale(pygame.image.load("water.png"), (WIDTH, HEIGHT))
AGAIN = pygame.transform.scale(pygame.image.load("again.png"), (WIDTH, HEIGHT))

# Function to draw the game window
def draw_window():
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, (0, 0, 0), BORDER)

    pygame.display.update()
