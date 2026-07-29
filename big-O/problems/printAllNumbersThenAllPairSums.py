
def print_all_numbers_then_all_pair_sum(numbers):

    print("These are the numbers:")
    for number in numbers:  # o(n)
        print(number)

    print("\nThese are their sums:")
    for i in range(len(numbers)):   # O(n)
        for j in range(len(numbers)): # O(n) -> O(n^2)
            print(numbers[i] + numbers[j])

    # O(n + n^2) -Drop non dominants> O(n^2)
numbers = [1,2,3,4,5]
print_all_numbers_then_all_pair_sum(numbers)

"""
Another example, we have another function with the notation
O(x^2 + 3x + 100 +x/2). And the rule says that we only care about the 
most important dominant term and because x^2 is the most significant
term (in terms of scale) we drop everything else ans we only
keep the O(n^2)
"""