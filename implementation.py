from queue import PriorityQueue


def A_star_map_coloring(map):
    open_set = PriorityQueue()
    initial_state = generate_initial_state(map)
    open_set.put((0, initial_state))  

    while not open_set.empty():
        _, current_state = open_set.get()

        if is_goal_state(current_state, map):
            return current_state  

        for neighbor in get_neighbors(current_state, map):
            new_cost = cost_of(current_state) + 1  

            if neighbor not in open_set.queue or new_cost < cost_of(neighbor):
                open_set.put((new_cost, neighbor))  

    return None  



def generate_initial_state(map):
    return ['-1' for _ in range(len(map))]  
def is_goal_state(state, map):

    for i, neighbors in enumerate(map):
        for neighbor in neighbors:
            if state[i] == state[neighbor]:  
                return False
    return all(color != '-1' for color in state)

def get_neighbors(current_state, map):
    neighbors = []
    for i, color in enumerate(current_state):
        if color == '-1':  
            for new_color in get_possible_colors(i, current_state, map):
                new_state = current_state[:]
                new_state[i] = new_color
                neighbors.append(new_state)
            break  
    return neighbors

def get_possible_colors(region_index, state, map):
    colors=["green", "red", "blue"]
    used_colors = set(state[neighbor] for neighbor in map[region_index])
    return [colors[color] for color in range(3) if str(color) not in used_colors]


def cost_of(state):

    return len(set(state)) - (1 if '-1' in state else 0)

