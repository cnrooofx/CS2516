"""Route Map Graph."""

from time import time
from graph import Graph


class RouteMap(Graph):
    """Graph to represent a road map."""

    def __init__(self, filename=None):
        """Initialise a new RouteMap, optionally from a file.
        
        Args:
            filename (str): Path to the file containing the graph.
                            (Default: None)
        """
        super().__init__()
        self._coords = {}

        if filename:
            self.read_route_graph(filename)

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

    def print_path(self, path):
        """Prints the path with the coordinates and cost of each step.

        Args:
            path (list): A list with the vertices on a path.
        """
        print("type\tlatitude\tlongitude\telement\tcost")
        for step in path:
            vertex, cost = step[0], step[1]
            coordinates = self._coords[vertex]
            latitude = coordinates[0]
            longitude = coordinates[1]
            elt = vertex.element()
            print("W\t{}\t{}\t{}\t{}".format(latitude, longitude, elt, cost))

    def read_route_graph(self, filename):
        """Build a route map from the given file.

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
                gps = file.readline().split()
                latitude = round(float(gps[1]), 6)
                longitude = round(float(gps[2]), 6)
                self.add_vertex(nodeid, (latitude, longitude))
                entry = file.readline()
            verts = len(self.vertices())
            print("Read {} vertices, added {} into graph".format(count, verts))
            count = 0
            while entry == "Edge\n":
                count += 1
                source = int(file.readline().split()[1])
                sv = self.get_vertex_by_label(source)
                target = int(file.readline().split()[1])
                tv = self.get_vertex_by_label(target)
                file.readline()  # Length
                edge_time = float(file.readline().split()[1])
                file.readline()  # Oneway
                entry = file.readline()
                self.add_edge(sv, tv, edge_time)
            edges = len(self.edges())
            print("Read {} edges, added {} into graph".format(count, edges))
        end = time()
        total_time = end - start
        print("Time to build graph {}s".format(total_time))


def main():
    graph = RouteMap("corkCityData.txt")

if __name__ == "__main__":
    main()
