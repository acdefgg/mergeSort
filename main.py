def Sort(A, p, r):
	if p < r:
		q = (p + r) // 2 
		Sort(A, p, q)
		Sort(A, q + 1, r)
		Merge(A, p, q, r)


def Merge(A, p, q, r):
	tempArrLeft = A[p:q] # Создание временных массивов для хранения отсортированных подмассивов
	tempArrRight = A[q:r + 1]
	i = 0 # создания переменных для временных подмассивов
	j = 0
	
	while i < len(tempArrLeft) and j < len(tempArrRight): # пока в каждом из временных масивов есть числа, основной массив будет изменяться
		if tempArrLeft[i] < tempArrRight[j]:
			A[p + i + j] = tempArrLeft[i]
			i += 1
		else:
			A[p + i + j] = tempArrRight[j]
			j += 1
	# После того, как в одном из временных массивов закаончатся числа, второй массив дозаполнит оставшееся место в постоянном массиве
	while i < len(tempArrLeft):
		A[p + i + j] = tempArrLeft[i]
		i += 1
	while j < len(tempArrRight):
		A[p + i + j] = tempArrRight[j]
		j += 1


A = [5, 2, 4, 6, 1, 3, 2, 6]

Sort(A, 0, len(A))
print('res: ', A)
