def selection_sort(a):
	for i in range(len(a)):
		min_pos = i
		for j in range(i+1,len(a)):
			if a[j]<a[min_pos]:
				min_pos = j
		(a[min_pos],a[i]) = (a[i],a[min_pos])
	return a


print(selection_sort([3,4,2,1,8,77,5,-1,-5,100]))