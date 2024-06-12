
import numpy as np
import heapq

class Puzzle:
    def __init__(self, init_state, goal_state):
        self.init_state = init_state
        self.goal_state = goal_state
        self.n = len(init_state)

    def get_empty_pos(self, state):
        pos = np.where(np.array(state) == '_')
        return pos[0][0], pos[1][0]

    def get_possible_moves(self, state):
        empty_pos = self.get_empty_pos(state)
        moves = []
        if empty_pos[0] > 0:
            moves.append((empty_pos[0]-1, empty_pos[1]))
        if empty_pos[0] < self.n-1:
            moves.append((empty_pos[0]+1, empty_pos[1]))
        if empty_pos[1] > 0:
            moves.append((empty_pos[0], empty_pos[1]-1))
        if empty_pos[1] < self.n-1:
            moves.append((empty_pos[0], empty_pos[1]+1))
        return moves

    def swap(self, state, pos1, pos2):
        new_state = [row.copy() for row in state]
        new_state[pos1[0]][pos1[1]], new_state[pos2[0]][pos2[1]] = new_state[pos2[0]][pos2[1]], new_state[pos1[0]][pos1[1]]
        return new_state

    def heuristic(self, state):
        return sum(tile1 != tile2 for row1, row2 in zip(state, self.goal_state) for tile1, tile2 in zip(row1, row2) if tile1 != '_')

    def solve(self):
        queue = [(self.heuristic(self.init_state), self.init_state, [])]
        while queue:
            _, current_state, moves = heapq.heappop(queue)
            if current_state == self.goal_state:
                return moves
            for move in self.get_possible_moves(current_state):
                new_state = self.swap(current_state, self.get_empty_pos(current_state), move)
                new_moves = moves + [new_state[move[0]][move[1]]]
                heapq.heappush(queue, (self.heuristic(new_state) + len(new_moves), new_state, new_moves))

init_state = [[79, 90, 85, 67], [100, 61, '_', 15], [95, 41, 33, 73]]
goal_state = [[100, 95, 90, 85], [79, 73, 67, 61], [41, 33, 15, '_']]
puzzle = Puzzle(init_state, goal_state)
print(puzzle.solve())
