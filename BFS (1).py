from collections import deque
def bfs(graph, start_node):
    """
    input:
        graph (dict): A dictionary representing the graph as an adjacency list.
        start_node
    output:
        dict: A dictionary containing the following information:
            distances
            parent_nodes
            visited
    """
    distances = {}
    parents = {}
    visited = set()

    bfs_traversal_list(graph, start_node, distances, parents, visited)

    # Visit disconnected components
    for node in graph:
        if node not in visited:
            bfs_traversal_list(graph, node, distances, parents, visited)

    return {
        'distances': distances,
        'parents': parents,
        'visited': visited
    }

def bfs_traversal_list(graph, start_node, distances, parents, visited):
    queue = deque([(start_node, 0)])
    visited.add(start_node)
    distances[start_node] = 0

    while queue:
        current_node, current_distance = queue.popleft()

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = current_distance + 1
                parents[neighbor] = current_node
                queue.append((neighbor, current_distance + 1))