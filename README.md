Space Shooters
Space Shooters is a 2D player-vs-player space shooting game developed using Pygame. The game features two players, each controlling a spaceship on opposite sides of the screen. The goal is to deplete your opponent's health by firing bullets while avoiding being hit.

Features
Two-player gameplay: Control two spaceships, one on the left and one on the right.
Bullet firing: Players can shoot bullets to damage their opponent. 
Health system: Each player has a health bar that decreases when hit by a bullet.
Countdown timer: The game includes a countdown timer that determines the length of each match.
Sound effects: Bullet fire, bullet hit, and victory sounds enhance the gaming experience.
Backgrounds: The game includes different backgrounds that change based on game events (win, draw).

Game Controls
Player One: (To be Added)
Move left: A
Move right: D
Move up: W
Move down: S
Shoot: Left Ctrl

Player Two: (To be Added)
Move left: Left Arrow
Move right: Right Arrow
Move up: Up Arrow
Move down: Down Arrow
Shoot: Right Ctrl

Installation and Setup
Ensure Python is installed:
Install Pygame: You can install Pygame using pip:
pip install pygame

Download the game assets: The game requires certain images and sound files. Ensure you have the following files in the same directory as the game script:
icon.png
firstspaceship.png
secondspaceship.png
bg.jpg
sky.png
water.png
again.png
Assets_Grenade+1.mp3
Assets_Gun+Silencer.mp3
Confetti.mp3
wah.mp3
moosic.mp3
Pixeltype.ttf (Font file)
Run the game:
python space_shooters.py

How to Play
Objective: The objective is to reduce the opponent's health to zero before the countdown timer runs out.
Winning: If one player’s health reaches zero, the other player wins. If both players still have health when the countdown reaches zero, the game ends in a draw.
Play Again: After the game ends, players can press Enter to play again, or close the window to quit.

Code Structure
draw_window(): Draws the game window, including spaceships, bullets, health, and countdown timer.
one_movement(): Handles the movement of Player One's spaceship. (To be Added)
two_movement() : Handles the movement of Player Two's spaceship. (To be Added)
handle_bullets(): Manages bullet movement and detects collisions between bullets and spaceships. (To be Added)
draw_winner(): Displays the winner screen with corresponding background and plays a sound effect. (To be Added)
play_again_screen(): Displays a screen prompting players to play again or quit. (To be Added)
main(): Main game loop that handles game events, player inputs, and updates the screen. (To be Added)
