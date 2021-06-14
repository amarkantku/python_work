from itertools import combinations

def print_powerset(string):
	for i in range(0,len(string)+1):
		for element in combinations(string,i):
			print(list(element))

string=['a','b','c'] 
print_powerset(string)


  
def printPowerSet(array,set_size): 
      
    # set_size of power set of a set 
    # with set_size n is (2**n -1) 
    pow_set_size = (int) (2 ** set_size); 
    counter = 0; 
    j = 0;
    print(set_size, pow_set_size);
 
    # Run from counter 000..0 to 111..1 
    for counter in range(0, pow_set_size): 
        for j in range(0, set_size): 
              
            # Check if jth bit in the  
            # counter is set If set then  
            # print jth element from set  
            if((counter & (1 << j)) > 0): 
                print(array[j], end = "");
                print('-->', j)

        print(""); 
  
# Driver program to test printPowerSet 
array = ['a', 'b', 'c']; 
printPowerSet(array, 3);
print('----')

for i in range(0,8):
	print("i ->", i)
	for j in range(0,3):
		print("\tj ->", j , end="")
		print("\t",i & (1<<j), end="")
	print("")

