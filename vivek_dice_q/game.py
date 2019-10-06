"""Compute the average money made by rolling the dice."""
import random
import sys
import argparse
import my_plot 

def main(argv):
    """Run the experiments 'm' times consisting of 'n' trials."""
    opt = parse_cmd_line(argv)
    results = []

    msg = "Running exp {0} times with {1} trials and max {2} dice rolls".format(
            opt.num_experiments, opt.num_trials, opt.max_rolls)
    print(msg)
    for i in range(opt.num_experiments):
        # Repeat the experiment with max_rolls 'num_trials' times.
        results.append(experiment(opt.num_trials, opt.max_rolls))

    my_plot.draw_bar(msg, results)


    
def experiment(num_trials, max_rolls):
    """Return the average return of running the trial num_times."""
    total_profit = 0
    for i in range(num_trials):
        total_profit +=  trial_best_of_n_rolls(max_rolls)

    average_return = round(total_profit/num_trials, 1)
    return average_return

def trial_best_of_n_rolls(max_rolls):
    """Returns the best case profit in upto n rolls of dice.
       max_rolls: Allow upto these many rolls of the dice.
       Return a tuple with the number of actual rolls and max profit.
    """
    winnings = []
    for i in range(max_rolls):
        winnings.append(random.randint(1,6))
    max_profit = max(winnings)
    return max_profit

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

    return parser.parse_args(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
