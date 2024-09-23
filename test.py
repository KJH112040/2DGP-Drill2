from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

turn = False

while(1):
    if(turn==False):
        x = 400
        y = 90
        while(x<600):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,90)
            x += 2
            delay(0.01)
        
        while(x>400):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x -= math.cos(110)
            y += math.sin(110)
            delay(0.01)
        
        while(x>200):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x -= math.cos(200)
            y -= math.sin(200)
            delay(0.01)
        
        turn=True
    elif(turn==True):
        x=400

close_canvas()
