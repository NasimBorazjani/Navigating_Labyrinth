
import heapq
import math


def a_star():
    # Define the initial state of the puzzle
    initial_state = [[93, 88, 60], [28, 18, 24], ['_', 47, 53]]
    goal_state = [[93, 88, 60], [28, 24, 18], [53, 47, '_']]

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state == goal_state:
            return actions

        empty_spot = find_empty_spot(state)
        possible_moves = get_possible_moves(empty_spot)

        for move in possible_moves:
            new_state = make_move(state, empty_spot, move)
            new_cost = g + 1

            if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                visited_costs[str(new_state)] = new_cost
                h = heuristic(new_state, goal_state)
                heapq.heappush(queue, (g + h, new_cost, actions + [new_state[move[0]][move[1]]], new_state))

    return None


def find_empty_spot(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                return (i, j)


def get_possible_moves(empty_spot):
    possible_moves = []
    row, col = empty_spot
    if row > 0:
        possible_moves.append((row - 1, col))
    if row < 2:
        possible_moves.append((row + 1, col))
    if col > 0:
        possible_moves.append((row, col - 1))
    if col < 2:
        possible_moves.append((row, col + 1))
    return possible_moves


def make_move(state, empty_spot, move):
    new_state = [row[:] for row in state]
    row, col = empty_spot
    new_row, new_col = move
    new_state[row][col] = new_state[new_row][new_col]
    new_state[new_row][new_col] = '_'
    return new_state


def heuristic(state, goal_state):
    # The heuristic is the sum of Manhattan distances of each tile from its goal position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != '_':
                value = state[i][j]
                goal_pos = find_goal_position(value, goal_state)
                h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return h


def find_goal_position(value, goal_state):
    for i in range(len(goal_state)):
        for j in range(len(goal_state[0]):
            if goal_state[i][j] == value:
                return (i, j)


print(a_star())
