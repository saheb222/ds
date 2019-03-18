def bin_search(a,n,min,max):
	if max-min+1<=0:
		return False
	else:
		mid = min+(max-min)//2
		if a[mid] == n:
			return mid
		elif n>a[mid]:
			return bin_search(a,n,mid+1,max)
		else :
			return bin_search(a,n,0,mid-1)
a= [2,3,4,5,6,7,8]
n=int(input("please enter the searcing element\n"))
result = bin_search(a,n,0,len(a))
print(result)