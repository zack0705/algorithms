import numpy
def lcs(a,b):
	n = len(a)
	m = len(b)
	M = numpy.zeros((n+1,m+1))
	for i in range(1,n+1):
		for j in range(1,m+1):
			if(a[i-1]==b[j-1]):
				M[i][j] = 1 + ((M[i-1][j-1])*10%10)/10 + 0.1
			elif(M[i-1][j]*10%10 > M[i][j-1]*10%10):
				M[i][j] = 2 + (M[i-1][j]*10%10)/10
			else:
				M[i][j] = 0 + (M[i][j-1]*10%10)/10
	return M

def trace(a,A,B):
	n = len(a)-1
	m = len(a[0])-1
	x = ""	
	while (a[n][m]!=0.):
		if(int(a[n][m])==1):
			x = str(A[n-1])+x
			n -= 1
			m -= 1
		elif(int(a[n][m])==2):
			n -= 1
		elif(int(a[n][m])==0):
			m -= 1
	return x

a = "ababc"
b = "bcabd"

c = lcs(a,b)
print(c)
print(trace(c,a,b))

