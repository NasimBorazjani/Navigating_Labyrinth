
import heapq

class Puzzle:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
        self.empty_spot = self.find_empty_spot(self.initial)

    def find_empty_spot(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == '_':
                    return i, j

    def get_possible_moves(self):
        moves = ['up', 'down', 'left', 'right']
        if self.empty_spot[0] == 0:  # remove up
            moves.remove('up')
        if self.empty_spot[0] == 2:  # remove down
            moves.remove('down')
        if self.empty_spot[1] == 0:  # remove left
            moves.remove('left')
        if self.empty_spot[1] == 4:  # remove right
            moves.remove('right')
        return moves

    def swap(self, direction):
        x, y = self.empty_spot
        if direction == 'up':
            self.initial[x][y], self.initial[x - 1][y] = self.initial[x - 1][y], self.initial[x][y]
            self.empty_spot = x - 1, y
        elif direction == 'down':
            self.initial[x][y], self.initial[x + 1][y] = self.initial[x + 1][y], self.initial[x][y]
            self.empty_spot = x + 1, y
        elif direction == 'left':
            self.initial[x][y], self.initial[x][y - 1] = self.initial[x][y - 1], self.initial[x][y]
            self.empty_spot = x, y - 1
        elif direction == 'right':
            self.initial[x][y], self.initial[x][y + 1] = self.initial[x][y + 1], self.initial[x][y]
            self.empty_spot = x, y + 1

    def solve(self):
        heap = []
        heapq.heappush(heap, (0, self.initial))
        while heap:
            (priority, state) = heapq.heappop(heap)
            if state == self.goal:
                return priority
            for move in self.get_possible_moves():
                self.swap(move)
                heapq.heappush(heap, (priority + 1, self.initial))
                self.swap(move)  # swap back to original state

initial = [['_', 92, 90, 50, 40], [52, 39, 31, 83, 16], [36, 56, 51, 70, 49]]
goal = [[92, 90, 83, 70, 56], [52, 51, 50, 49, 40], [39, 36, 31, 16, '_']]
puzzle = Puzzle(initial, goal)
print(puzzle.solve())
