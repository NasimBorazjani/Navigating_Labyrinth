
import heapq

def initialize():
    coins = [22, 15, 4, 23, 19, 3, 5, 28, 22, 27, 13, 18, 14, 11, 22, 20, 27, 24, 21, 13, 25, 11, 6, 2, 30, 29, 4, 16, 3, 13, 3, 28, 28, 20, 15, 27, 4, 18, 20, 5, 16, 21, 25, 24, 23, 15, 22, 26]
    tax_values = {15: 2, 18: 17, 22: 16, 29: 7, 28: 5, 23: 1, 20: 17, 14: 3, 13: 2, 4: 2, 5: 3, 27: 10, 16: 6, 3: 2, 6: 3, 19: 8, 2: 1, 25: 6, 24: 19, 26: 18, 21: 10, 11: 1, 30: 4}
    target_sum = 303
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
