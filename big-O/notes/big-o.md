# Big-O notation
Is the language we use for talking about how long an algorithm takes to run.  

![Complexity chart](images/complexity-chart.png)

## O(n) -> Linear time
It's going to take as many operations as elements in the array.  
It takes linear time. Number of operations increases linearly.

## O(1) -> Constant time
The number of operations do not depend on the size of the input and are always constant.  



## Simplifying Big O (Rule Book)

### 1. Worst Case
Always think about the worst case when calculating Big O.

### 2. Remove constants
We have to remove the constants when doing the Big O calcutaion. We only care about what is on the chart.  
For example  
`O(1 + n/2 + 100) -> O(n)` -> Linear time.  
`O(2n) -> O(n)` -> Linear time.  
With Big O we don't really care about how steep the line is, we care about how the line moves as our input increases.

### 3. Different terms for inputs

### 4. Drop non dominants