import dudraw

dudraw.set_canvas_size(700,700)
dudraw.clear(dudraw.BLACK)

def title_card():
    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.line(0,0.91,1,0.91)
    dudraw.set_font_family("OCR A Extended")
    dudraw.set_font_size(35)
    dudraw.text(0.5,0.95,"PONG")

def left_player_1 (y_change: float):
    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.filled_rectangle(0.025,0.5+y_change,0.025,0.2)


def right_player_2(y_change: float):
    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.filled_rectangle(0.975,0.5+y_change,0.025,0.2)

def ball (x: float, y: float,r:float): 
    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.filled_circle(x,y,r)

def scoreboard (a: float, b: float):
    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.set_font_size(20)
    dudraw.text(0.1,0.95,f'Player 1: {a}')
    dudraw.text(0.9,0.95,f'Player 2: {b}')



def main():
    movement_velocity_left = 0.01
    movement_velocity_right = 0.01
    ball_change_x = 0.015
    ball_change_y = 0.010
    radius = 0.01
    x_center = 2*radius
    y_center = radius
    left_player_score = 0 
    right_player_score = 0

    while True:
        dudraw.clear(dudraw.BLACK)
        left_player_1(movement_velocity_left)
        right_player_2(movement_velocity_right)
        title_card()
        scoreboard(left_player_score,right_player_score)
        if dudraw.has_next_key_typed():
            key = dudraw.next_key_typed()
            if key =="q" and movement_velocity_left < 0.12:
                movement_velocity_left += 0.1
            if key == 'a' and movement_velocity_left > -0.2:
                movement_velocity_left -= 0.1
            if key == 'o' and movement_velocity_right <0.12:
                movement_velocity_right +=0.1
            if key == 'l' and movement_velocity_right > -0.2:
                movement_velocity_right -= 0.1
            if key == 'g':
                return False
        
        ball(x_center,y_center,radius)
        x_center += ball_change_x
        if x_center + radius > 1:
            ball_change_x *= -1
        if x_center - radius <= 0:
            ball_change_x *= -1
        y_center += ball_change_y
        if y_center + radius > 0.91:
            ball_change_y *=-1
        if y_center - radius <= 0:
            ball_change_y *=-1
        ball_change_x *= 1.001
        ball_change_y *= 1.001

        
        #parameters for the left side of the screen
        if x_center-radius< 0.05 and 0.3+movement_velocity_left <y_center< 0.7 +movement_velocity_left:
            ball_change_x *= -1
            left_player_score +=1
        if x_center+radius> 0.95 and 0.3+movement_velocity_right <y_center< 0.7 +movement_velocity_right:
            right_player_score += 1
            ball_change_x *= -1

        
        dudraw.show(50)
    dudraw.show(5000)

main()