
import numpy as np
import heapq

class Puzzle:
    def __init__(self, init_state, goal_state):
        self.init_state = np.array(init_state)
        self.goal_state = np.array(goal_state)
        self.empty_spot = tuple(np.argwhere(self.init_state == '_')[0])

    def get_moves(self):
        moves = []
        if self.empty_spot[0] > 0:
            moves.append('up')
        if self.empty_spot[0] < len(self.init_state) - 1:
            moves.append('down')
        if self.empty_spot[1] > 0:
            moves.append('left')
        if self.empty_spot[1] < len(self.init_state[0]) - 1:
            moves.append('right')
        return moves

    def swap(self, direction):
        x, y = self.empty_spot
        if direction == 'up':
            self.init_state[x, y], self.init_state[x - 1, y] = self.init_state[x - 1, y], self.init_state[x, y]
            self.empty_spot = (x - 1, y)
        elif direction == 'down':
            self.init_state[x, y], self.init_state[x + 1, y] = self.init_state[x + 1, y], self.init_state[x, y]
            self.empty_spot = (x + 1, y)
        elif direction == 'left':
            self.init_state[x, y], self.init_state[x, y - 1] = self.init_state[x, y - 1], self.init_state[x, y]
            self.empty_spot = (x, y - 1)
        elif direction == 'right':
            self.init_state[x, y], self.init_state[x, y + 1] = self.init_state[x, y + 1], self.init_state[x, y]
            self.empty_spot = (x, y + 1)

    def solve(self):
        queue = [(self.init_state, [])]
        visited = set()
        while queue:
            state, path = heapq.heappop(queue)
            if np.array_equal(state, self.goal_state):
                return path
            for move in self.get_moves():
                self.swap(move)
                if str(self.init_state.tolist()) not in visited:
                    visited.add(str(self.init_state.tolist()))
                    heapq.heappush(queue, (self.init_state.copy(), path + [self.empty_spot]))
                self.swap({'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}[move])

init_state = [[97, 78, '_', 9, 67], [18, 65, 52, 27, 66], [38, 92, 50, 14, 6]]
goal_state = [[97, 92, 78, 67, 66], [65, 52, 50, 27, 18], [38, 14, 9, 6, '_']]
puzzle = Puzzle(init_state, goal_state)
print(puzzle.solve())
