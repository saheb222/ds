def bin_search(a,n,min,max):
	if min>max:
		return False
	else:
		mid = (min+max)//2
		if a[mid] == n:
			return mid
		elif n>a[mid]:
			return bin_search(a,n,mid+1,max)
		else :
			return bin_search(a,n,min,mid-1)
a= [2,3,4,5,6,7,8,9,11,12,14]
n=int(input("please enter the element to be searched\n"))
result = bin_search(a,n,0,len(a)-1)
print(result)
