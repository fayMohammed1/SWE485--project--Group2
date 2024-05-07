import time
from local_search_implementation import local_search
from TestCases_local import scenarios

for name, graph in scenarios.items():
    start_time = time.time()  
    solution = local_search(graph) 
    end_time = time.time()  
   
    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"{name}: {'Solution found with colors in' if solution else 'No solution'} {elapsed_time_ms} ms \n")
    