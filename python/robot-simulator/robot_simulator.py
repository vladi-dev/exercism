NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

DIRECTIONS = {
    NORTH: (0, 1),
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1, 0)
}


class Robot:
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return (self.x, self.y)

    def advance_coords(self, x, y):
        self.x += x
        self.y += y

    def advance(self):
        self.advance_coords(*DIRECTIONS[self.bearing])

    def simulate(self, instruction):
        for command in instruction:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'A':
                self.advance()

    def turn_right(self):
        self.bearing = self.bearing << 1 if self.bearing < WEST else NORTH

    def turn_left(self):
        self.bearing = self.bearing >> 1 if self.bearing > NORTH else WEST
