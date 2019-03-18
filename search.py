def search(a,n):
	for i in range(0,len(a)):
		if a[i] == n:
			return i
	return False

print("please enter the list seperated  by white space")
a = [int(x) for x in input().split()]
print("please enter the number to search from the list")
n = int(input())
result= search(a,n)
if result== False:
	print("not found")
else:
	print("found(first occurance) in position %d" %(result))

