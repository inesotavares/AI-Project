import networkx
import time
import random
    
def connected_components(vertices, edges):
    G = networkx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(edges)
    Components = list(networkx.connected_components(G))
    # # uncomment for visualizing components:
    # print("edges:", edges)
    # for c in Components:   
    #     print(f"\t{c}")
    return len(Components)


if __name__ == "__main__":
    n = 10
    prob = 0.10
    V = list(range(1,n+1))
    E = [(i,j) for i in V for j in V if i < j and random.random() < prob]
    print("vertices:", V)
    print("edges:", E)

    # (not required) graph as adjacency list:
    graph = {i: [j for j in V if j != i and (i,j) in E or (j,i) in E] for i in V}
    print("graph as adjacency list:", graph)

    start = time.process_time()
    print("number of connected components:", connected_components(V,E))
    end = time.process_time()
    print(f"CPU time used: {end - start:g} seconds")
