class Solution(object):
	def topKFrequent(self, nums, k):
		time_dict = {}
		answer = k*[0]
		for i in nums:
			if i not in time_dict:
				time_dict[i] = 0
			time_dict[i] += 1
		sorted_dict = sorted(time_dict.items(), key=lambda time_dict:time_dictp[1], reverse=True) 
		return sorted_dict[:k]
