
def findMinRec(arr, i, sumCalculated,sumTotal):
	if i == 0:
		if sumCalculated == sumTotal:
			print(sumCalculated)
			return 11000000000000
		if sumCalculated==0:
			return 11000000000000
		return abs((sumTotal - sumCalculated) - sumCalculated)
	return min(findMinRec(arr, i-1 , sumCalculated+arr[i-1],sumTotal),findMinRec(arr, i - 1, sumCalculated, sumTotal))



def findMin(arr, n):
	sumTotal = 0
	for i in range(n):
		sumTotal += arr[i]
	print(sumTotal)
	return findMinRec(arr, n, 0, sumTotal)


nums = [76,8,45,20,74,84,28,1]
n = len(nums)
nums.sort(reverse=True)
print(findMin(nums, n))