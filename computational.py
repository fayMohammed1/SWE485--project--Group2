import time
from implementation import A_star_map_coloring
from testCases import scenarios

for name, graph in scenarios.items():
    start_time = time.time()  
    solution = A_star_map_coloring(graph) 
    end_time = time.time()  
   
    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"{name}: {'Solution found with colors in' if solution else 'No solution'} {elapsed_time_ms} ms \n")
    

