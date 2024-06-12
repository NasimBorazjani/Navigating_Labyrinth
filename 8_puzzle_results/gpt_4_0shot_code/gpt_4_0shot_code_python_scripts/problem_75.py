
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
                    return (i, j)

    def swap(self, state, pos1, pos2):
        new_state = [row[:] for row in state]
        new_state[pos1[0]][pos1[1]], new_state[pos2[0]][pos2[1]] = new_state[pos2[0]][pos2[1]], new_state[pos1[0]][pos1[1]]
        return new_state

    def get_possible_moves(self, state):
        moves = []
        x, y = self.find_empty_spot(state)
        if x > 0:
            moves.append((x - 1, y))
        if x < len(state) - 1:
            moves.append((x + 1, y))
        if y > 0:
            moves.append((x, y - 1))
        if y < len(state[0]) - 1:
            moves.append((x, y + 1))
        return moves

    def solve(self):
        queue = [(self.initial, [])]
        visited = set()
        while queue:
            state, path = heapq.heappop(queue)
            if str(state) in visited:
                continue
            visited.add(str(state))
            if state == self.goal:
                return path
            for move in self.get_possible_moves(state):
                new_state = self.swap(state, self.empty_spot, move)
                new_path = path + [state[move[0]][move[1]]]
                heapq.heappush(queue, (new_state, new_path))
        return None

initial = [['_', 67, 21, 97, 69], [61, 68, 55, 16, 73], [42, 41, 31, 83, 53]]
goal = [[97, 73, 69, 68, 67], [61, 55, 53, 42, 41], [31, 21, 16, '_', '_']]
puzzle = Puzzle(initial, goal)
print(puzzle.solve())
