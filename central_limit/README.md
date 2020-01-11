## Central Limit Theorem
Suppose we roll the dice. The probability of getting a 1 to 6 is a constant 1/6. Hence the pdf is a straight line.

Now say we do an experiment that does n (say 1000) trials and compute the average score.

Repeat this experiment say m times and plot the average score of the experiment.

As per the central limit theorem the PDF of the average score should be a bell curve.

## Running
```
python3 central_limit.py 1000000 100
```

![result](https://github.com/sanjeevs/puzzles/blob/master/central_limit/out_million_trial_100.png)
