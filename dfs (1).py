def dfs(graph, start_node):
  """
  input:
      graph (dict): A dictionary representing the graph.
                    Keys are nodes, and values are lists of adjacent nodes.
      start_node

  output:
      dict: Dictionary containing DFS traversal information:
          - 'visited_nodes'
          - 'dfs_num'
          - 'parent_nodes'
          - 'low_num'
  """
  visited_nodes = set()
  dfs_num = {}
  parent_nodes = {}
  low_num = {}
  count = [0]  # Use a list to emulate nonlocal variable

  def dfs_traverse(node):
      visited_nodes.add(node)
      dfs_num[node] = low_num[node] = count[0]
      count[0] += 1

      for neighbor in graph.get(node, []):
          if neighbor not in visited_nodes:
              parent_nodes[neighbor] = node
              dfs_traverse(neighbor)
              low_num[node] = min(low_num[node], low_num[neighbor])
          elif neighbor != parent_nodes.get(node):
              low_num[node] = min(low_num[node], dfs_num[neighbor])

  # Iterate through all nodes in the graph and start DFS from each unvisited node
  for node in graph:
      if node not in visited_nodes:
          dfs_traverse(node)

  return {
      'visited_nodes': visited_nodes,
      'dfs_num': dfs_num,
      'parent_nodes': parent_nodes,
      'low_num': low_num
  }