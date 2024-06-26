# GraphModels

GraphModels is a Python package providing implementations of optimization algorithms for networks, including [pathfinding problem](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_plus_court_chemin) and scheduling problem like [Project management](https://en.wikipedia.org/wiki/Project_management).

- [Why GraphModels?](#why-graphmodels)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [GraphModels In The Wild](#graphmodels-in-the-wild)
- [Thanks](#thanks)

## Why GraphModels?

GraphModels is designed to offer efficient and easy-to-use implementations of essential optimization algorithms for network-related problems. Whether you need to find the shortest path in a graph or manage project schedules effectively, GraphModels provides robust solutions.

GraphModels offers several compelling reasons to use it:

- **Optimization Algorithms**: Provides implementations of optimization algorithms for networks, including pathfinding algorithms like [Dijkstra's algorithm](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra).

- **Scheduling Solutions**: Includes algorithms for scheduling problems such as [Pert algorithm](https://en.wikipedia.org/wiki/Program_evaluation_and_review_technique), useful in project management.

- **Ease of Use**: Designed for simplicity with "batteries included," while still allowing easy customization of key methods.

- **JSON Serialization**: Models can be serialized to JSON, enabling caching and efficient storage of results.

- **Pure Python Implementation**: Relies only on pure-Python libraries, minimizing external dependencies.

- **Python Compatibility**: Tested on Python versions 3.7, 3.8, 3.9, and 3.10, ensuring compatibility across recent Python releases.

By leveraging these features, GraphModels provides a robust framework for solving network optimization and scheduling problems with ease and efficiency.

## Installation

To install GraphModels, simply use pip:

```bash
pip install GraphModels

## Basic Usage
### Dijkstra algorithm

```python
from GraphModels.DijkstraAlgorithm import DijkstraAlgorithm

# Create an instance of Dijkstra's algorithm
dijkstra = DijkstraAlgorithm()

# Example usage: find the shortest path in a graph
shortest_path = dijkstra.final_solution()
print("Shortest path:", shortest_path)
# For the visualization of the solution 
print(dijkstra.visualization())
```

### Bellman algorithm

```python
from GraphModels.BellmanAlgorithm import BellmanAlgorithm

# Create an instance of Dijkstra's algorithm
bellman = BellmanAlgorithm()

# Example usage: find the shortest path in a graph
shortest_path = bellman.final_solution()
print("Shortest path:", shortest_path)
# For the visualization of the solution 
print(bellman.visualization())
```

### Pert algorithm


```python
from GraphModels.PertAlgorithm import PertAlgorithm

# Create an instance of Pert algorithm
pert = PertAlgorithm()

# Example usage: manage project schedules
earliest_dates = pert.date_au_plutot()
latest_dates = pert.date_au_plus_tard()
critical_path = pert.chemin_critique()
print("Earliest dates:", earliest_dates)
print("Critical path:", critical_path)
```
