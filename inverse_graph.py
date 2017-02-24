# Write a function inverse_graph which takes as its input the
# adjacency matrix of a graph and returns the adjacency matrix
# of the inverse graph.

def inverse_graph(graph):
    u = []
    i = len(u)
    for f in graph:
         u.append(f)
    for x in range(len(u)):
        i = i - 1
        if u[x][i] != 0:
            for y in range(len(u[x])):
                u[x][y] = 0
        else:
            for y in range(len(u[x])):
                u[x][y] = 0
                if u[x][i] == 0:
                    u[x][i] = 1
    return u

def test():
    g1 = [[0, 1, 1, 0],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [0, 1, 1, 0]]
    assert inverse_graph(g1) == [[0, 0, 0, 1],
                                 [0, 0, 1, 0],
                                 [0, 1, 0, 0],
                                 [1, 0, 0, 0]]
    g2 = [[0, 1, 1, 1],
          [1, 0, 1, 1],
          [1, 1, 0, 1],
          [1, 1, 1, 0]]
    assert inverse_graph(g2) == [[0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0]]
