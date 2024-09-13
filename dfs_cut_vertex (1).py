from dfs import dfs
def dfs_cut_vertex(graph):
  """
  Finds cut vertices (articulation points) in a graph using DFS.
  input:
      graph:
  output:
      list: A list of cut vertices  found in the graph.
  """
  cut_vertex = []
  dfs_result = dfs(graph, next(iter(graph)))  # Start DFS from the first node

  visited_nodes = dfs_result['visited_nodes']
  dfs_num = dfs_result['dfs_num']
  parent_nodes = dfs_result['parent_nodes']
  low_num = dfs_result['low_num']

  for node in visited_nodes:
      if len(graph[node]) > 1:  # Check if the node has more than one child
          is_cut_vertex = False
          for neighbor in graph[node]:
              if low_num[neighbor] > dfs_num[node]:
                  is_cut_vertex = True
                  break
          if is_cut_vertex:
              cut_vertex.append(node)

  return cut_vertex