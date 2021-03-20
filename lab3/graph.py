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
        self._edge = (v1, v2)
        self._element = element

    def __str__(self):
        """Return a string representation of the edge."""
        return "({} -- {} : {})".format(self._edge[0], self._edge[1], self._element)

    def element(self):
        """Return the element associated with the edge."""
        return self._element

    def vertices(self):
        """Return the pair of vertices in the edge."""
        return self._edge

    def start(self):
        """Return the first vertex in the ordered pair."""
        return self._edge[0]

    def end(self):
        """Return the second vertex in the ordered pair."""
        return self._edge[1]

    def opposite(self, v):
        """If the edge is incident on 'v', return the other vertex."""
        if v == self._edge[0]:
            return self._edge[1]
        elif v == self._edge[1]:
            return self._edge[0]
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
                edges.append(vertices[vertex])
            return edges
        return None

    def degree(self, v):
        """Return the degree of vertex v.
        
        Args:
            v (Vertex): The vertex to get the degree of.
        """
        return len(self._adj_map[v])

    def highest_degree(self):
        """Return the vertex with highest degree."""
        highest_degree = -1
        highest_vertex = None
        for vertex in self._adj_map:
            if self.degree(vertex) > highest_degree:
                highest_degree = self.degree(vertex)
                highest_vertex = vertex
        return highest_vertex

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

    def depthfirstsearch(self, v):
        """Return a dictionary of the depth-first search from v.

        Args:
            v (Vertex): The vertex to start searching from.

        Returns:
            dfs (dict): Dictionary of the depth-first search.
        """
        dfs = {v: None}
        self._depthfirstsearch(v, dfs)
        return dfs

    def _depthfirstsearch(self, v, marked):
        for edge in self.get_edges(v):
            opposite = edge.opposite(v)
            if opposite not in marked:
                marked[opposite] = edge
                self._depthfirstsearch(opposite, marked)

    def breadthfirstsearch(self, v):
        """Return a dictionary of the breadth-first search from v.

        Args:
            v (Vertex): The vertex to start searching from.
        
        Returns:
            bfs (dict): Dictionary of the breadth-first search.
        """
        bfs = {v: (None, 0)}
        layer = [v]
        i = 1
        self._breadthfirstsearch(i, layer, bfs)
        return bfs

    def _breadthfirstsearch(self, i, layer, marked):
        next_layer = []
        for vertex in layer:
            for edge in self.get_edges(vertex):
                opposite = edge.opposite(vertex)
                if opposite not in marked:
                    marked[opposite] = (edge, i)
                    next_layer.append(opposite)
        if len(next_layer) > 0:
            i += 1
            self._breadthfirstsearch(i, next_layer, marked)

    def max_distance(self, bfs):
        """Return the max distance to a vertex from a breadth-first search.

        Args:
            bfs (dict): The result of a breadth-first search from a vertex.

        Returns:
            max_distance (int): The maximum number of steps to another vertex.
        """
        max_distance = -1
        for vertex in bfs:
            distance = bfs[vertex][1]
            if distance > max_distance:
                max_distance = distance
        return max_distance

    def print_distances(self, bfs):
        """Print the paths and distances given a breadth-first search tree."""
        for vertex in bfs:
            edge, distance = bfs[vertex]
            print("V: {}, E: {}, Distance: {}".format(vertex, edge, distance))
