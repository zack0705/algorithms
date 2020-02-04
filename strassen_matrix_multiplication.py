import numpy

def stra(a,b,c):
	if(len(a)!=len(b) and len(a)%2!=0):
		print("Not possible")
	if(len(a)==1):
		c[0] = int(a[0])*int(b[0])

	else:
		n = len(a)
		x = a[:n/2 , :n/2]
		y = a[:n/2 , n/2:]
		z = a[n/2: , :n/2]
		w = a[n/2: , n/2:]

		X = b[:n/2 , :n/2]
		Y = b[:n/2 , n/2:]
		Z = b[n/2: , :n/2]
		W = b[n/2: , n/2:]

		p1 = numpy.zeros((n/2,n/2), dtype=int)
		p2 = numpy.zeros((n/2,n/2), dtype=int)
		p3 = numpy.zeros((n/2,n/2), dtype=int)
		p4 = numpy.zeros((n/2,n/2), dtype=int)
		p5 = numpy.zeros((n/2,n/2), dtype=int)
		p6 = numpy.zeros((n/2,n/2), dtype=int)
		p7 = numpy.zeros((n/2,n/2), dtype=int)

		stra(numpy.add(x,w),numpy.add(X,W),p1)
		stra(numpy.add(z,w),X,p2)
		stra(x,numpy.subtract(Y,W),p3)
		stra(w,numpy.subtract(Z,X),p4)
		stra(numpy.add(x,y),W,p5)
		stra(numpy.subtract(z,x),numpy.add(X,Y),p6)
		stra(numpy.subtract(y,w),numpy.add(Z,W),p7)

		c[:n/2 , :n/2] = numpy.subtract(numpy.add(numpy.add(p1,p4),p7),p5)
		c[:n/2 , n/2:] = numpy.add(p3,p5)
		c[n/2: , :n/2] = numpy.add(p2,p4)
		c[n/2: , n/2:] = numpy.subtract(numpy.add(numpy.add(p1,p3),p6),p2)
		
a = numpy.array([[5,2,6,1],[0,6,2,0],[3,8,1,4],[1,8,5,6]])
b = numpy.array([[7,5,8,0],[1,8,2,6],[9,4,3,8],[5,3,7,9]])
c = numpy.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

stra(a,b,c)
print("ANS============")
print(c)

