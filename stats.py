def mean(vals):
	"""Calculate the arithmetic mean of a list of numbers in vals"""
	assert type(vals) is list, 'wrong imput format'
	new_list=[]
	for x in vals:
		new_list.append(float(x))
		
	total = sum(new_list)
	length = len(new_list)
	if length == 0:
		return 0
	else:
		return total/length
	
#print(mean("hello"))
