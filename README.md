# puzzles
Various puzzles/programming exercises

## Techniques
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
