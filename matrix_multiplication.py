import math,sys

def matrix_mul(a,b):
	ar = len(a)
	ac = len(a[0])
	br = len(b)
	bc = len(b[0])
	c = []
	if(ac!=br):
		print("Not possible")
		sys.exit()
	for i in range(ar):
		c.append([])
		for j in range(bc):
			c[i].append(0)
			for k in range(ac):
				c[i][j]+=a[i][k]*b[k][j]
	return c

def matrix_mul_noice(a,b):
	ar = len(a)
	ac = len(a[0])
	br = len(b)
	bc = len(b[0])
	c = [[],[],[],[]]
	if(ac!=br or math.log(ar,2)%1 == 0.0 or ar == ac or br == ar or bc == ar):
		print("Not possible")
		sys.exit()
	if(ar==2):
		p1 = (a[0][0]+a[1][1])*(b[0][0]+b[1][1])
		p2 = (a[1][0]+a[1][1])*b[0][0]
		p3 = a[0][0]*(b[0][1]-b[1][1])
		p4 = a[1][1]*(b[1][0]-b[0][0])
		p5 = (a[0][0]+a[0][1])*b[1][1]
		p6 = (a[1][0]-a[0][0])*(b[0][0]+b[0][1])
		p7 = (a[0][1]-a[1][1])*(b[1][0]+b[1][1])

		c[0][0] = p1+p4-p5+p7
		c[0][1] = p3+p5
		c[1][0] = p2+p4
		c[1][1] = p1+p3-p2+p6
	else:
		

	return c

a = [[1,0,0],[0,1,0],[0,0,1]]
b = [[1,2,3],[4,5,6],[7,8,9]]
c = matrix_mul(a,b)
print(c)

