import random
# SHAPE FORMATS


def get_shape():
    shapes = [
        SShape(5, 0),
        ZShape(5, 0),
        IShape(5, 0),
        OShape(5, 0),
        JShape(5, 0),
        LShape(5, 0),
        TShape(5, 0),
        UShape(5, 0),
        BigOShape(5, 0),
        BigTShape(5, 0),
        CrossShape(5, 0),
    ]

    return random.choice(shapes)

class Piece:
    rows = 20  # y
    columns = 10  # x

    def __init__(self, x_axis, y_axis):
        self.x = x_axis
        self.y = y_axis
        self.rotation = 0  # number from 0-3
        self.color = (0, 255, 0)
        self.shape = [
            ['.....', '.....', '.....', '.....', '.....']
        ]

    def shape_format(self):
        positions = []
        formats = self.shape[self.rotation % len(self.shape)]

        for i, line in enumerate(formats):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    positions.append((self.x + j, self.y + i))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

        return positions


class SShape(Piece):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (60, 255, 0)
        self.shape = [
            ['.....', '.....', '..00.', '.00..', '.....'],
            ['.....', '..0..', '..00.', '...0.', '.....']
        ]


class ZShape(Piece):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (255, 60, 0)
        self.shape = [
            ['.....', '.....', '.00..', '..00.', '.....'],
            ['.....', '..0..', '.00..', '.0...', '.....']
        ]


class IShape(Piece):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (60, 255, 255)
        self.shape = [
            ['..0..', '..0..', '..0..', '..0..', '.....'],
            ['.....', '0000.', '.....', '.....', '.....']
        ]


class OShape(Piece):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (255, 255, 60)
        self.shape = [
            ['.....', '.....', '.00..', '.00..', '.....']
        ]


class JShape(Piece):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (255, 165, 60)
        self.shape = [
            ['.....', '.0...', '.000.', '.....', '.....'],
            ['.....', '..00.', '..0..', '..0..', '.....'],
            ['.....', '.....', '.000.', '...0.', '.....'],
            ['.....', '..0..', '..0..', '.00..', '.....']
        ]


class LShape(Piece):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (60, 60, 255)
        self.shape = [
            [
                '.....',
                '...0.',
                '.000.',
                '.....',
                '.....'
            ],
            [
                '.....',
                '..0..',
                '..0..',
                '..00.',
                '.....'
            ],
            [
                '.....',
                '.....',
                '.000.',
                '.0...',
                '.....'
            ],
            [
                '.....',
                '.00..',
                '..0..',
                '..0..',
                '.....'
            ]
        ]


class TShape(Piece):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (128, 60, 128)
        self.shape = [
            ['.....', '..0..', '.000.', '.....', '.....'],
            ['.....', '..0..', '..00.', '..0..', '.....'],
            ['.....', '.....', '.000.', '..0..', '.....'],
            ['.....', '..0..', '.00..', '..0..', '.....']
        ]


class UShape(Piece):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (70, 180, 255)
        self.shape = [
            [
                '.....',
                '.0.0.',
                '.000.',
                '.....',
                '.....'
            ],
            [
                '.....',
                '..00.',
                '..0..',
                '..00.',
                '.....'
            ],
            [
                '.....',
                '.....',
                '.000.',
                '.0.0.',
                '.....'
            ],
            [
                '.....',
                '.00..',
                '..0..',
                '.00..',
                '.....'
            ]
        ]

class BigOShape(Piece):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (255, 20, 60)
        self.shape = [
            ['.....', '.000.', '.000.', '.000.', '.....']
        ]

class BigTShape(Piece):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (128, 60, 255)
        self.shape = [
            [
                '..0..',
                '..0..',
                '.000.',
                '.....',
                '.....'
            ],
            [
                '.....',
                '..0..',
                '..000',
                '..0..',
                '.....'
            ],
            [
                '.....',
                '.....',
                '.000.',
                '..0..',
                '..0..'
            ],
            [
                '.....',
                '..0..',
                '000..',
                '..0..',
                '.....'
            ]
        ]

class CrossShape(Piece):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (255, 60, 128)
        self.shape = [
            [
                '.....',
                '..0..',
                '.000.',
                '..0..',
                '.....'
            ]
        ]
# index 0 - 6 represent shape
