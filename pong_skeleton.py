"""Pong!"""

import pygame

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


def main():
    """Entrypoint to pong program."""
    ### DO NOT MODIFY THIS FUNCTION ###
    # Boilerplate code for pygame display
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)  # https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
    pygame.display.set_caption("ping pong without the ping")

    playing: bool = True
    clock = pygame.time.Clock()

    initialize()  # Step 1: implement
    global p1_points, p2_points
    p1_points = 0
    p2_points = 0

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        screen.fill(BLACK)
        keypress()  # Step 2: implement
        model(screen)  # Step 3: implement
        pygame.display.update()  # https://www.pygame.org/docs/ref/display.html#pygame.display.update
        clock.tick(60)  # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    
    print("Player 1 points: " + str(p1_points))
    print("Player 2 points: " + str(p2_points))

    pygame.quit()


# Step 3:
def model(screen):
    """This function handles game logic and calculations."""
    ### DO NOT MODIFY ###
    global pad1_ypos, pad2_ypos, pad1_vel, pad2_vel, p1_points, p2_points

    # Draw net - horizontally centered vertical line
    # No effect on gameplay
    pygame.draw.line(screen, WHITE, [WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 5)  # https://www.pygame.org/docs/ref/draw.html#pygame.draw.line

    ### DO NOT MODIFY ###

    """1. Draw: draw the two rectangular paddles and the circular ball on screen using 3 of pygame's predefined functions."""
    # Draw paddles and ball
    # pad1 = pygame.Rect([0, pad1_ypos - HALF_PAD_HEIGHT], [PAD_WIDTH, PAD_HEIGHT])  # https://www.pygame.org/docs/ref/rect.html tl;dr arguments are [left, top], [width, height]
    # https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
    # https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle

    """2. Paddles: check vertical bounds."""
    # TODO: IMPLEMENT

    # Check paddle 1
    
    # Check paddle 2 (should be the same as above, just with some variable name changes)

    """3. Ball: check vertical bounds."""
    # TODO: IMPLEMENT

    # Check collisions with top and bottom walls

    """4. Ball: check horizontal bounds."""
    # TODO: IMPLEMENT

    # Check if ball crosses its left bound.
    
    # Check bounds on right side (should be almost the same as the code above)
    
    """5. Ball: update ball position."""
    # TODO: IMPLEMENT


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
    # TODO: IMPLEMENT


# Step 2:
def keypress():
    """Get keyboard input and set paddle 1 and paddle 2 velocity accordingly."""
    global pad1_vel, pad2_vel
    keys = pygame.key.get_pressed()  # https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

    # TODO: implement

    # K_w and K_s should control the left paddle

    # K_UP and K_DOWN arrow keys should control the right paddle


if __name__ == "__main__":
    main()
