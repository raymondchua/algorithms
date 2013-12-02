#pseudocode for BFS
#source: MIT 6.006, Introduction to Algorithms Fall 2011
BFS(S,  Adj):
	level = { s : Ø }
	parent = {s : None}
	i = 1

	#level i - 1
	frontier = [s]

	#end when frontier is an empty list
	while frontier:

		#level i
		next  = []
		for u in frontier:
			for v in Adj[v]:
				if v not in level:
					level[v] = i
					parent[v] = u
					next.append[v]
		frontier = next
		i+ = 1