"""Pong!"""

import pygame
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 600
HEIGHT = 400
SCREEN_SIZE = (WIDTH, HEIGHT)

PAD_WIDTH = 10
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH // 2  # note that it's dangerous to use normal division, which creates floats that might lead to type errors
HALF_PAD_HEIGHT = PAD_HEIGHT // 2  # but integer division might round if we don't use even numbers, and rounding creates inaccuracy
PAD_VELOCITY = 7

BALL_RADIUS = 10
BALL_VELOCITY = 4

MAKES_BOUNCING_LOOK_NICER = 3  # this makes the ball not bounce immediately when it contacts the paddle
# otherwise, it sometimes looks like it bounces off nothing imo


def main():
    """Entrypoint to pong program."""

    # Boilerplate code for pygame display
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)  # https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
    pygame.display.set_caption("ping pong without the ping")

    playing: bool = True
    clock = pygame.time.Clock()

    initialize()  # Step 1: implement this function
    global p1_points, p2_points
    p1_points = 0
    p2_points = 0

    while playing:  # Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        screen.fill(BLACK)
        keypress()  # Step 2: implement
        model(screen)  # Step 3: implement
        pygame.display.update()  # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
        clock.tick(60)  # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    
    print("Player 1 points: " + str(p1_points))
    print("Player 2 points: " + str(p2_points))

    pygame.quit()


# Step 3:
def model(screen):
    """This function handles game logic and calculations."""
    global pad1_ypos, pad2_ypos, pad1_vel, pad2_vel, p1_points, p2_points

    # Draw net - horizontally centered vertical line
    # No effect on gameplay
    pygame.draw.line(screen, WHITE, [WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 5)  # https://www.pygame.org/docs/ref/draw.html#pygame.draw.line

    """1. Draw: draw the two rectangular paddles and the circular ball on screen using pygame's predefined functions."""
    # Draw paddles and ball
    pad1 = pygame.Rect([0, pad1_ypos - HALF_PAD_HEIGHT], [PAD_WIDTH, PAD_HEIGHT])  # https://www.pygame.org/docs/ref/rect.html tl;dr arguments are [left, top], [width, height]
    pad2 = pygame.Rect([WIDTH - PAD_WIDTH, pad2_ypos - HALF_PAD_HEIGHT], [PAD_WIDTH, PAD_HEIGHT])
    pygame.draw.rect(screen, WHITE, pad1)  # https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
    pygame.draw.rect(screen, WHITE, pad2)
    pygame.draw.circle(screen, WHITE, ball_pos, BALL_RADIUS)  # https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle

    """2. Paddles: check vertical bounds. Move paddle positions by their paddle velocity constants when appropriate."""
    # Check paddle 1
    if pad1_ypos > HALF_PAD_HEIGHT and pad1_ypos < HEIGHT - HALF_PAD_HEIGHT:
        pad1_ypos += pad1_vel
    elif pad1_ypos <= HALF_PAD_HEIGHT and pad1_vel > 0:  # this does work if it's == instead of <=, but I'm using <= just to be safe!
        pad1_ypos += pad1_vel
    elif pad1_ypos >= HEIGHT - HALF_PAD_HEIGHT and pad1_vel < 0:
        pad1_ypos += pad1_vel

    # Check paddle 2 (same as above, just with some variable name changes)
    if pad2_ypos > HALF_PAD_HEIGHT and pad2_ypos < HEIGHT - HALF_PAD_HEIGHT:
        pad2_ypos += pad2_vel
    elif pad2_ypos <= HALF_PAD_HEIGHT and pad2_vel > 0:
        pad2_ypos += pad2_vel
    elif pad2_ypos >= HEIGHT - HALF_PAD_HEIGHT and pad2_vel < 0:
        pad2_ypos += pad2_vel

    """3. Ball: check vertical bounds."""
    # Check collisions with top and bottom walls
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    """4. Ball: check horizontal bounds."""
    # Check if ball crosses its left bound. Then handle case 1 - collision with paddle and case 2 - no collision with paddle, out of bounds
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS - MAKES_BOUNCING_LOOK_NICER:  # this expression could (mathematically, it should - draw a diagram) just be PAD_WIDTH + BALL_RADIUS. But the constant makes it look better imo. An alternative is to use HALF_PAD_WIDTH instead of PAD_WIDTH, which is basically the same as using this constant.
        if ball_pos[1] >= pad1_ypos - HALF_PAD_HEIGHT and ball_pos[1] <= pad1_ypos + HALF_PAD_HEIGHT:
            ball_vel[0] *= -1
        else:
            p2_points += 1
            initialize()
    
    # Check bounds on right side (should be almost the same as the code above)
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS + MAKES_BOUNCING_LOOK_NICER:
        if ball_pos[1] >= pad2_ypos - HALF_PAD_HEIGHT and ball_pos[1] <= pad2_ypos + HALF_PAD_HEIGHT:
            ball_vel[0] *= -1
        else:
            p1_points += 1
            initialize()
    
    """5. Ball: update ball position."""
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]


# Step 1:
def initialize():
    """Initialize these global variables to default settings:
    paddle 1 y position - vertical center
    paddle 2 y position - vertical center
    ball position - horizontal and vertical center
    ball velocity - x and y velocity components are the BALL_VELOCITY constant

    This function is called once in the main() function to set up the board
    and is also called whenever the ball goes out of horizontal bounds to
    reset the board."""
    global pad1_ypos, pad2_ypos, ball_pos, ball_vel
    pad1_ypos = HEIGHT / 2
    pad2_ypos = HEIGHT / 2
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [BALL_VELOCITY, BALL_VELOCITY]


# Step 2:
def keypress():
    """Get keyboard input and set paddle 1 and paddle 2 velocity accordingly."""
    global pad1_vel, pad2_vel
    keys = pygame.key.get_pressed()  # https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

    # K_w and K_s should control the left paddle
    if keys[pygame.K_w]:
        pad1_vel = -PAD_VELOCITY
    elif keys[pygame.K_s]:
        pad1_vel = PAD_VELOCITY
    else:
        pad1_vel = 0

    # K_UP and K_DOWN arrow keys should control the right paddle
    if keys[pygame.K_UP]:
        pad2_vel = -PAD_VELOCITY
    elif keys[pygame.K_DOWN]:
        pad2_vel = PAD_VELOCITY
    else:
        pad2_vel = 0


if __name__ == "__main__":
    main()
