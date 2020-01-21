#
# python module for euler path for directed graphs
#
#

class Vertex(object):
    ''' vertex '''

    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return '{}'.format(self.label)

class Edge(object):
    ''' edge '''

    def __init__(self, source, destination):
        self.start = source
        self.destination = destination

    def __repr__(self):
        return ' {}->{} '.format(self.start, self.destination)

    def reverse(self):
	return Edge(self.destination, self.start)

class Graph(object):
    ''' graph '''

    def __init__(self):
        self.vertices  = list()
        self.edges_in  = dict()
        self.edges_out = dict()
        self.directed  = True

    def add_vertex(self, v):
	if v in self.vertices:
	    raise Exception('vertex already present')
        self.edges_in[v]  = list()
        self.edges_out[v] = list()
        self.vertices.append(v);

    def vertex(self, index):
	if index > self.vertices:
	    raise Exception('index out of bounds')
        return self.vertices[index]

    def add_edge(self, e):
        self.edges_out[e.start].append(e)
        self.edges_in[e.destination].append(e.reverse())

    def reverse_graph(self):
	self.r_edges_out = dict()
        for v, edges_out in self.edges_out.items():
	    for e in edges_out:
                v = e.destination
		if v not in self.r_edges_out:
		    self.r_edges_out[v] = list()
		self.r_edges_out[e.destination].append(e.reverse())

    def is_eulirean(self):
        ''' check if euler tour or path is possible for directed graph '''
        ''' directed graph is strongly connected '''

        stack = []
	start = self.vertices[0]
        visited = set()
	vc = 0

        for v in self.vertices:
	    if len(self.edges_in[v]) == len(self.edges_out[v]):
		continue
	    elif len(self.edges_in[v]) < len(self.edges_out[v]):
		beg = v
	    else:
		end = v

            vc = vc + 1
            if vc > 2:
                print v, self.edges_in[v], self.edges_out[v]
                print ('vertices with degree mismatch > 2')
                return False

	if vc > 0:
	     self.edges_in[beg].append(Edge(beg, end))
	     self.edges_out[end].append(Edge(end, beg))

        stack.append(start)

        while len(stack) > 0:
            v = stack.pop()
	    if v not in visited:
	        visited.add(v)
	        for e in self.edges_out[v]:
	            if e.destination not in visited:
		        stack.append(e.destination)
			print '{}->{}'.format(e.start, e.destination)
	    else:
		break

        if len(visited) != len(self.vertices):
	    print '{} visited:{} total_vertices:{}'.format('dfs has unvisited nodes',
		len(visited), len(self.vertices))
	    return False

        self.reverse_graph()

        visited = set()
        stack.append(start)
        while len(stack) > 0:
            v = stack.pop()
            if v not in visited:
	        visited.add(v)
                for e in self.r_edges_out[v]:
	            if e.destination not in visited:
		        stack.append(e.destination)

        if len(visited) != len(self.vertices):
	    print '{} visited:{} total_vertices:{}'.format('dfs reverse graph has unvisited nodes',
		len(visited), len(self.vertices))
            return False
	else:
	    return True, vc == 0

    def join_tours(self, cp_list):
        cp = None
        while len(cp_list) > 0:
            for c in cp_list:
                i = cp_list.index(c)
                if cp is None :
                    cp = c
                    cp_list.pop(i)
                    break
                elif cp[-1] == c[0]:
                    cp = cp + c[1:]
                    cp_list.pop(i)
                    break
                else:
                    pass
        return cp

    def euler_path(self):
        ''' print the euler path '''
        stack = []
        circuits = []
        e_visited = set()
        v_visited = set()

        # get an unvisited vertex
        for i in self.vertices:
            circuit = []

            # for euler walks, for any visited vertex
            # all paths must be visited by now
            if i in v_visited:
                continue

            stack.append(i)
            # mark current vertex visible
            v_visited.add(i)

            while len(stack) > 0:
                e_new = False
                v = stack[-1]
                # new edge
                for e in self.edges_out[v]:
                    if e not in e_visited:
                        e_new = True
                        e_visited.add(e)
                        # vertex can be revisited
                        stack.append(e.destination)
                        v_visited.add(e.destination)
                        break
                # no new edge
                if e_new is False:
                    v = stack.pop()
                    circuit.append(v)
                    for e in self.edges_out[v]:
                        if e in e_visited:
                            continue
                        e_visited.add(e)
                        # vertex can be revisited
                        stack.append(e.destination)
                        v_visited.add(e.destination)
                        break

            circuit.reverse()
            circuits.append(circuit)

        return self.join_tours(circuits)

    def print_graph(self):
	print ('Graph:')
        for v, edges_out in self.edges_out.items():
            print 'v : {} e : {}'.format(v, ''.join([ str(e) for e in edges_out ]))

    def print_reverse_graph(self):
	print ('RGraph:')
        for v, edges_out in self.r_edges_out.items():
            print 'v : {} e : {}'.format(v, ''.join([ str(e) for e in edges_out ]))

if __name__ == "__main__":
    g = Graph()
    for i in range(10):
        g.add_vertex(Vertex(i))

    for i in range(1, 10):
        g.add_edge(Edge(g.vertex(i - 1), g.vertex(i)))

    g.print_graph()
    g.reverse_graph()
    g.print_reverse_graph();
    print 'Graph eulirean  :{}'.format(g.is_eulirean())
    if g.is_eulirean():
        circuit = g.euler_path()
        path = ''
        for x in circuit:
	        path = '{} {}'.format(path, x)
        print 'euler path : {}'.format(path)
