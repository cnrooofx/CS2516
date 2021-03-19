"""Classes that make up an Undirected Graph ADT."""


class Vertex:
    """Class to represent a Vertex as part of a Graph."""

    def __init__(self, element):
        """Initialise a new vertex.

        Args:
            element (any): The data associated with the vertex.
        """
        self._element = element

    def __str__(self):
        """Return the string representation of the vertex."""
        return str(self._element)

    def __lt__(self, other):
        """Return True if the vertex is less than the other, otherwise False.

        Args:
            other (Vertex): The vertex to compare with.
        """
        return self._element < other.element()

    def element(self):
        """Return the element associated with the vertex."""
        return self._element


class Edge:
    """Class to represent an Edge between two vertices in a Graph."""

    def __init__(self, v1, v2, element):
        """Initialise a new edge.

        Args:
            v1 (Vertex): The first vertex in the edge.
            v2 (Vertex): The second vertex in the edge.
            element (any): The data associated with the edge.
        """
        self._v1 = v1
        self._v2 = v2
        self._element = element

    def __str__(self):
        """Return a string representation of the edge."""
        return "({} -- {} : {})".format(self._v1, self._v2, self._element)

    def element(self):
        """Return the element associated with the edge."""
        return self._element

    def vertices(self):
        """Return the pair of vertices in the edge."""
        return (self._v1, self._v2)

    def start(self):
        """Return the first vertex in the ordered pair."""
        return self._v1

    def end(self):
        """Return the second vertex in the ordered pair."""
        return self._v2

    def opposite(self, v):
        """If the edge is incident on 'v', return the other vertex."""
        if v == self._v1:
            return self._v2
        elif v == self._v2:
            return self._v1
        return None


class Graph:
    """Class to represent an Undirected Graph."""

    def __init__(self):
        """Initialise a new graph."""
        self._adj_map = {}

    def __str__(self):
        """Return a string representation of the graph."""
        summary = "|V| = {}; |E| = {}".format(
            self.num_vertices(), self.num_edges())
        vertex_str = "\n\nVertices: "
        for vertex in self._adj_map:
            vertex_str += str(vertex) + "-"
        edges = self.edges()
        edge_str = "\n\nEdges: "
        for edge in edges:
            edge_str += str(edge) + " "
        return summary + vertex_str + edge_str

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
        """Return the edge between v1 and v2, if any.
        
        Args:
            v1 (Vertex): The first vertex in the edge.
            v2 (Vertex): The second vertex in the edge.
        """
        try:
            edge = self._adj_map[v1][v2]
        except KeyError:
            edge = None
        return edge

    def get_edges(self, v):
        """Return a list of all the edges incident on v, if any.
        
        Args:
            v (Vertex): The vertex to get the edges of.
        """
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
        """Return the degree of vertex v.
        
        Args:
            v (Vertex): The vertex to get the degree of.
        """
        return len(self._adj_map[v])

    def get_vertex_by_label(self, element):
        """Return the first vertex that matches element.
        
        Args:
            element (Element): The element to search for.
        """
        for vertex in self._adj_map:
            if vertex.element() == element:
                return vertex
        return None

    def add_vertex(self, element):
        """Add and return a new vertex.
        
        Args:
            element (any): The data associated with the vertex.
        """
        vertex = Vertex(element)
        self._adj_map[vertex] = {}
        return vertex

    def add_vertex_if_new(self, element):
        """Add and return a new vertex. If it already exists, return that.
        
        Args:
            element (any): The data associated with the vertex.
        """
        for vertex in self._adj_map:
            if vertex.element() == element:
                return vertex
        return self.add_vertex(element)

    def add_edge(self, v1, v2, element):
        """Add and return an edge between vertices v1 and v2.

        Only adds the edge if both vertices are already in the graph.

        Args:
            v1 (Vertex): The first vertex in the edge.
            v2 (Vertex): The second vertex in the edge.
            element (any): The data associated with the edge.
        """
        if v1 not in self._adj_map or v2 not in self._adj_map:
            return None
        new_edge = Edge(v1, v2, element)
        self._adj_map[v1][v2] = new_edge
        self._adj_map[v2][v1] = new_edge
        return new_edge

    def remove_vertex(self, v):
        """Remove vertex v and all incident edges on it.
        
        Args:
            v (Vertex): Vertex to be removed.
        """
        if v in self._adj_map:
            for vertex in self._adj_map[v]:
                del self._adj_map[vertex][v]
            del self._adj_map[v]

    def remove_edge(self, e):
        """Remove edge e.
        
        Args:
            e (Edge): Edge to be removed.
        """
        v1 = e.start()
        v2 = e.end()
        del self._adj_map[v1][v2]
        del self._adj_map[v2][v1]
