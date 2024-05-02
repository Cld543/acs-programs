'''
Function to split a large list of items into multiple evenly sized lists.
If the number cannot be evenly split into equal length lists, then the remainder
will be added into a list that contains all remaining items that are left over

@param items: The list of items the user wishes to split up
@param num_per_list: The number of items per list 
'''
# coding: utf-8
def split_list(items, num_per_list):
    lists = []
    n = len(items)
    num_lists = n // num_per_list + 1
    for _ in range(num_lists):
        lists.append([])
    for i in range(n):
        lists[i // num_per_list].append(items[i])
    if len(lists[-1]) == 0:
        lists.pop()
    return lists
    
