def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in checked:
            lowest_cost = cost
            lowest_node = node
    return lowest_node

#Nodes and costs
graph = {}
graph["start"] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['end'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5
graph['end'] = {}

#known costs at the beginning
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = float('inf')

#parent nodes
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

#keep track of nodes studied
checked = []

node = find_lowest_cost_node (costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    checked.append(node)
    node = find_lowest_cost_node(costs)
