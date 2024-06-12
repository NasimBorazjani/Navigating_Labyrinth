
import heapq

def initialize():
    initial_state = (('x', '19', '7', '11', 'x', '3', '18', '8', 'x', 'x', 'x'), ('12', '18', '6', '1', '13', '12', '14', '11', '13', '5', '19'), ('11', '10', '10', '18', '15', 'x', '12', 'x', '4', '17', '10'), ('4', '3', '3', '7', 'x', '19', 'x', 'x', 'x', '12', '9'), ('x', 'x', '6', '19', 'x', '4', '14', 'x', '9', '4', '15'), ('4', '7', '6', '5', '8', 'x', '15', '3', 'x', '16', '3'), ('13', 'x', 'x', '1', '9', '1', '9', 'x', 'x', 'x', 'x'), ('2', '13', '5', '9', '5', 'x', '6', 'x', '18', 'x', '3'), ('19', 'x', '2', '9', '4', '13', 'x', 'x', 'x', '16', '6'), ('x', 'x', 'x', '12', 'x', '7', '9', '3', '9', '8', '1'), ('x', '10', 'x', '12', '3', '6', 'x', '4', '12', '4', 'x'))
    start_workshop = (5, 10)
    end_workshop = (3, 0)
    districts = [(0, 3), (4, 4), (5, 10)]
    moves = [((- 1), 0), (1, 0), (0, (- 1)), (0, 1)]
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], start_workshop)]
    return (initial_state, start_workshop, end_workshop, districts, moves, visited_costs, queue)

def a_star():
    (initial_state, start_workshop, end_workshop, districts, moves, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, current_workshop) = heapq.heappop(queue)
        if (current_workshop == end_workshop):
            return actions
        for move in moves:
            new_workshop = ((current_workshop[0] + move[0]), (current_workshop[1] + move[1]))
            if ((0 <= new_workshop[0] < len(initial_state)) and (0 <= new_workshop[1] < len(initial_state[0])) and (initial_state[new_workshop[0]][new_workshop[1]] != 'x') and any(((district[0] <= new_workshop[0] <= district[1]) for district in districts)) and any(((district[0] <= current_workshop[0] <= district[1]) for district in districts))):
                new_cost = (g + 1)
                if ((new_workshop not in visited_costs) or (new_cost < visited_costs[new_workshop])):
                    visited_costs[new_workshop] = new_cost
                    h = heuristic(new_workshop, end_workshop)
                    heapq.heappush(queue, ((new_cost + h), new_cost, (actions + [new_workshop]), new_workshop))
    return None

def heuristic(current_workshop, end_workshop):
    return ((((current_workshop[0] - end_workshop[0]) ** 2) + ((current_workshop[1] - end_workshop[1]) ** 2)) ** 0.5)
print(a_star())
