from graph import Graph

class RouteMap(Graph):
    """Graph to represent a road map."""

    def __init__(self):
        """Initialise a new RouteMap."""
        super().__init__()
        self._coords = {}
    
    def __str__(self):
        """Return a string representation of the route map."""
        if self.num_edges() > 100 or self.num_vertices() > 100:
            return "Too Many Vertices or Edges to print"
        return super().__str__()

    def add_vertex(self, element, coordinates):
        """Add a new vertex into the route map with a pair of coordinates."""
        vertex = super().add_vertex(element)
        self._coords[vertex] = coordinates
        return vertex

    def sp(self, v, w):
        """Get the shortest path from vertex v to w.

        Args:
            v (Vertex): Start vertex in the path.
            w (Vertex): End vertex in the path.

        Returns:
            A list of the vertices on the path from v to w with their costs.
        """
        shortest_paths = self.shortest_paths(v)
        path = []
        target = w

        while target is not None:
            data = shortest_paths[target]
            cost, predecessor = data[0], data[1]
            path.append((target, cost))
            target = predecessor
        path.reverse()
        return path


def read_route_graph(filename):
    graph = RouteMap()
    with open(filename, "r") as file:
        entry = file.readline()
        count = 0
        while entry == "Node\n":
            count += 1
            nodeid = int(file.readline().split()[1])
            gps = file.readline().split()
            latitude = round(float(gps[1]), 6)
            longitude = round(float(gps[2]), 6)
            coordinates = (latitude, longitude)
            graph.add_vertex(nodeid, coordinates)
            entry = file.readline()
        verts = len(graph.vertices())
        print("Read {} vertices and added {} into graph".format(count, verts))
        count = 0
        while entry == "Edge\n":
            count += 1
            source = int(file.readline().split()[1])
            sv = graph.get_vertex_by_label(source)
            target = int(file.readline().split()[1])
            tv = graph.get_vertex_by_label(target)
            file.readline()  # Length
            time = float(file.readline().split()[1])
            file.readline()  # Oneway
            entry = file.readline()
            graph.add_edge(sv, tv, time)
        edges = len(graph.edges())
        print("Read {} edges and added {} into graph".format(count, edges))
    print(graph, "\n")
    return graph


def main():
    graph = read_route_graph("testfiles/simpleroute.txt")


if __name__ == "__main__":
    main()
