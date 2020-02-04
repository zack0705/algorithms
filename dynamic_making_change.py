def min(a,b):
	if(a<=b):
		return a
	return b

def change(money,change):
	a = []
	for i in range(len(money)):
		for j in range(change+1):
			if(j==0):
				a.append([0])
			elif(i==0 and j<money[0]):
				a[i].append(9999)
			elif(i==0):
				a[i].append(1+a[i][j-money[0]])
			elif(j<money[i]):
				a[i].append(a[i-1][j])
			else:
				a[i].append(min(a[i-1][j], a[i][j-money[i]]+1))
	return a	
	return a[len(money)-1][change]

a = change([1,4,6],8)
for i in a:
	print i


