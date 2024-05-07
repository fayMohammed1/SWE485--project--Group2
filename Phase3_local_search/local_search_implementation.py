import random

def local_search(map, max_iterations=1000):
    current_state = generate_initial_state(map)
    best_state = current_state[:]
    best_cost = cost_of(current_state)

    for _ in range(max_iterations):
        neighbor = get_random_neighbor(current_state, map)
        if neighbor is None:
            continue

        neighbor_cost = cost_of(neighbor)
        
        if neighbor_cost < best_cost:
            best_state = neighbor[:]
            best_cost = neighbor_cost
        
        current_state = neighbor[:]  # Move to the neighbor regardless of whether it's better

    return best_state

def get_random_neighbor(current_state, map):
    neighbors = []
    for i, color in enumerate(current_state):
        if color == '-1':
            possible_colors = get_possible_colors(i, current_state, map)
            if possible_colors:
                new_color = random.choice(possible_colors)
                neighbor = current_state[:]
                neighbor[i] = new_color
                neighbors.append(neighbor)
    if not neighbors:
        return None
    return random.choice(neighbors)

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
