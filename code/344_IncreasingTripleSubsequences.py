# !/user/bin/env python
# -*- coding: utf-8 -*-
def increasingTriplet(nums):
	len = nums.__len__()
	if len < 3:
		return False
	second_min = -1
	minnum = nums[0]
	
	for i in range(1, len):
		if nums[i] <= minnum:
			minnum = nums[i]
		elif second_min == -1 or second_min >= nums[i]:
			second_min = nums[i]
		else:
			return True
	return False
