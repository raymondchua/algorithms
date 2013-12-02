#Breadth-first search, Python
from collections import deque
from graph import constructGraph

#breadth-first search
#param: root node of a graph, vertex it is searching for
#return True if found, else False
def bfsearch(root, vertex):
	queue = deque([root])
	visitedNodes = set()

	#keep looking while queue is not empty
	while len(queue) > 0:
		node = queue.pop()
		
		#if node is visited, go to the next node in graph
		if node in visitedNodes:

			continue

		#else add node to visitedNodes list and check if it is found
		else:
			
			visitedNodes.add(node)
			if node.value == vertex:
				
				printShortestPath(node)
				return True

			for x in node.adjacentNodes:
				if x not in visitedNodes:
					queue.append(x)
					x.parent = node
				


	return False

#print the route from the resulting node to the root node
def printShortestPath(lastNode):

	if lastNode.parent != -1:
		print lastNode.value, "->",
		printShortestPath(lastNode.parent)

	else:

		print lastNode.value



if __name__ == "__main__":
   vertices = ["s", "x", "a", "z", "c", "d","f","v"]
   edges = [("s","x"), ("s","a"), ("a","z"), ("x","d"), ("x","c"), ("d","f"),("c","v"),("f","v")]

   G = constructGraph(vertices, edges)

   #test for node that cannot be found
   print bfsearch(G, "e")

   #test for node that can be found
   print bfsearch(G, "v")
