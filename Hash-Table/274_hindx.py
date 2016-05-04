def hIndex(self, citations):
	if citations == []:
		return 0
	citations.sort(reverse = True)
	end = len(citations) - 1
	start = 0
	while start < end - 1:
		mid = (start + end) / 2
		if citations[mid] < mid + 1:
			end = mid
		elif citations[mid] == mid + 1:
			return mid + 1
		else:
			start = mid
	if citations[end] >= end + 1:
		return end + 1
	elif citations[start] < start + 1:
		return 0
	else:
		return start + 1
		

			
