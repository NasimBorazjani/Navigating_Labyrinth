
import heapq

def initialize():
    initial_state = (('10', 'x', '19', '11', 'x', 'x', '6', '12', 'x', 'x', 'x'), ('2', '9', '10', 'x', 'x', '10', '17', 'x', 'x', '11', '5'), ('x', '15', '8', '9', 'x', '7', '17', '20', 'x', 'x', '13'), ('1', '9', '15', '14', '9', '9', '13', '7', '12', 'x', '10'), ('9', 'x', '17', 'x', 'x', '7', 'x', '1', '14', 'x', 'x'), ('16', '18', '11', 'x', '14', '18', '9', '13', 'x', 'x', 'x'), ('9', '3', '5', '8', '17', '15', '19', 'x', '3', 'x', '14'), ('2', '13', 'x', 'x', '17', '13', '14', '18', '9', 'x', '6'), ('3', 'x', '18', '6', 'x', '14', 'x', 'x', '8', '19', 'x'), ('2', '4', 'x', 'x', 'x', 'x', '3', '4', 'x', '19', 'x'), ('x', 'x', 'x', 'x', '11', 'x', 'x', 'x', 'x', '5', '5'))
    start_workshop = (3, 7)
    end_workshop = (7, 0)
    districts = [(0, 2), (3, 6), (7, 10)]
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
