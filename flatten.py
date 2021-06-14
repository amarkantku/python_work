from collections.abc import Iterable

def single_list(list,ignore_types=(str)): 
	for item in list:
	    if isinstance(item, Iterable) and not isinstance(item, ignore_types):
	        yield from single_list(item,ignore_types=(str))
	    else:
	        yield item

Item_list = [
	10,20,
	[30,40],
	[50,None,'hello',70],
	100
]
items_single=single_list(Item_list)
#print(list(items_single))

for item in items_single:
    print(item)