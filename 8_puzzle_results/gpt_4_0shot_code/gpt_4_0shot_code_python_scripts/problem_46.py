
import heapq

class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.moves = []

    def solve(self):
        heap = []
        heapq.heappush(heap, (self.heuristic(self.initial_state), self.initial_state))
        while heap:
            (h, state) = heapq.heappop(heap)
            if state == self.goal_state:
                return self.moves
            for (move, new_state) in self.neighbors(state):
                if new_state not in self.moves:
                    self.moves.append(move)
                    heapq.heappush(heap, (self.heuristic(new_state), new_state))
        return []

    def heuristic(self, state):
        return sum(abs(b % 4 - g % 4) + abs(b//4 - g//4)
                   for b, g in ((state.index(i), self.goal_state.index(i)) for i in range(1, 9)))

    def neighbors(self, state):
        neighbors = []
        i = state.index(0)
        moves = ((0, -1), (0, 1), (-1, 0), (1, 0))
        for dx, dy in moves:
            x, y = i % 4 + dx, i // 4 + dy
            if 0 <= x < 4 and 0 <= y < 3:
                new_state = list(state)
                new_state[i], new_state[x + y*4] = new_state[x + y*4], new_state[i]
                neighbors.append((new_state[x + y*4], new_state))
        return neighbors

initial_state = [85, 0, 61, 100, 45, 77, 10, 91, 83, 57, 95, 39]
goal_state = [100, 95, 91, 85, 83, 77, 61, 57, 45, 39, 10, 0]
puzzle = Puzzle(initial_state, goal_state)
print(puzzle.solve())
