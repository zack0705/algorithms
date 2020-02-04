def bin_rec_search(a,high,low,s):
	mid = int((high+low)/2)
	if(low>high):
		return(-1)
	if(a[mid] == s):
		return mid
	elif(a[mid] > s):
		return (bin_rec_search(a, mid-1, low, s))
	else:
		return (bin_rec_search(a, high, mid+1, s))

def bin_itt_search(a,high,low,s):
	while(low<=high):
		mid = int((high+low)/2)
		if(a[mid]==s):
			return mid
		elif(a[mid]>s):
			high=mid-1
		else:
			low=mid+1
	return(-1)

a = [0,1,2,3,4,5,6,7,8]
b = int(input("Enter no. to find"))
print("REC = "+str(bin_rec_search(a,len(a)-1,0,b)))
print("ITT = "+str(bin_itt_search(a,len(a)-1,0,b)))

