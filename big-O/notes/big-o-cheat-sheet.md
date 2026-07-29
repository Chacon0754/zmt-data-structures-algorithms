# Cheat sheet
## Big Os
- **O(1) *Constant:*** No Loops.    
- **O(log(n)) *Logarithmic:*** Usually searching algorithms have log(n) if they are sorted (Binary search) (not on hash maps though).  
- **O(n) *Linear:*** for or while loops.  
- **O(n\*log(n)) *Log linear:*** Sorting operations usually.  
- **O(n^2) *Quadratic:*** Every element in a collection needs to be compared to every other element. Two nested loops.  
- **O(2^N) *Exponential:*** Recursive algorithms that solve a problem of size N.  
- **O(n!) *Factorial:*** You are adding a loops for every element.  

>**Important:** 
- Iterating through half a collection is still O(n).
- Two separate collections:cO(a + b).

## What can cause time in a function
- **Operations** (+, -, *, /-).
- **Comparisons** (<, >, ==).
- **Looping** (for, while).
- **Outside function call** (function()).

## Rule book
1. Always worst case.
2. Remove constants.
3. Different inputs should have different variables. `O(a+b)`. a and b arrays nested would be `O(a*b)`.
    - for steps in order.
    - for nested steps.
4. Drop non dominant terms.

## What causes space complexity
- Variables.
- Data structures.
- Function call. 
- Allocations.
