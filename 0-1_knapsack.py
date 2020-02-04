def max(a,b):
	if(a>=b):
		return a
	return b

def knap(item,weight):
	a = []
	for i in range(len(item)+1):
		for j in range(weight+1):
			if(j==0):
				a.append([0])
			elif(i==0):
				a[i].append(0)
			elif(item[i-1][0]<=j):
				a[i].append(max(item[i-1][1]+a[i-1][j-item[i-1][0]],a[i-1][j]))
			else:
				a[i].append(a[i-1][j])
	return a
a = knap([[2,3],[3,4],[4,5],[5,6]],5)
for i in a:
	print(i)

