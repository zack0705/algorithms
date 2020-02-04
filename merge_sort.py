import random

def merge(a,p,q,r):
	n1 = q-p+1
	n2 = r-q
	l = []
	u = []
	for i in range(p,q+1):
		l.append(a[i])
	for i in range(q+1,r+1):
		u.append(a[i])
	l.append(9999)
	u.append(9999)
	i = 0
	j = 0
	for k in range(p,r+1):
		if(l[i]<=u[j] and l[i]!=9999):
			a[k]=l[i]
			i+=1
		elif(l[i]>u[j] and u[j]!=9999):
			a[k]=u[j]
			j+=1

def merge_sort(a,p,r):
	if(p!=r):
		merge_sort(a,p,int((p+r)/2))
		merge_sort(a,int((p+r)/2+1),r)
		merge(a,p,int((p+r)/2),r)

a = []
for i in range(100):
	a.append(random.randint(0,100))
merge_sort(a,0,len(a)-1)
print(a)

