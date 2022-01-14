import random
import graphics
import pipes_static_A

def main():
    win = graphics.graphics(500,500, 'Pipe Grid')
    ''' base color '''
    win.rectangle(0,0,500,500,'grey')

    x_pos = 50
    ''' Surprisingly the mainloop doesn't make this happen infinetly '''
    y_pos = 50
    ''' 
    Im sorry this checker is so long 
    I thought this loop would be smaller as I mentioned last time
    '''
    while True:
        if y_pos > 450:
            break
        if random.randint(0,1) == 1:
            North = True
        else:
            North = False
        if random.randint(0,1) == 1:
            South = True
        else:
            South = False
        if random.randint(0,1) == 1:
            East = True
        else:
            East = False
        if random.randint(0,1) == 1:
            West = True
        else:
            West = False
        if random.randint(0,1) == 1:
            Color = True
        else:
            Color = False
        if random.randint(0,1) == 1:
            Well = True
        else:
            Well = False
        
        pipes_static_A.draw_tile(win,x_pos,y_pos,East,West,North,South,Color,Well)

        x_pos+=100
        if x_pos > 450:
            x_pos = 50
            y_pos+=100

    pipes_static_A.white_lines(win)
    win.mainloop()


if __name__ == '__main__':
    main()