import graphics

def main():
    win = graphics.graphics(800,800, 'Animated 3')

    move = 0
    move2 = 0

    while not win.is_destroyed():
        move+=1
        move2+=.01

        if move > 200:
            move = 0
            move2 = 55
        
        win.clear()
        
        win.line(400+move,200+move,600-move,600-move)
        win.line(600,600,200,600)
        win.line(200,600,400,200)

        win.update_frame(20)

if __name__ == '__main__':
    main()