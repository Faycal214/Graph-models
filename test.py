from GraphModels.DijkstraAlgorithm import DijkstraAlgorithm
dijkstra = DijkstraAlgorithm()

# Example usage: find the shortest path in a graph
shortest_path = dijkstra.final_solution()
print("Shortest path:", shortest_path)
# For the visualization of the solution 
print(dijkstra.visualization())