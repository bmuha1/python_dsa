#!/usr/bin/python3
# Implement adjacency list


class Vertex:
    def __init__(self, key):
        # Initialize vertex
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, number, weight=0):
        # Add connection to another vertex
        self.connected_to[number] = weight

    def __str__(self):
        # Display vertex
        return (str(self.id) + ' connected to: ' +
                str([x.id for x in self.connected_to]))

    def get_connections(self):
        # Return all the vertices in the adjacency list
        return self.connected_to.keys()

    def get_id(self):
        # Return the id
        return self.id

    def get_weight(self, number):
        # Return the weight
        return self.connected_to[number]


class Graph:
    def __init__(self):
        # Initialize graph
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        # Add vertex
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        # Return vertex with given key
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        # Check if key is in graph
        return n in self.vert_list

    def add_edge(self, f, t, weight=0):
        # Add edge
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], weight)

    def get_vertices(self):
        # Return names of all the vertices in the graph
        return self.vert_list.keys()

    def __iter__(self):
        # Iterate over all vertices
        return iter(self.vert_list.values())

if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    for v in g:
        for w in v.get_connections():
            print('({}, {})'.format(v.get_id(), w.get_id()))
