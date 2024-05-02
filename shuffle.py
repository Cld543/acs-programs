'''
This function shuffles the values stored within the given
array parameter
'''

# coding: utf-8
def shuffle(array):
    n = len(array)
    for i in range(n - 2):
        j = random.randint(i,n-1)
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
    return array
            
