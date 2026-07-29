
def boooo(n):
    for i in range(len(n)):
        print('boooooo')

    """
     This function has a space complexity of
     O(1) because we are not adding extra space
    """

boooo([1,1,1,1,1])

def array_of_n_hi_n_times(n):
    hi_array= ["H"] * n
    
    return hi_array

    """
    The space complexity of this function is O(n)
    because each iteam is an additional memory space on 
    our computers
    """

print(array_of_n_hi_n_times(100000000))