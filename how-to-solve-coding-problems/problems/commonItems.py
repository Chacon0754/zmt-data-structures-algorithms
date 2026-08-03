"""
    Given 2 arrays, create a function that let's a user know (true/false)
    wether these two arrays contain any common items.
    For example:
    array1 = ["a", "b", "c", "x"]
    array2 = ["z", "y", "i"]
    should return False

    array1 = ["a", "b", "c", "x"]
    array2 = ["z", "y", "x"]
    should return True
"""

def common_item(arr1, arr2):
    items_arr2 = set(arr2)
    for letter in arr1:
        if letter in items_arr2:
            return True
    return False



array1 = ["a", "b", "c", "x"]
array2 = ["z", "y", "i"]
array3 = ["z", "y", "x"]

print(common_item(array1, array2))
print(common_item(array1, array3))
