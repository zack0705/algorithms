import random
count =0 

def partition(a,p,r):			#<------------from backward
	x = a[r]
	i = p-1
	global count
	for j in range(p,r):
		if(a[j]<=x):
			count+=1
			i+=1
			a[i],a[j] = a[j],a[i]
	a[i+1],a[r]=a[r],a[i+1]
	return(i+1)

def quick_sort(a,p,r):
	global count
	if(p<r):
		count+=1
		q = partition(a,p,r)
		quick_sort(a,p,q-1)
		quick_sort(a,q+1,r)


a = []
for i in range(100):
	a.append(random.randint(0, 100))

quick_sort(a,0,len(a)-1)

print([i for i in a])

print("Count = "+str(count))

