"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

***The two by two grid actually has 9 verticies***

How many such routes are there through a 20×20 grid?

There are 12 subsections in a 2x2 grid, divided by the 2 movable ways is equal to 6. Would this
formula work for 20x20? I think the answer is no.

To find all the cycles in an undirected graph use the following formula: (n - 1)! / 2
Here we want to find all the paths, not cycles in the graph, and this is a directed graph.

Will look at using depth-first search optimized for a directed acyclic graph to solve.

Solution: 137846528820

Holy hell! Learned a lot of graph theory only to realize that I was kinda boned when the problem
asked for anything higher than about 12x12.

After doing some searching on similar problems I stumbled on a blog article that showed 'opening'
the number of possible paths to each point in a graphic. A graphic that looked suspiciously like
Pascal's triangle tipped to one side. Eureka!

I had previously coded a function to find a number in Pascal's triangle given a row and column number.
The only trick was to figure how many rows to go down and how many columns over!

This is the first .py that includes a generator (I did not write this generator) and I am still
trying to understand how these work... 1/17/17
"""


from time import time


def dfs(graph, root):
    """
    A depth first search algorithm that finds a possible path thru root a given graph.

    Adapted from: http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    """


    visited = set()
    stack = [root]

    while stack:

        current = stack.pop()

        if current not in visited:
            visited.add(current)
            stack.extend(graph(current) - visited)

    return visited

def dfs_paths(graph, start, goal):
    """
    A depth first search algorithm that finds and returns all possible trails in a given graph
    from start to goal.

    From: http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    """

    stack = [(start, [start])]

    while stack:
        (vertex, path) = stack.pop()

        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]

            else:
                stack.append((next, path + [next]))

def gen_graph(x, y):
    """
    Generates a directional acyclic graph for use in this problem with any number of verticies.
    """

    graph = dict()

    for i in range(1, (x*y)+1):
        if i == (x * y):
            graph[x * y] = set()

        elif i % x == 0:
            graph[i] = set([i+x])

        elif ((x * y) - x) <= i <= ((x * y) - 1):
            graph[i] = set([i+1])
        else:
            graph[i] = set([i+1, i+x])

    return graph

graph = gen_graph(15, 15)


def pascals(r, c):
    """
    Find the integer in pascal's triangle given the coordinates (r, c) or (row #, column #)
    with the formula (r, c) = r! / c! (r - c)!
    """
    try:
        result = fac(r - 1) // (fac(c - 1) * (fac((r - 1) - (c - 1))))
    except ValueError:
        result = 'non-existant'

    return result


print(pascals(41,21))

# start = time()
# print(len(list(dfs_paths(graph, 1, 100))))
# print(round(time() - start, 4))
