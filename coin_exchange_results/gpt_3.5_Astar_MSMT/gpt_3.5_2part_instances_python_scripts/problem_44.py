
import heapq

def initialize():
    coins = [2, 27, 9, 80, 20, 81, 13, 24, 16, 6, 26, 12, 3, 26, 20, 8, 16, 8, 20, 22, 9, 34, 23, 8, 12, 34, 4, 6, 22, 19]
    tax_values = {12: 9, 16: 12, 13: 5, 34: 8, 9: 9, 23: 4, 81: 2, 80: 20, 8: 1, 19: 19, 2: 2, 22: 13, 20: 7, 26: 11, 4: 1, 6: 2, 27: 4, 3: 1, 24: 12}
    target_sum = 346
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
