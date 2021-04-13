"""Undirected Graph ADT."""

from apq import SearchableAPQ
from time import time


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

    def __eq__(self, other):
        """Return True if the vertex is equal to the other, otherwise False.

        Args:
            other (Vertex): The vertex to compare with.
        """
        if isinstance(other, Vertex):
            return self._element == other.element()
        return self._element == other

    def __lt__(self, other):
        """Return True if the vertex is less than the other, otherwise False.

        Args:
            other (Vertex): The vertex to compare with.
        """
        if isinstance(other, Vertex):
            return self._element < other.element()
        return self._element < other

    def __hash__(self):
        """Return the hash of the Vertex."""
        return hash(self._element)

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
        return "(E: {}; {} -- {})".format(self._element, self._edge[0],
                                          self._edge[1])

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
    """Undirected Graph."""

    def __init__(self, filename=None):
        """Initialise a new graph, optionally from a file.

        Args:
            filename (str): Path to the file containing the graph.
                            (Default: None)
        """
        self._adj_map = {}
        self._vertices_lookup = {}
        if filename:
            self.read_graph(filename)

    def __str__(self):
        """Return a string representation of the graph."""
        summary = "|V| = {}; |E| = {}".format(self.num_vertices(),
                                              self.num_edges())
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
        edges = []
        if v in self._adj_map:
            vertices = self._adj_map[v]
            for vertex in vertices:
                edges.append(vertices[vertex])
        return edges

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
        try:
            vertex = self._vertices_lookup[element]
        except KeyError:
            vertex = None
        return vertex

    def add_vertex(self, element):
        """Add and return a new vertex.

        Args:
            element (any): The data associated with the vertex.
        """
        vertex = Vertex(element)
        self._adj_map[vertex] = {}
        self._vertices_lookup[element] = vertex
        return vertex

    def add_vertex_if_new(self, element):
        """Add and return a new vertex. If it already exists, return that.

        Args:
            element (any): The data associated with the vertex.
        """
        if element in self._vertices_lookup:
            return self._vertices_lookup[element]
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

    def depth_first_search(self, v):
        """Return a dictionary of the depth-first search from v.

        Args:
            v (Vertex): The vertex to start searching from.
        """
        dfs = {v: None}
        self._depth_first_search(v, dfs)
        return dfs

    def _depth_first_search(self, v, marked):
        for edge in self.get_edges(v):
            opposite = edge.opposite(v)
            if opposite not in marked:
                marked[opposite] = edge
                self._depth_first_search(opposite, marked)

    def breadth_first_search(self, v):
        """Return a dictionary of the breadth-first search from v.

        Args:
            v (Vertex): The vertex to start searching from.
        """
        bfs = {v: (None, 0)}
        layer = [v]
        i = 1
        self._breadth_first_search(i, layer, bfs)
        return bfs

    def _breadth_first_search(self, i, layer, marked):
        next_layer = []
        for vertex in layer:
            for edge in self.get_edges(vertex):
                opposite = edge.opposite(vertex)
                if opposite not in marked:
                    marked[opposite] = (edge, i)
                    next_layer.append(opposite)
        if len(next_layer) > 0:
            i += 1
            self._breadth_first_search(i, next_layer, marked)

    def max_distance(self, bfs):
        """Return the max distance to a vertex from a breadth-first search.

        Args:
            bfs (dict): The result of a breadth-first search from a vertex.
        """
        max_distance = -1
        for vertex in bfs:
            distance = bfs[vertex][1]
            if distance > max_distance:
                max_distance = distance
        return max_distance

    def print_distances(self, bfs):
        """Print the paths and distances given a breadth-first search tree.

        Args:
            bfs (dict): The result of a breadth-first search from a vertex.
        """
        for vertex in bfs:
            edge, distance = bfs[vertex]
            print("V: {}, E: {}, Distance: {}".format(vertex, edge, distance))

    def central_vertex(self):
        """Return the most central vertex in the graph."""
        min_distance = None
        central = None
        vertices = self.vertices()
        if len(vertices) > 0:
            for vertex in vertices:
                bfs = self.breadth_first_search(vertex)
                max_distance = self.max_distance(bfs)
                if not min_distance or max_distance < min_distance:
                    min_distance = max_distance
                    central = vertex
        return central

    def shortest_paths(self, v):
        """Dijkstra's Algorithm for finding shortest paths to other vertices.

        Args:
            v (Vertex): Start vertex to find paths from.

        Returns:
            A dictionary with vertices as keys and (cost, predecessor) pairs
            as values.
        """
        opened = SearchableAPQ()
        closed = {}
        predecessors = {v: None}

        opened.add(0, v)
        while len(opened) > 0:
            cost, vertex = opened.remove_min()
            predecessor = predecessors.pop(vertex)

            closed[vertex] = (cost, predecessor)
            for edge in self.get_edges(vertex):
                opposite_vertex = edge.opposite(vertex)
                if opposite_vertex not in closed:
                    new_cost = cost + edge.element()
                    if opposite_vertex not in opened:
                        # Set the current vertex's predecessor
                        predecessors[opposite_vertex] = vertex
                        # Add the current vertex to opened with it's cost
                        opened.add(new_cost, opposite_vertex)
                    else:
                        element = opened[opposite_vertex]
                        old_cost = opened.get_key(element)
                        # If the new cost is better than the old cost
                        if new_cost < old_cost:
                            # Replace the old predecessor with current vertex
                            predecessors[opposite_vertex] = vertex
                            # Update the cost to current vertex in opened
                            opened.update_key(element, new_cost)
        return closed

    def read_graph(self, filename):
        """Build a graph from the given file.

        Args:
            filename (str): The path to the graph file.
        """
        start = time()
        with open(filename, "r") as file:
            entry = file.readline()
            count = 0
            while entry == "Node\n":
                count += 1
                nodeid = int(file.readline().split()[1])
                self.add_vertex(nodeid)
                entry = file.readline()
            verts = self.num_vertices()
            print("Read {} vertices, added {} into graph".format(count, verts))
            count = 0
            while entry == "Edge\n":
                count += 1
                source = int(file.readline().split()[1])
                sv = self.get_vertex_by_label(source)
                target = int(file.readline().split()[1])
                tv = self.get_vertex_by_label(target)
                length = float(file.readline().split()[1])
                self.add_edge(sv, tv, length)
                file.readline()
                entry = file.readline()
            edges = self.num_edges()
            print("Read {} edges, added {} into graph".format(count, edges))
        end = time()
        total_time = round((end - start), 4)
        print("Time to build graph {}s".format(total_time))
        print("-" * 25, "\n")


def test_shortest_paths(filename, start_vertex, end_vertex):
    """Build a graph and get the shortest path between the given vertices.

    Args:
        filename (str): The name of the graph file.
        start_vertex: The vertex to start the path from.
        end_vertex: The vertex to end the path on.

    Returns:
        The cost to get to the end vertex and it's predecessor.
    """
    graph = Graph(filename)
    start_v = graph.get_vertex_by_label(start_vertex)
    end_v = graph.get_vertex_by_label(end_vertex)
    start = time()
    paths = graph.shortest_paths(start_v)
    end = time()
    print("Time to get shortest paths {} s".format(end - start))

    for vertex, value in paths.items():
        cost, predecessor = value[0], value[1]
        print("{} -> Cost: {}, Pred: {}".format(vertex, cost, predecessor))
    result_path = paths[end_v]

    print("\n" + "*" * 25 + "\n")
    return result_path


def main():
    result = test_shortest_paths("simplegraph1.txt", 1, 4)
    cost, pred = result[0], result[1]
    assert cost == 8.0
    print(pred)

    result = test_shortest_paths("simplegraph2.txt", 14, 5)
    cost, pred = result[0], result[1]
    assert cost == 16.0
    print(pred)


if __name__ == "__main__":
    main()
