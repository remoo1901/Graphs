"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """

        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Error vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = []
        queue.append(starting_vertex)

        visited = set()

        while len(queue) > 0:
            current_vertex = queue.pop(0)

            if current_vertex not in visited:
                print(current_vertex)

                visited.add(current_vertex)

                for neighbor in self.get_neighbors(current_vertex):
                    queue.append(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = []
        stack.append(starting_vertex)

        visited = set()

        while len(stack) > 0:
            current_vertex = stack.pop()

            if current_vertex not in visited:
                print(current_vertex)

                visited.add(current_vertex)

                for neighbor in self.get_neighbors(current_vertex):
                    stack.append(neighbor)

        print("===============")

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor)

        print("====")

   # this algorithm does BFT until we find the goal vertex, and returns an array of vertex IDs that are part of the path
    def bfs(self, starting_vertex_id, target_vertex_id):
        # Create an empty queue and Add a PATH TO starting vertex
        # I.e add array [1] to the queue
        queue = [[starting_vertex_id]]

        # create visited set (its empty for now)
        visited = set()
        # while queue is not empty:
        while len(queue) > 0:

            # dequeue the current PATH from the queue
            current_path = queue.pop(0)

            # get the current vertex to analyze from the path
            # use the vertex at the END of the path array
            current_vertex = current_path[-1]

            # if vertex not visited:
            if current_vertex not in visited:

                # add vertex to visited list
                visited.add(current_vertex)

                # CHECK IF CURRENT VERTEX IS THE TARGET VERTEX
                if current_vertex == target_vertex_id:
                    return current_path
                    # we found our vertex, and the path to it
                    # return the PATH
                # for each neighbor of current vertex
                    # Add the path to that neighbor, to the queue

                for neighbor in self.get_neighbors(current_vertex):
                    # COPY THE CURRENT PATH
                    current_path_copy = list(current_path)
                    # add neighbor to new path
                    current_path_copy.append(neighbor)
                    # add the whole path to the Queue
                    queue.append(current_path_copy)

        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = [[starting_vertex]]

        visited = set()

        while len(stack) > 0:
            current_path = stack.pop()

            current_vertex = current_path[-1]

            if current_vertex not in visited:
                visited.add(current_vertex)

                if current_vertex == destination_vertex:
                    return current_path

                for neighbor in self.get_neighbors(current_vertex):
                    current_path_copy = list(current_path)
                    current_path_copy.append(neighbor)
                    stack.append(current_path_copy)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
