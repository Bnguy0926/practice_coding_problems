from array import array
from hashlib import new
import itertools


def findWithSum(arr, val, n=2):
    list_of_combos = []
    target_combo = []
    
    for i in range(n): #get an array of all the possible combinations with the length of n
        list_of_combos += [list(j) for j in itertools.combinations(arr, n)]

    for i in range(len(list_of_combos)): #add up each of the possible combinations
        total = list(itertools.accumulate(list_of_combos[i]))[-1]
        if total == val: #if the sum of the combo = val, we save it as a variable
            target_combo = list_of_combos[i]
    
    new_dic = {} #create the new dictionary that will be outputted

    j = 0
    for i in range(len(target_combo)):
        while arr[j] != target_combo[i]:
            j += 1
        arr[j] == target_combo[i]
        new_dic[j] = arr[j]
        j += 1        
        
    return new_dic




# test cases
arr = []
val = 0
print(findWithSum(arr, val))

arr = [1, 2, 3]
val = 2
print(findWithSum(arr, val, 1))

arr = [1, 1, 1]
val = 3
print(findWithSum(arr, val, 3))

arr = [3, 2, 5]
val = 5
print(findWithSum(arr, val, 1))