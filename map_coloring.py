# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 06:02:41 2024

@author: Saadi
"""

def A_star_map_coloring(map): 
    open_set = PriorityQueue()  # Priority queue of states, prioritized by heuristic + cost 
    open_set.add((initial_state, 0))  # Add initial state with cost 0 

    while not open_set.isEmpty(): 
        current_state, cost = open_set.pop() 

        if is_goal_state(current_state): 
            return current_state  # Goal state reached 

        for neighbor in get_neighbors(current_state, map): 
            new_cost = cost + 1  # Increment cost for coloring a region 

            if neighbor not in open_set or new_cost < cost_of(neighbor): 
                open_set.add((neighbor, new_cost))  # Add neighbor to open set with new cost 

    return None  # No solution found 


    