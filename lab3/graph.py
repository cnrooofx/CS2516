"""Classes that make up an Undirected Graph ADT."""


class Vertex:
    """Class to represent a Vertex as part of a Graph."""

    def __init__(self, element):
        self._element = element

    def __str__(self):
        return str(self._element)

    def __lt__(self, other):
        return self._element < other.element()

    def element(self):
        return self._element


class Edge:
    """Class to represent an Edge between two vertices in a Graph."""

    def __init__(self, v1, v2, label):
        self._label = label
        self._v1 = v1
        self._v2 = v2

    def __str__(self):
        return "({} -- {} : {})".format(self._v1, self._v2, self._label)

    def element(self):
        return self._label

    def vertices(self):
        """Return the pair of vertices in the edge."""
        return (self._v1, self._v2)

    def start(self):
        """Return the first vertex in the ordered pair."""
        return self._v1

    def end(self):
        """Return the second vertex in the ordered pair."""
        return self._v2

    def opposite(self, vertex):
        if vertex == self._v1:
            return self._v2
        elif vertex == self._v2:
            return self._v1
        return None


class Graph:
    """Class to represent an Undirected Graph."""
    def __init__(self):
        """Initialise a new Graph."""
        self._adj_map = {}
    
    def __str__(self):
        """Return a string representation of the graph."""
        return "graph"
    
    def vertices(self):
        """Return a list of all the vertices in the graph."""
        return [vertex for vertex in self._adj_map]
    
    def edges(self):
        """Return a list of all the edges in the graph."""
        edge_list = []
        for v1 in self._adj_map:
            for v2 in self._adj_map[v1]:
                edge = self._adj_map[v1][v2]
                if edge.start() == v1:
                    edge_list.append(edge)
        return edge_list
    
    def num_vertices(self):
        """Return the total number of vertices in the graph."""
        return len(self._adj_map)
    
    def num_edges(self):
        """Return the total number of edges in the graph."""
        total = 0
        for vertex in self._adj_map:
            total += len(self._adj_map[vertex])
        return total // 2

    def get_edge(self, v1, v2):
        """Return the edge between v1 and v2, if any."""
        try:
            edge = self._adj_map[v1][v2]
        except KeyError:
            edge = None
        return edge
    
    def get_edges(self, v):
        """Return a list of all the edges incident on v, if any."""
        if v in self._adj_map:
            edges = []
            vertices = self._adj_map[v]
            for vertex in vertices:
                edge = vertices[vertex]
                if edge.start() == v:
                    edges.append(edge)
            return edges
        return None
    
    def degree(self, v):
        """Return the degree of vertex v."""
        return len(self._adj_map[v])
    
    def get_vertex_by_label(self, element):
        """Return the first vertex that matches element."""
        for vertex in self._adj_map:
            if vertex.element() == element:
                return vertex
        return None

    def add_vertex(self, label):
        """Add and return a new vertex."""
        vertex = Vertex(label)
        self._adj_map[vertex] = {}
        return vertex

    def add_vertex_if_new(self, element):
        for vertex in self._adj_map:
            if vertex.element() == element:
                return vertex
        return self.add_vertex(element)

    def add_edge(self, v1, v2, label):
        """Add and return an edge between vertices v1 and v2 with a label."""
        new_edge = Edge(v1, v2, label)
        self._adj_map[v1][v2] = new_edge
        self._adj_map[v2][v1] = new_edge
        return new_edge
    
    def remove_vertex(self, v):
        """Remove vertex v and all incident edges on it."""
        if v in self._adj_map:
            for vertex in self._adj_map[v]:
                del self._adj_map[vertex][v]
            del self._adj_map[v]
    
    def remove_edge(self, e):
        """Remove edge e."""
        v1 = e.start()
        v2 = e.end()
        del self._adj_map[v1][v2]
        del self._adj_map[v2][v1]


def main():
    graph = Graph()
    with open("usa.txt", "r") as file:
        for line in file:
            data = line.split()
            state1 = data[0]
            state2 = data[1]
            label = "{} - {}".format(state1, state2)
            v1 = graph.add_vertex_if_new(state1)
            v2 = graph.add_vertex_if_new(state2)
            graph.add_edge(v1, v2, label)
    print(graph.num_vertices())
    print(graph.num_edges())

    ny = graph.get_vertex_by_label("NY")
    ma = graph.get_vertex_by_label("MA")
    print("degree of ny", graph.degree(ny))
    print("degree of ma", graph.degree(ma))
    print(graph.get_edge(ny, ma))
    graph.remove_vertex(ny)
    print("degree of ma", graph.degree(ma))
    print(graph.get_edge(ny, ma))



if __name__ == "__main__":
    main()
