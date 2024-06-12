
import heapq

def initialize():
    coins = [69, 32, 32, 6, 19, 13, 21, 68, 32, 16, 21, 29, 20, 13, 21, 24, 26, 5, 23, 18, 16, 24, 2, 17, 15, 30, 26]
    tax_values = {30: 3, 20: 11, 24: 15, 26: 6, 68: 2, 29: 5, 13: 2, 2: 1, 17: 2, 32: 11, 18: 4, 15: 9, 5: 3, 21: 11, 69: 19, 6: 3, 16: 4, 23: 17, 19: 15}
    target_sum = 322
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
