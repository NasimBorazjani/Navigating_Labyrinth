
import heapq

def initialize():
    initial_state = (('10', '14', '4', '16', 'x', '17', '5', 'x', 'x'), ('5', '20', '16', '3', '1', '8', 'x', '16', '19'), ('1', 'x', '5', '13', '3', '15', '19', '15', 'x'), ('x', '16', '13', '20', 'x', '8', 'x', 'x', 'x'), ('x', '16', 'x', '17', '11', '1', 'x', '15', 'x'), ('10', 'x', '14', '11', '5', '7', '12', 'x', '5'), ('7', 'x', '15', 'x', 'x', 'x', '16', '3', '13'), ('x', '12', '14', 'x', 'x', 'x', '9', '7', '14'))
    start_workshop = (7, 7)
    end_workshop = (1, 2)
    districts = [(0, 1), (2, 6), (7, 8)]
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
