from node import Node

def constructGraph(vertex, edges):
	
	vertices = dict([(vertex[i],Node(vertex[i])) for i in range(len(vertex))])

	for i in vertices:
		vertices[i].value = i

	for (u,v) in edges:
		vertices[u].adjacentNodes.append(vertices[v])

	#return the root node
	return vertices[vertex[0]]
