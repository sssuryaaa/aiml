graph={
	1:[2,3],
	2:[1,4,5],
	3:[1,6],
	4:[2,5],
	5:[2,4,6],
	6:[3,5]
}
visited=[]
def dfs(node,x):
	if x>0:
		if node not in visited:
			print(node,end=" ")
			visited.append(node)
		for i in graph[node]:
			dfs(i,x-1)
#if __name__ == '__main__':
for x in range(2,20,2):
	dfs(1,x)
	print()
