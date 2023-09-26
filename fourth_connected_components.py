#Auxiliary functions

def adjacency(V, E):
    adjacency_list = {vertex: [] for vertex in V}

    for edge in E:
        u, v = edge  # Assuming each edge is a tuple (u, v)
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)  # For undirected graphs, add the reverse edge as well

    return adjacency_list



class CCU:

    def __init__(self, adj):
        self.adj = adj
        self.num_vertices = len(adj)
        self.visited = [False for i in range(self.num_vertices)]
        self.component = []

    def dfs_sneaky_sneaky(self, node):
        stack = [node]
        while len(stack)>0:
            node2 = stack[-1]
            self.visited[node2] = True
            self.component.append(node2)
            new_node = False
            for neighbor in self.adj[node2]:
                if self.visited[neighbor]==False:
                    stack.append(neighbor)
                    new_node = True
                    break
            if not new_node:
                stack = stack[:-1]

    def connected_components_util(self):
        components = []

        for node in range(self.num_vertices):
            if self.visited[node]==False:
                #print("ccu ", node)
                self.component = []
                self.dfs_sneaky_sneaky(node)
                #if len(self.component) > 1: #discards isolated nodes, same interpretation as the networkx solution
                components.append(self.component)

        return components

#####
#################
#####

#Aggregate into 1 function
def fourth_connected_components(V,E):
    adjacency_list = adjacency(V,E)
    ccu = CCU(adjacency_list)
    components = ccu.connected_components_util()
    return components, len(components)
