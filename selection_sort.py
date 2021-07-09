"""
Author : Gülşah Büyük
Date : 19.04.2021
"""

def selectionSort(data_list ):
    size = len(data_list)
    for i in range(size - 1):
        # set the first element as a minimum in the data
        min_index = i
        # select the minimum element in each loop
        for j in range(i+1,size):
            # Compare minimum element with the (i+1)th element.
            # If the (i+1)th element is smaller than the minimum,
            # assign the (i+1)th element as a minimum.
            if data_list[j] < data_list[min_index] :
                min_index = j
        # After each iteration the minimum is placed in the front of the unsorted list.
        if min_index != i :
            temp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = temp
    # Repeat the process (lenght-1) times as expected.
    # Last element in the list automatically sorted.
    return data_list


data = [-12,334,87,19,5,78,544]
sortedlist = selectionSort(data)
print(sortedlist)