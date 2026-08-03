
numbers = [1,2,2,4,5,5,5,5,5,4]
target = 8


def two_sum(numbers, target):

    complement = 0
    complement_index = {}
    for i in range(len(numbers)):
        complement = target - numbers[i]


        if numbers[i] in complement_index:
            print(complement_index)
            return (i, complement_index.get(numbers[i]))
        
        complement_index[complement] = i

    

print(two_sum(numbers, target))


