# Implementation of classic arcade game Pong
# Use codeskulptor to run Python program in browser
# http://www.codeskulptor.org

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_pos = WIDTH / 2 - 2 * PAD_HEIGHT
paddle2_pos = WIDTH / 2 - 2 * PAD_HEIGHT
paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0



# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[1] =  0 - random.randrange(1, 3)
    if direction == LEFT :
        ball_vel[0] = 0 - random.randrange(2, 4)
    elif direction == RIGHT :
        ball_vel[0] = random.randrange(2, 4)


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(LEFT)
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, BALL_RADIUS
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]     
    
    # collide and reflect off of top/bottom of canvas
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = 0 - ball_vel[1]
    
    #collision with gutters
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH: 
        if ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
            ball_vel[0] = 0 - ball_vel[0]
        else:    
            score2 += 1
            spawn_ball(RIGHT)
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
            ball_vel[0] = 0 - ball_vel[0]
        else:    
            score1 += 1
            spawn_ball(LEFT)

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
        
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel <= 0) or (paddle1_pos + paddle1_vel) >= (HEIGHT - PAD_HEIGHT):
        paddle1_pos += 0        
    else:
        paddle1_pos += paddle1_vel
        
    if (paddle2_pos + paddle2_vel <= 0) or (paddle2_pos + paddle2_vel) >= (HEIGHT - PAD_HEIGHT):
        paddle2_pos += 0
    else:
        paddle2_pos += paddle2_vel
  
    # draw paddles
    canvas.draw_line((4, paddle1_pos), (4, paddle1_pos + PAD_HEIGHT), PAD_WIDTH, "white")
    canvas.draw_line((596, paddle2_pos), (596, paddle2_pos + PAD_HEIGHT), PAD_WIDTH, "white")
    
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1), (30, 20), 30, "white")
    canvas.draw_text(str(score2), (560, 20), 30, "white")
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
         paddle1_vel = -2
    elif key==simplegui.KEY_MAP["s"]:
         paddle1_vel = 2
    elif key==simplegui.KEY_MAP["up"]:
         paddle2_vel = -2
    elif key==simplegui.KEY_MAP["down"]:
         paddle2_vel = 2
  
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
         paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
         paddle1_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
         paddle2_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
         paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button("Restart", new_game)


# start frame
new_game()
frame.start()
