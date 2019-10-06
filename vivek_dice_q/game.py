"""Compute the average money made by rolling the dice."""
import random
import sys
import argparse
import my_plot 

def main(argv):
    """Run the experiments 'm' times consisting of 'n' trials."""
    opt = parse_cmd_line(argv)
    results = []

    dispatcher = {'max': max, 'min': min, 
            'anamaya': anamaya,
            'rand': lambda lst: random.randint(0, len(lst) -1)}
    strategy = dispatcher[opt.strategy] 

    msg = "Running exp {0} times with {1} trials and max {2} dice rolls and {3} strategy".format(
            opt.num_experiments, opt.num_trials, opt.max_rolls, opt.strategy)
    print(msg)

    for i in range(opt.num_experiments):
        # Repeat the experiment with max_rolls 'num_trials' times.
        results.append(experiment(opt.num_trials, opt.max_rolls, strategy))

    my_plot.draw_bar(msg, results)


    
def experiment(num_trials, max_rolls, strategy):
    """Return the average return of running the trial num_times."""
    total_profit = 0
    for i in range(num_trials):
        total_profit +=  trial_best_of_n_rolls(max_rolls, strategy)

    average_return = round(total_profit/num_trials, 1)
    return average_return

def trial_best_of_n_rolls(max_rolls, strategy):
    """Returns the best case profit in upto n rolls of dice.
       max_rolls: Allow upto these many rolls of the dice.
       Return a tuple with the number of actual rolls and max profit.
    """
    winnings = []
    for i in range(max_rolls):
        winnings.append(random.randint(1,6))
    max_profit = strategy(winnings)
    return max_profit

def anamaya(lst):
    """Keep playing if the value is more than the expected value of n-1."""
    if lst[0] > 4:
        return lst[0]
    elif lst[1] > 3:
        return lst[1]
    else:
        return lst[2]

def parse_cmd_line(argv):
    """Parse the command line options."""
    parser = argparse.ArgumentParser(
                    description="Run the roll dice experiment to figure out the average return." )
    parser.add_argument('--num_trials', action="store", dest="num_trials", type=int,
                        default=1000, help="Repeat so many times for each trial.")
    parser.add_argument('--max_rolls', action="store", dest="max_rolls", type=int,
                        default=3, help="Allow max rolls of dice per trial.")
    parser.add_argument('--num_experiments', action="store", dest="num_experiments", type=int,
                        default=10000, help="Repeat experiment so many times.")
    parser.add_argument('--strategy', action="store", dest="strategy", type=str,
                        default="max", help="Strategy to use in a trial.")

    return parser.parse_args(argv)


if __name__ == "__main__":
    main(sys.argv[1:])
