import heapq
import copy
row=[1,0,-1,0]
col=[0,-1,0,1]
visited=[]
class node:
	def __init__(self,mat,cost,level,blank_pos):
		self.mat=mat
		self.cost=cost
		self.level=level
		self.blank_pos=blank_pos
	def __lt__(self,i):
		return self.cost<i.cost
def calculatecost(cur,final):
	count=0
	for i in range(3):
		for j in range(3):
			if(cur[i][j] and cur[i][j]!=final[i][j]):
				count+=1
	return count
def output(mat):
	for i in range(3):
		for j in range(3):
			print(mat[i][j],end=" ")
		print()
	print()
def newNode(mat,final,new_pos,old_pos,level):
	new_mat=copy.deepcopy(mat)
	new_mat[new_pos[0]][new_pos[1]],new_mat[old_pos[0]][old_pos[1]]=new_mat[old_pos[0]][old_pos[1]],new_mat[new_pos[0]][new_pos[1]]
	cost=calculatecost(new_mat,final)
	child=node(new_mat,cost,level,new_pos)
	return child
def solve(initial,final,blank_pos):
	heap=[]
	cost=calculatecost(initial,final)
	#output(initial)
	if(cost==0):
		output(initial)
		return
	temp=node(initial,cost,0,blank_pos)
	#output(temp.mat)
	heapq.heappush(heap,temp)
	visited.append(temp.mat)
	while heap:
		cur=heapq.heappop(heap)
		output(cur.mat)
		for i in range(4):
			a=cur.blank_pos[0]+row[i]
			b=cur.blank_pos[1]+col[i]
			if(a>-1 and a<3 and b>-1 and b<3):
				child=newNode(cur.mat,final,[a,b],cur.blank_pos,cur.level+1)
				#output(child.mat)
				if(child.cost==0):
					output(child.mat)
					return
				if child.mat not in visited:
					#output(child.mat)
					heapq.heappush(heap,child)
					visited.append(child.mat)
#initial=[[3,1],[2,0]]
#final=[[1,2],[3,0]]
#blank_pos=[1,1]

initial=[[8,7,6],[5,4,3],[2,1,0]]
final=[[1,2,3],[4,5,6],[7,8,0]]
blank_pos=[2,2]
solve(initial,final,blank_pos)