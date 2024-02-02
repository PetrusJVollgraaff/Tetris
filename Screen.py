import Shapes
import pygame


class PlayScreen:

    def __init__(self, lockedpos={}):
        self.locked_pos = lockedpos
        self.grids = self.draw


    def draw(self):
        grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in self.locked_pos:
                    c = self.locked_pos[(j, i)]
                    grid[i][j] = c

        self.grids = grid

    def space_valid(self, shape):
        accepted_positions = [[(j, i) for j in range(10) if self.grids[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_positions = [j for sub in accepted_positions for j in sub]
        formatted = shape.shape_format()

        for pos in formatted:
            if pos not in accepted_positions:
                if pos[1] > -1:
                    return False

        return True

    def islost(self):
        for pos in self.locked_pos:
            x, y = pos
            if y < 1:
                return True

        return False

    def setcolor(self, shape):
        shape_pos = shape.shape_format()
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                print( self.grids[y][x] )
                #pygame.draw.rect(win, self.grids[y][x], (top_leftx + j * block_size, top_lefty + i * block_size, block_size, block_size), 1)  # horizontal lines
                self.grids[y][x] = shape.color



    def clearRows(self):
        inc = 0

        for i in range(len( self.grids ) - 1, -1, -1):
            row = self.grids[i]
            if (0, 0, 0) not in row:
                inc += 1
                ind = i
                for j in range(len(row)):
                    try:
                        del self.locked_pos[(j, i)]

                    except:
                        continue

        if inc > 0:
            for key in sorted(list(self.locked_pos), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < ind:
                    newKey = (x, y + inc)
                    self.locked_pos[newKey] = self.locked_pos.pop(key)

        return inc

    def shapeChange(self, currentshape, nextshape, isChange):
        shape_pos = currentshape.shape_format()

        if isChange:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                self.locked_pos[p] = currentshape.color

            currentshape = nextshape
            nextshape = Shapes.get_shape()
            isChange = False
            self.clearRows()

        return isChange, currentshape, nextshape