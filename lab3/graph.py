"""Class to represent an Undirected Graph."""

class Graph:
    def __init__(self):
        """Initialise a new Graph."""
        self._adj_map = {}
    
    def __str__(self):
        """Return a string representation of the graph."""
    
    def vertices(self):
        """Return a list of all the vertices."""
    
    def edges(self):
        """Return a list of all the edges."""
    
    def num_vertices(self):
        """Return the total number of vertices."""
    
    def num_edges(self):
        """Return the total number of edges."""

    def get_edge(self, v1, v2):
        """Return the edge between v1 and v2, if any."""
    
    def get_edges(self, v):
        """Return a list of the edges incident on v."""
    
    def degree(self, v):
        """Return the degree of vertex v."""

    def add_vertex(self, label):
        """Add a new vertex."""

    def add_edge(self, v1, v2, label):
        """Add a new edge between v1 and v2."""
    
    def remove_vertex(self, v):
        """Remove vertex v and all incident edges on it."""
    
    def remove_edge(self, e):
        """Remove edge e."""


def main():
    states = []
    with open("usa.txt", "r") as file:
        for line in file:
            data = line.split()
            state1 = data[0]
            state2 = data[1]
            if state1 not in states:
                states.append(state1)
            elif state2 not in states:
                states.append(state2)
    states.sort()
    for state in states:
        print(state)
    print(len(states))


if __name__ == "__main__":
    main()
