import networkx
import time
import random
import gzip
import sys

import matplotlib.pyplot as plt

from connected_components import connected_components
from alternative_connected import alternative_connected, alternative_dfs
from third_connected_components import adjacency, dfs, connected_components_util, third_connected_components


def mk_instance(n, k, r):
    """Set random seed to 'r' and create a graph withn 'n' vertices and (up to) n * k edges."""
    random.seed(r)
    V = list(range(0,n)) #ALTERADO PARA COMEÇAR COM VERTICES EM 0
    E = set()
    for _ in range(n*k):
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)
        if i != j:
            i, j = min(i,j), max(i,j)
            E.add((i,j))
    return V, E


def write_instance(V, E, filename):
    """Write a graph instance to a file (loosely, in a format used in DIMACS challenges)."""
    with open(filename, "w") as f:
        f.write(f"Nodes {n}\n")
        f.write(f"Edges {len(E)}\n")
        for (i,j) in E:
            f.write(f"E {i} {j}\n")


def read_instance(filename):
    """Read a graph from a file."""
    try:
        if len(filename)>3 and filename[-3:] == ".gz":  # file compressed with gzip
            import gzip
            f = gzip.open(filename, "rt")
        else:   # usual, uncompressed file
            f = open(filename)
    except IOError:
        print("could not open file", filename)
        exit(-1)

    edges = set()
    for line in f:
        if line[0:6].lower() == 'edges ':
            e, n_edges = line.split()
            n_edges = int(n_edges)
        elif line[0:6].lower() == 'nodes ':
            e, n_nodes = line.split()
            n_nodes = int(n_nodes)
        elif line[0:2].lower() == 'e ':
            e, i, j = line.split()
            i, j = int(i), int(j)
            i, j = min(i,j), max(i,j)
            edges.add((i,j))
    f.close()

    assert n_edges == len(edges)
    vertices = list(range(1,n_nodes+1))
    return vertices, list(edges)


if __name__ == "__main__":
    results1 = []
    results2 = []
    results3 = []
    sys.setrecursionlimit(1000000) #needed for both our methods, otherwise RecursionError: maximum recursion depth exceeded
    #print(sys.getrecursionlimit())
    for n in [100, 1000, 10000, 100000, 1000000]:
        for k in [1, 2, 5, 10]:
            for r in range(1,2): #11 #para testar em 10 grafos diferentes com a mesma combinação n,k (nº edges não tem de ser necessariamente igual
                # # uncomment for creating benchmark set in memory and solving with 'default' method:
                V, E = mk_instance(n, k, r)
                print("Size: ", (len(V),len(E)))
                start = time.process_time()
                res1 = connected_components(V,E)
                end = time.process_time()
                results1.append(end-start)
                cpu = end - start
                print(f"1st method: {cpu} seconds")
                
                #start = time.process_time()
                #res2 = alternative_connected(V,E)
                #end = time.process_time()
                #results2.append(end-start)
                #cpu = end - start
                #print(f"2nd method: {cpu} seconds")
                
                start = time.process_time()
                res3 = third_connected_components(V,E)
                end = time.process_time()
                results3.append(end-start)
                cpu = end - start
                print(f"3rd method: {cpu} seconds")
