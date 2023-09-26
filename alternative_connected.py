def alternative_dfs(V, E, node=0, visited=None, stack=None):
    if visited is None:
        visited = set()
    if stack is None:
        stack = []

    visited.add(node)

    for edge in E:
        if (edge[0] == node) and (edge[1] not in visited) and (edge[1] not in stack):
            stack.append(edge[1])
        elif (edge[1] == node) and (edge[0] not in visited) and (edge[0] not in stack):
            stack.append(edge[0])

    if stack:
        next_node = stack.pop()
        return alternative_dfs(V, E, next_node, visited, stack)

    #return (node, list(visited), stack)
    return list(visited)


def alternative_connected(V,E):
    '''
    Code is built for graphs with integer nodes from 0 to n
    '''
    component_count = 0
    connected_components = []
    visited = [False for v in range(len(V))]

    for v in V:
        if visited[v]==False:
            connected=alternative_dfs(V,E,node=v) #find connected component starting from this node
            for el in connected:
                visited[el]=True
            if len(connected) > 1: #not considering isolated nodes
                connected_components.append(connected)
                component_count += 1
    return connected_components, component_count

# Example usage:
#V = [0,1,2,3,4,5]
#E = [(0,1),(0,2),(0,3),(2,3),(2,4)]

#print(alternative_dfs(V,E,node=2))
#print(alternative_connected(V,E))
