
import heapq

def initialize():
    coins = [12, 23, 57, 18, 6, 5, 21, 15, 14, 23, 5, 16, 9, 8, 19, 8, 19, 6, 8, 3, 12, 2, 14, 3, 3, 4, 26, 6, 6, 25, 9, 13, 20, 24, 6, 26, 14, 25, 5, 26]
    tax_values = {6: 2, 12: 3, 9: 2, 2: 1, 14: 1, 16: 12, 21: 10, 4: 1, 8: 5, 26: 7, 23: 7, 57: 11, 15: 15, 19: 13, 25: 15, 13: 4, 5: 3, 24: 4, 3: 3, 18: 4, 20: 10}
    target_sum = 260
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    queue = [(0, 0, [], (0, 0, 0))]
    return (coins, tax_values, target_sum, visited_costs, queue)

def a_star():
    (coins, tax_values, target_sum, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        (total_value, prev_coin, total_tax) = state
        if (total_value == target_sum):
            return actions
        for coin in coins:
            if ((coin not in actions) and ((total_value + coin) <= target_sum)):
                if (((coin < prev_coin) and ((coin % 2) == 0)) or ((coin >= prev_coin) and ((coin % 2) != 0))):
                    coin_tax = tax_values[coin]
                    new_total_tax = (total_tax + coin_tax)
                    new_state = ((total_value + coin), coin, new_total_tax)
                    new_cost = (g + coin_tax)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + new_total_tax), new_cost, (actions + [coin]), new_state))
    return None
print(a_star())
