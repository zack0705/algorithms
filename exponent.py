def exp_norm(a,n):
	x = 1
	for i in range(n):
		x = x*a
	return x

def exp_noice(a,n):
	if(n==1):
		return a
	if(n%2 == 0):
		return(exp_noice(a*a,n/2))
	else:
		return(a*exp_noice(a*a,(n-1)/2))
print(exp_noice(2,30))

