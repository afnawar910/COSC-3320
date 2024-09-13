from dfs import dfs
def dfs_cut_edges(graph, start_node):
  """
  Finds cut-edges (bridges) in the graph using DFS.
  input:
      graph (dict)
      start_node
 output:
      list: A list of cut-edges
  """
  dfs_result = dfs(graph, start_node)
  visited_nodes = dfs_result['visited_nodes']
  dfs_num = dfs_result['dfs_num']
  parent_nodes = dfs_result['parent_nodes']
  low_num = dfs_result['low_num']

  cut_edges = []

  for node in visited_nodes:
      for neighbor in graph.get(node, []):
          if dfs_num[node] < low_num[neighbor]:  # Check if it's a cut-edge
              cut_edge = tuple(sorted((node, neighbor)))
              if cut_edge not in cut_edges:
                  cut_edges.append(cut_edge)

  return cut_edges