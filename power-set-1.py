def powerset(s):
	x = len(s)
	for i in range(1 << x):
		print(list([s[j] for j in range(x) if (i & (1 << j))]))

# powerset([4,5,6])

def list_powerset(lst):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in lst:
        result.extend([subset + [x] for subset in result])
    return result;
 
# print(list_powerset([4,5,6]))


def powerSet(a_list):
	result = [[]]
	if(len(a_list) == 0):
		return result

	for x in a_list:
		for i in range(len(result)):
			result.append(result[i] + [x])
	return result

#print(powerSet([1,2,3]))


def list_power_set(lst):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in lst:
    	for i in range(len(result)):
    		result.append(result[i] + [x])
    		print(result)
        #result.extend([subset + [x] for subset in result])
    return result;
 
#print(list_power_set([4,5,6]))


def rec_power_set(lst, index, res):
	if(index == len(lst) -1):
		res.append([lst[index]])
	else:
		rec_power_set(lst, index + 1, res)
		for i in range(len(res)):
			res.append([lst[index]] + res[i])

res = [[]]
rec_power_set([1,2,3,4,5], 0, res)
print(res);







