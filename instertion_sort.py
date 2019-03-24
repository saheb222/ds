def selecttion_sort(a):
	for i in range(len(a)):
		point = i
		for j in range(i-1,-1,-1):
			if a[point]<a[j]:
				(a[point],a[j]) = (a[j],a[point])
				point = j
	return a
print (selecttion_sort([200,100,23,14,1,6,7,18,9,0,-5,-8,-100]))
