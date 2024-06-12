
import heapq

def initialize():
    initial_state = (('x', '13', 'x', '3', '10', '20', '3', 'x', '5'), ('x', 'x', 'x', 'x', '20', '16', 'x', 'x', '17'), ('3', '14', '18', '8', '1', '20', '14', 'x', '7'), ('13', '3', '6', '10', '7', '4', '6', '6', '1'), ('10', '12', '2', 'x', '11', 'x', '10', '8', '11'), ('x', 'x', 'x', '11', '6', '18', '13', '20', '17'), ('x', 'x', '16', 'x', '4', '17', '7', '10', '15'), ('x', '7', '16', '6', '19', '4', '7', 'x', 'x'), ('x', '11', '18', 'x', 'x', 'x', '3', '8', 'x'))
    start_workshop = (0, 7)
    end_workshop = (2, 1)
    districts = [(0, 2), (3, 4), (5, 8)]
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
