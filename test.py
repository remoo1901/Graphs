class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else: 
            print("Error vertex not found")
​
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
​
    def bft(self, starting_vertex_id):
        # Create an empty Queue and add starting vertex to it
        # This will keep track of all next_to_visit_vertices
        queue = []
        queue.append(starting_vertex_id)
        # Create an empty set to keep track of visited vertices
        visited = set()
        # While the queue is not empty
        while len(queue) > 0:
            # dequeue a vertex off the queue
            current_vertex = queue.pop(0)
​
            # if vertex not in visited vertices
            if current_vertex not in visited:
                # Print it 
                print(current_vertex)
                # Add the vertex to our visited set
                visited.add(current_vertex)
                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    queue.append(neighbor)
            
​
    def dft(self, starting_vertex_id):
        # Create an empty Stack and add starting vertex to it
        # This will keep track of all next_to_visit_vertices
        stack = []
        stack.append(starting_vertex_id)
        # Create an empty set to keep track of visited vertices
        visited = set()
        # While the queue is not empty
        while len(stack) > 0:
            # dequeue a vertex off the stack
            current_vertex = stack.pop()
​
            # if vertex not in visited vertices
            if current_vertex not in visited:
                # Print it 
                print(current_vertex)
                # Add the vertex to our visited set
                visited.add(current_vertex)
                # Add all neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    stack.append(neighbor)
            
    # this algorithm does BFT until we find the goal vertex, and returns an array of vertex IDs that are part of the path
    def bfs(self, starting_vertex_id, target_vertex_id):
        # Create an empty queue and Add a PATH TO starting vertex 
        # I.e add array [1] to the queue
        queue = [ [starting_vertex_id] ] 
        # create visited set (its empty for now)
        visited = set()
        # while queue is not empty:
        while len(queue) > 0:
            # dequeue the current PATH from the queue
            current_path = queue.pop(0)
            # get the current vertex to analyze from the path 
            # use the vertex at the END of the path array
            current_vertex = current_path[-1]
​
            # if vertex not visited:
            if current_vertex not in visited:
                # add vertex to visited list
                visited.add(current_vertex)
​
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
​
        return None
​
​
our_graph = Graph()
​
our_graph.add_vertex(1)
our_graph.add_vertex(2)
our_graph.add_vertex(3)
our_graph.add_vertex(4)
our_graph.add_vertex(5)
our_graph.add_vertex(6)
our_graph.add_vertex(7)
our_graph.add_edge(1,2)
our_graph.add_edge(2,3)
our_graph.add_edge(2,4)
our_graph.add_edge(3,5)
our_graph.add_edge(5,3)
our_graph.add_edge(4,6)
our_graph.add_edge(4,7)
our_graph.add_edge(6,3)
our_graph.add_edge(7,6)
our_graph.add_edge(7,1)
​
​
print(our_graph.vertices)
# our_graph.dft(1)
print(our_graph.bfs(1, 3))
Shared in