# puzzles
Various puzzles/programming exercises. Demonstrate various techniques that have helped.

## Techniques
Below are the usual techniques. Note that "memonization" or "dynamic programming" are not techniques but
optimization that will convert the exponential problem to say polynomial time.

1. Clever Perspective

2. Recursion:
  The classic example is towns of hanoi. Rule:can't move a larger disk on top of a smaller disk 
   -- i.e., disks can only be moved to empty stacks or on top of larger disks. so smallest one on the top
  
[Solutions](https://www.youtube.com/watch?v=UuIneNBbscc&t=2518s)

Start with 1 disc from tower 1 to tower 3. ie only 1 move
Start with 2 disc from tower 1 to tower 3. ie only 3 moves
Start with 3 disc from tower 1 to tower 3. ie only 7 moves. 
   * Tower 1 to Tower 3
   * Tower 1 to Tower 2
   * Tower 3 to Tower 2

If you start with Tower 1 to Tower 2 then you can eventually move it to intermediate tower.
Size of the solution as 'n' number of discs. The pattern is 2^n -1 ie doubles in size.


### Clever Perspective
### breaking eggs
This puzzle is taken from [here](https://www.geeksforgeeks.org/puzzle-set-35-2-eggs-and-100-floors/)
The rules of the puzzle are

Suppose that we wish to know which stories in a n-story building are safe to drop eggs from, and which will cause the eggs to break on landing. What strategy should be used to drop eggs such that total number of drops in worst case is minimized and we find the required floor.
I am trying various strategies and trying to find the optimum result. 

Prof Srini represented the algorithm as a r-ary d-digit number. (where d is the number of balls). I plot his algo against tha naive binary search.
* Simulation
```
python3 sim1.py
```

* Simple linear search. Just to test out my tests.
```
py.test test_simple_serial_algo.py
```

* binary search. Divide into half each time.
```
py.test test_bin_search_algo.py


```

### Recursion
The general ideas for recursion is to express it in terms of intermediate problem.

1. Recurrence: 
Express the problem as a simple recurrence. For example Fib series, factorial. This will usually be in terms of 'n'
with some base cases.

2. Exhaustive Search: 
Explore the search space by walking through all the possibilities. Some common ways to search are
* Permutation without replacement: For example permute([a,b,c]) will give all 6 possibile arrangements. This is also
sometimes called exhaustive search.

* Subset: Find all possible subsets. For example subset([a,b,c]) will result in all the 8 combinations.
* printBinary: Accept the number of digits and print binary that have that many digits in ascendign order.

