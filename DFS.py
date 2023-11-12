graph={
	1:[2,3],
	2:[1,4,5],
	3:[1,6],
	4:[2,5],
	5:[2,4,6],
	6:[3,5]
}
def dfs(node,visited):
	if node not in visited:
		print(node,end=" ")
		visited.append(node)
		for i in graph[node]:
			dfs(i,visited)
#if __name__ == '__main__':
dfs(1,[])