

no_adjacencies = [[] for _ in range(4)]
linear_chain = [[1], [0, 2], [1, 3], [2]]
circle_chain = [[1, 3], [0, 2], [1, 3], [0, 2]]
star_config = [[1, 2, 3], [], [], []]
single_adjacency = [[1], [0], [], []]
complete_graph = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
slide_map= [
    [1, 2],  # WA: NT, SA
    [0, 2, 3],  # NT: WA, SA, Q
    [0, 1, 3, 4, 5],  # SA: WA, NT, Q, NSW, V
    [1, 2, 4],  # Q: NT, SA, NSW
    [2, 3, 5],  # NSW: SA, Q, V
    [2, 4, 6],  # V: SA, NSW, T
    [5]  # T: V
]

# Scenario Testing
scenarios = {
    "No Adjacencies": no_adjacencies,
    "Linear Chain": linear_chain,
    "Circle Chain": circle_chain,
    "Star Configuration": star_config,
    "Single Adjacency": single_adjacency,
    "Complete Graph": complete_graph, 
    "slide map": slide_map

}