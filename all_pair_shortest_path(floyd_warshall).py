def floyd_warshall(a,m,v):	
	for k in range(len(a)):
		for i in range(len(a)):
			for j in range(len(a)):
				if(a[i][j]>(a[i][k]+a[k][j])):
					a[i][j] = a[i][k]+a[k][j]
					m[i][j] = v[k]

vertex = "abcd"
a = [[0,8,9999,1],[9999,0,1,9999],[4,9999,0,9999],[9999,2,9,0]]
m = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

floyd_warshall(a,m,vertex)

print(a)
print(m)

