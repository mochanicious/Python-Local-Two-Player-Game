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
def draw_window(one, two, one_bullets, two_bullets, two_health, one_health, countdown):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, (0, 0, 0), BORDER)
    
    two_health_text = HEALTH_FONT.render("Health: " + str(two_health), 1, (255, 255, 255))
    one_health_text = HEALTH_FONT.render("Health: " + str(one_health), 1, (255, 255, 255))
    WIN.blit(two_health_text, (WIDTH - two_health_text.get_width() - 10, 10))
    WIN.blit(one_health_text, (10, 10))

    countdown_text = HEALTH_FONT.render("Countdown: " + str(countdown), 1, (255, 255, 255))
    WIN.blit(countdown_text, (WIDTH - countdown_text.get_width() - 10, HEIGHT - countdown_text.get_height() - 10))
    
    WIN.blit(ONE_SHIP, (one.x, one.y))
    WIN.blit(TWO_SHIP, (two.x, two.y))

    for bullet in two_bullets:
        pygame.draw.rect(WIN, (255, 0, 255), bullet)

    for bullet in one_bullets:
        pygame.draw.rect(WIN, (255, 165, 0), bullet)

    pygame.display.update()

# Function to handle movement of player one
def one_movement(keys_press, one):
    if keys_press[pygame.K_a] and one.x - VEL > 0 - 25: # LEFT
        one.x -= VEL
    if keys_press[pygame.K_d] and one.x + VEL + one.width < BORDER.x + 15: # RIGHT
        one.x += VEL
    if keys_press[pygame.K_s] and one.y + VEL + one.height < HEIGHT + 15: # DOWN
        one.y += VEL
    if keys_press[pygame.K_w] and one.y - VEL > 0 - 5: # UP
        one.y -= VEL

# Function to handle movement of player two
def two_movement(keys_press, two): 
        if keys_press[pygame.K_LEFT] and two.x - VEL > BORDER.x + BORDER.width - 15: #LEFT
            two.x -= VEL
        if keys_press[pygame.K_RIGHT] and two.x + VEL + two.width < WIDTH + 20: #RIGHT
            two.x += VEL
        if keys_press[pygame.K_DOWN] and two.y + VEL + two.height < HEIGHT + 15: #DOWN
            two.y += VEL
        if keys_press[pygame.K_UP] and two.y - VEL > 0 - 5: #UP
            two.y -= VEL

# Function to handle bullets
def handle_bullets(one_bullets, two_bullets, one, two):
    for bullet in one_bullets:
        bullet.x += B_VEL
        if two.colliderect(bullet):
            pygame.event.post(pygame.event.Event(TWO_HIT))
            one_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            one_bullets.remove(bullet)
    for bullet in two_bullets:
        bullet.x -= B_VEL
        if one.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ONE_HIT))
            two_bullets.remove(bullet)
        elif bullet.x < 0:
            two_bullets.remove(bullet)

# Function to draw the winner on the screen
def draw_winner(text):
    if text == "Player Wins!" or text == "Enemy Wins!":
        WIN.blit(SKY, (0, 0))
        draw_text = WINNER_FONT.render(text, 1, (255, 255, 255))
        WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
        WINNER_SOUND.play()
        pygame.display.update()
        pygame.time.delay(5000)
    else:
        WIN.blit(WATER, (0, 0))
        draw_text = WINNER_FONT.render(text, 1, (255, 255, 255))
        WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
        WAHH.play()
        pygame.display.update()
        pygame.time.delay(5000)

# Function to display the play again screen
def play_again_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    MUSIC.stop()
                    return True

        WIN.blit(AGAIN, (0, 0))
        MUSIC.play()
        play_again_text = WINNER_FONT.render("Play Again? (Press Enter)", 1, (255, 255, 255))
        WIN.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT // 2 - play_again_text.get_height() // 2))
        pygame.display.update() 

# Main game function
def main():
    one = pygame.Rect(100, 300, SPACE_H, SPACE_W)
    two = pygame.Rect(700, 300, SPACE_H, SPACE_W)
    one_bullets = []
    two_bullets = []
    one_health = 5
    two_health = 5
    clock = pygame.time.Clock()
    countdown = 5
    countdown_time = pygame.time.get_ticks() + 45000
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(one_bullets) < AMMO:
                    bullet = pygame.Rect(one.x + one.width, one.y + one.height//2 - 2, 10, 5)
                    one_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(two_bullets) < AMMO:
                    bullet = pygame.Rect(two.x, two.y + two.height//2 - 2, 10, 5)
                    two_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == TWO_HIT:
                two_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == ONE_HIT:
                one_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if two_health <= 0:
            winner_text = "Player One Wins!"

        if one_health <= 0:
            winner_text = "Player Two Wins!"

        if countdown <= 0:
            winner_text = "Draw!"

        if winner_text != "":
            draw_winner(winner_text)
            if not play_again_screen():
                break
            else:
                one = pygame.Rect(100, 300, SPACE_H, SPACE_W)
                two = pygame.Rect(700, 300, SPACE_H, SPACE_W)
                one_bullets = []
                two_bullets = []
                one_health = 5
                two_health = 5
                countdown = 5
                countdown_time = pygame.time.get_ticks() + 45000
                continue
        current_time = pygame.time.get_ticks()
        if countdown_time > current_time:
            countdown = (countdown_time - current_time) // 1000  # Calculate the remaining countdown time in seconds
        else:
            countdown = 0 

        keys_press = pygame.key.get_pressed()
        one_movement(keys_press, one)      
        two_movement(keys_press, two)  

        handle_bullets(one_bullets, two_bullets, one, two)

        draw_window(one, two, one_bullets, two_bullets, two_health, one_health, countdown)

# Execute the main function
if __name__ == "__main__":
    main()



