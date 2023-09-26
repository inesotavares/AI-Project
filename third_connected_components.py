#Auxiliary functions

def adjacency(V, E):
    adjacency_list = {vertex: [] for vertex in V}

    for edge in E:
        u, v = edge  # Assuming each edge is a tuple (u, v)
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)  # For undirected graphs, add the reverse edge as well

    return adjacency_list

def dfs(adj, node=0, visited=[], component=[]):
    visited[node] = True
    component.append(node)

    for neighbor in adj[node]:
        if visited[neighbor]==False:
            dfs(adj, neighbor, visited, component)

def connected_components_util(adj):
    num_vertices = len(adj)
    visited = [False for i in range(num_vertices)]
    components = []

    for node in range(num_vertices):
        if visited[node]==False:
            component = []
            dfs(adj, node, visited, component)
            if len(component) > 1: #discards isolated nodes, same interpretation as the networkx solution
                components.append(component)

    return components

#####
#################
#####

#Aggregate into 1 function
def third_connected_components(V,E):
    adjacency_list = adjacency(V,E)
    components = connected_components_util(adjacency_list)
    return components, len(components)
