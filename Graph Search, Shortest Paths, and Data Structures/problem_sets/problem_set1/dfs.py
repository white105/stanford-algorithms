import sys
from priodict import priority_dict

def make_graph(filename):

    try:
        f = open(filename, 'r')
    except IOError:
        sys.exit("No such file!")
    line_list = f.readlines()

    # populate the graph using data from the text file via dictionary comprehensions
    G = {int(line.split()[0]): {(int(tup.split(',')[0])): int(tup.split(',')[1])
                                for tup in line.split()[1:] if tup} for line in line_list if line}
    f.close()
    return G

def dijkstra(G, start, end=None):

    D = {}	          # dictionary of final distances
    P = {}	          # dictionary of predecessors
    Q = priority_dict()   # est.dist. of non-final vert.

    # initialize Q and P
    for vertex in G:
        Q[vertex] = float("inf")
        P[vertex] = None

    Q[start] = 0

    for v in Q: # iterate and pop the smallest item in Q
        D[v] = Q[v]
        if v == end: break # we have reached the end

        for w in G[v]: # for all of v's adjacent vertices
            vwLength = D[v] + G[v][w]
            if w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

    return D, P

def findshortestPath(G, start, end):
    """Find a single shortest path from the given start vertex to the given end vertex.
    The input has the same conventions as dijkstra().
    The output is a list of the vertices in order along
    the shortest path.
    Input: G - the input graph in the adjacency list representation via a dictionary
    start - the starting vertex
    end - the ending vertex
    Note: This method is not needed in the current exercise, however, it would be nice to know the shortest path from one vertex to another sometimes"""

    _, P = dijkstra(G, start, end)
    path = []
    while 1:
        path.append(end)
        if end == start: break
        end = P[end] # find the next predecessor
    path.reverse() # reverse the list since we are appending from the back
    return path

def main():
    G = make_graph('dijkstraData.txt')
    lst = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197] # a list of all the desired ending vertices
    for v in lst:
        D, _ = dijkstra(G, 1, v)
        if v != lst[-1]:
            print(str(D[v]) + ",")
        else:
            print(D[v])

if __name__ == '__main__':
    main()
