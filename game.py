import pygame
import Shapes
from Screen import PlayScreen

pygame.font.init()

#Global vars
screen_width = 800
screen_height = 700
play_width = 300 #meaning 300 // 10 = 30 width per block
play_height = 600 #meaning 600 // 10 = 60 width per block
block_size = 30
rows = 20  # y
columns = 10  # x

top_left_x = (screen_width - play_width) // 2
top_left_y = screen_height - play_height

def draw_text(win, text, color, top, left, font ):
    label = font.render(text, 1, color)

    win.blit(label, (top - (label.get_width()/2), left - (label.get_height()/2)) )

def draw_nextShape(shape, win):
    font = pygame.font.SysFont('comicsans', 30)

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(win, shape.color, (sx + j * 30, sy + i * 30, 30, 30), 0)

    draw_text(win, 'Next Shape', (255, 255, 255), sx + 60, sy - 30, font)

def draw_grid(win):
    sx = top_left_x - 60
    sy = top_left_y - 15

    for i in range(rows):
        pygame.draw.line(win, (128, 128, 128), (sx, sy + i * block_size),
                         (sx + play_width, sy + i * block_size))  # horizontal lines
        for j in range(columns):
            pygame.draw.line(win, (128, 128, 128), (sx + j * block_size, sy),
                             (sx + j * block_size, sy + play_height))  # vertical lines



def draw_window(win, grid):
    win.fill((0, 0, 0))
    top_leftx = top_left_x - 60
    top_lefty = top_left_y - 15

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Tetris', 1, (255, 255, 255))
    win.blit(label, (top_leftx + play_width / 2 - (label.get_width() / 2), block_size))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(win, grid[i][j], (top_leftx + j * block_size, top_lefty + i * block_size, block_size, block_size), 0)  # horizontal lines

    pygame.draw.rect(win, (255,255,255),
                     (top_leftx, top_lefty, play_width, play_height),
                     1)  # horizontal lines
    draw_grid(win)

def main(win):
    locked_pos= {}  # (x,y):(255,0,0)
    ps = PlayScreen(locked_pos)
    ps.draw()

    score           = 0
    change_piece    = False
    run             = True
    current_shape   = Shapes.get_shape()
    next_shape      = Shapes.get_shape()
    clock           = pygame.time.Clock()
    fall_time       = 0
    fall_speed      = 0.27

    lostfont    = pygame.font.SysFont('comicsans', 60, bold=True)
    topcenter   = top_left_x + play_width / 2
    leftcenter  = top_left_y + play_height / 2

    while run:
        ps.draw()
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_shape.y += 1

            if current_shape.y > 0:
                if not (ps.space_valid(current_shape)):
                    current_shape.y -= 1
                    change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_shape.x -= 1
                    if not ps.space_valid(current_shape):
                        current_shape.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_shape.x += 1
                    if not ps.space_valid(current_shape):
                        current_shape.x -= 1

                elif event.key == pygame.K_UP:
                    current_shape.rotation = current_shape.rotation + 1 % len(current_shape.shape)

                    if not ps.space_valid(current_shape):
                        current_shape.rotation = current_shape.rotation - 1 % len(current_shape.shape)

                elif event.key == pygame.K_DOWN:
                    current_shape.y += 1

                    if not ps.space_valid(current_shape):
                        current_shape.y -= 1

        # add piece to the grid for drawing
        ps.setcolor(current_shape)

        # IF PIECE HIT GROUND
        change_piece, current_shape, next_shape = ps.shapeChange(current_shape, next_shape, change_piece)


        draw_nextShape(next_shape, win)
        draw_window(win, ps.grids)
        pygame.display.update()

        # Check if user lost
        if ps.islost():
            draw_text(win, "YOU LOSE!!!",  (255, 255, 255), topcenter, leftcenter, lostfont)
            pygame.display.update()
            pygame.time.delay(1500)
            run = False