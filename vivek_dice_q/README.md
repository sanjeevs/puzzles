# Question
Suppose you were paid as many dollars, as that appeared on max of 3 dice rolls. How many dollars will be you be willing to pay to play this game?

# Rules
1. You can roll upto 3 times for a single trial?
2. You can choose to stop at any time.

#Answer 1


Assuming that you had perfect vision of the future, the python code below shows that the average return is $5.

```python
python3 game.py
```

Attached is the output of the script.
![Script output](https://github.com/sanjeevs/puzzles/blob/master/vivek_dice_q/max_rolls_3.png)

So you should *NEVER* play if the charge is more than that. Since you don't have perfect vision, your strategy can never be better than this and so your actual return will be less than this value.


The interesting question is what should be the optimum strategy so that you can achieve this best result.

# Interesting
I ran the scripts with max rolls set to 2. The result is that you can play the game is the charge is less than $4.5.

```python
python3 game.py --max_rolls=2
```

![Script output](https://github.com/sanjeevs/puzzles/blob/master/vivek_dice_q/max_rolls_2.png)
