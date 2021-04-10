"""Route Map Graph."""

from time import time
from math import sqrt
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
        """Add and return a new vertex into the route map.

        Args:
            element (any): The data associated with the vertex.
            coordinates (tuple): Pair of geographic coordinates of the vertex.
        """
        vertex = super().add_vertex(element)
        self._coords[vertex] = coordinates
        return vertex

    def remove_vertex(self, v):
        """Remove vertex v and all incident edges on it.

        Args:
            v (Vertex): Vertex to be removed.
        """
        super().remove_vertex(v)
        if v in self._coords:
            del self._coords[v]

    def get_coordinates(self, v):
        """Return the coordinates of the vertex or None if not in the graph.

        Args:
            v (Vertex): Vertex to get the coordinates of.
        """
        try:
            coordinates = self._coords[v]
        except KeyError:
            coordinates = None
        return coordinates

    def distance(self, c1, c2):
        """Return the distance between coordinates c1 and c2.

        Args:
            c1 (tuple): First coordinate pair.
            c2 (tuple): Second coordinate pair.
        """
        lat1, lon1 = c1[0], c1[1]
        lat2, lon2 = c2[0], c2[1]
        distance = sqrt(((lat2-lat1) ** 2) + ((lon2-lon1) ** 2))
        return distance

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
        """Print the path with the coordinates and cost of each step.

        Args:
            path (list): A list with the vertices on a path.
        """
        print("type\tlatitude\tlongitude\telement\tcost")
        for step in path:
            vertex, cost = step[0], step[1]
            coordinates = self._coords[vertex]
            lat = coordinates[0]
            lon = coordinates[1]
            elt = vertex.element()
            print("W\t{}\t{}\t{}\t{}".format(lat, lon, elt, cost))

    def save_path_to_file(self, path, filename):
        """Write the path with the coordinates and cost of each step to a file.

        Args:
            path (list): A list with the vertices on a path.
            filename (str): Name of the output file.
        """
        filename += ".txt"
        with open(filename, "w") as file:
            file.write("type\tlatitude\tlongitude\telement\tcost\n")
            for step in path:
                vertex, cost = step[0], step[1]
                coordinates = self._coords[vertex]
                lat = coordinates[0]
                lon = coordinates[1]
                elt = vertex.element()
                file.write("W\t{}\t{}\t{}\t{}\n".format(lat, lon, elt, cost))

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
            verts = self.num_vertices()
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
            edges = self.num_edges()
            print("Read {} edges, added {} into graph".format(count, edges))
        end = time()
        total_time = round((end - start), 4)
        print("Time to build graph {}s".format(total_time))
        print("-" * 25, "\n")


def main():
    routemap = RouteMap("corkCityData.txt")

    ids = {}
    ids["wgb"] = 1669466540
    ids["turnerscross"] = 348809726
    ids["neptune"] = 1147697924
    ids["cuh"] = 860206013
    ids["oldoak"] = 358357
    ids["gaol"] = 3777201945
    ids["mahonpoint"] = 330068634

    paths = [("wgb", "neptune"), ("oldoak", "cuh"), ("gaol", "mahonpoint"),
             ("mahonpoint", "wgb")]

    for path in paths:
        source = path[0]
        destination = path[1]
        source_vertex = routemap.get_vertex_by_label(ids[source])
        dest_vertex = routemap.get_vertex_by_label(ids[destination])

        start = time()
        tree = routemap.sp(source_vertex, dest_vertex)
        end = time()

        path_str = "{}->{}".format(source, destination)
        routemap.print_path(tree)
        # routemap.save_path_to_file(tree, path_str)
        path_time = round((end - start), 4)
        print("\nTime to get path from {}: {}s\n".format(path_str, path_time))


if __name__ == "__main__":
    main()
