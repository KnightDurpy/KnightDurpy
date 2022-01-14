import graphics

def white_lines(win):
    x = 0
    y = 0
    while True:
        if x > 500:
            break 
        else:
            win.line(x,0,x,500, 'white', 5)
            win.line(0,y,500,y, 'white', 5)
            x+=100
            y+=100

    

def draw_tile(win,pos_x,pos_y,east,west,north,south,add_blue,well):
    x1 = pos_x
    x2 = pos_x
    y1 = pos_y
    y2 = pos_y
    if east:
        x2 += 50
    if west:
        x1 -= 50
    if north:
        y1 -= 50
    if south:
        y2 += 50
    
    win.line(x1,pos_y,x2,pos_y,'black',10)
    win.line(pos_x,y1,pos_x,y2,'black',10)

    if well:
        win.rectangle(pos_x-15,pos_y-15,30,30,'black')
        if add_blue:
            win.rectangle(pos_x-10,pos_y-10,20,20,'blue')
    else:
        win.rectangle(pos_x-5,pos_y-5,10,10,'black')
    
    if add_blue:
        win.line(x1,pos_y-.50,x2,pos_y-.50,'blue',3)
        win.line(pos_x-.50,y1,pos_x-.50,y2,'blue',3)

 
def main():
    win = graphics.graphics(500,500, 'Pipe Grid')
    ''' base color '''
    win.rectangle(0,0,500,500,'grey')

    ''' Black Pipes '''
    ''' I wish I could do this in a loop
    but i would have to use random and that
    is not the goal of this '''
    draw_tile(win,50,50,True,False,False,True,False,False)
    draw_tile(win, 150,50,True,True,False,False,False,False)
    draw_tile(win,250,50,True,False,False,False,False,True)
    draw_tile(win,350,50,False,True,False,True,False,False)
    draw_tile(win,450,50,False,False,False,True,False,True)
    draw_tile(win,50,150,False,False,True,True,False,False)
    draw_tile(win,250,150,False,True,False,False,False,True)
    draw_tile(win,350,150,True,True,True,False,False,False)
    draw_tile(win,450,150,True,False,False,False,False,True)
    draw_tile(win,50,250,True,True,False,True, False,False)
    draw_tile(win,350,250,True,True,False,True,False,False)
    draw_tile(win,450,250,False,True,False,False,False,True)
    draw_tile(win,350,350,True,False,True,True,False,False)
    draw_tile(win,450,350,True,True,True,False,False,False)
    draw_tile(win,50,450,False,False,False,True,False,True)
    draw_tile(win,150,450,False,True,True,False,False,False)
    draw_tile(win,250,450,True,False,False,False,False,True)
    draw_tile(win,350,450,False,False,False,True,False,True)
    draw_tile(win,450,450,False,False,False,True,False,True)

    ''' Blue Pipes '''
    draw_tile(win,150,150,False,False,False,True,True,True)
    draw_tile(win, 150,250,True,False,True,True,True,False)
    draw_tile(win, 250,250,False,True,True,True,True,True)
    draw_tile(win,50,350,True,False,False,True,True,False)
    draw_tile(win,150,350,True,True,True,False,True,False)
    draw_tile(win,250,350,True,False,True,False,True,False)

    ''' Grid Marks '''
    white_lines(win)

    win.mainloop()

if __name__ == '__main__':
    main()