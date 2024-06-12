
import heapq

class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.moves = []

    def solve(self):
        heap = []
        heapq.heappush(heap, (0, self.initial_state))
        visited = set()

        while heap:
            (cost, state) = heapq.heappop(heap)
            if state == self.goal_state:
                return self.moves

            for (next_state, move) in self.get_next_states(state):
                if next_state not in visited:
                    visited.add(next_state)
                    heapq.heappush(heap, (cost + 1, next_state))
                    self.moves.append(move)

        return None

    def get_next_states(self, state):
        next_states = []
        empty_pos = state.index('_')
        if empty_pos % 5 != 0:
            next_state = state[:]
            next_state[empty_pos], next_state[empty_pos - 1] = next_state[empty_pos - 1], next_state[empty_pos]
            next_states.append((next_state, next_state[empty_pos]))
        if empty_pos % 5 != 4:
            next_state = state[:]
            next_state[empty_pos], next_state[empty_pos + 1] = next_state[empty_pos + 1], next_state[empty_pos]
            next_states.append((next_state, next_state[empty_pos]))
        if empty_pos >= 5:
            next_state = state[:]
            next_state[empty_pos], next_state[empty_pos - 5] = next_state[empty_pos - 5], next_state[empty_pos]
            next_states.append((next_state, next_state[empty_pos]))
        if empty_pos < 10:
            next_state = state[:]
            next_state[empty_pos], next_state[empty_pos + 5] = next_state[empty_pos + 5], next_state[empty_pos]
            next_states.append((next_state, next_state[empty_pos]))

        return next_states

initial_state = [98, 74, 70, 26, 65, 91, 55, 12, '_', 68, 27, 18, 67, 40, 54]
goal_state = [98, 91, 74, 70, 68, 67, 65, 55, 54, 40, 27, 26, 18, 12, '_']
puzzle = Puzzle(initial_state, goal_state)
print(puzzle.solve())
