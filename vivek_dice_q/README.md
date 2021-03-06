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

If I change the strategy to say 'min', then the result falls to $2. 

```python
python3 game.py --strategy=min
```

![Script output](https://github.com/sanjeevs/puzzles/blob/master/vivek_dice_q/max_rolls_3_min_strategy.png)

# Anamaya Strategey
Just doing for 3 rolls. It is pretty good. It comes up with $4.7

```python
python3 game.py --strategy=anamaya
```

1. If the first dice comes with a 5, 6 then stop else continue

2. if the second dice comes with a 4, 5, 6 then stop else continue

3. Take what you got.
![Script output](https://github.com/sanjeevs/puzzles/blob/master/vivek_dice_q/anamaya_3_rolls.png)

# Interesting
I ran the scripts with max rolls set to 2. The result is that you can play the game is the charge is less than $4.5.

```python
python3 game.py --max_rolls=2
```

![Script output](https://github.com/sanjeevs/puzzles/blob/master/vivek_dice_q/max_rolls_2.png)

# Sanity check
I ran the scripts with max rolls set to 1. The result is that you can play the game is the charge is less than $3.5.

```python
python3 game.py --max_rolls=1
```

![Script output](https://github.com/sanjeevs/puzzles/blob/master/vivek_dice_q/max_rolls_1.png)
