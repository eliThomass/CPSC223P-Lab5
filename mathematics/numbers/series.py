def sum(list):
	sum = 0
	for val in list:
		sum += val
	return sum

def average(list):
	sum = 0
	num_items = 0
	for val in list:
		sum += val
		num_items += 1
	return sum / num_items
	
