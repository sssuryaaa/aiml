graph={
	1:[2,3],
	2:[1,4,5],
	3:[1,6],
	4:[2,5],
	5:[2,4,6],
	6:[3,5]
}
def bfs(node):
	visited=[]
	queue=[]
	queue.append(node)
	visited.append(node)
	while queue:
		a=queue.pop(0)
		print(a,end=" ")
		for i in graph[a]:
			if i not in visited:
				queue.append(i)
				visited.append(i)
if __name__ == '__main__':
	bfs(1)
