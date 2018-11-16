"""
You toss n coins, each showing heads with probability p, independently of the other tosses.
Each coin that shows tails is tossed again (once more).  Let X be the total number of tails
What is the probability mass function of the total number of tails?  Start at main() function.
"""
import random
from helper_methods.stats import binomial_pmf


def plot_coin_toss():
    print("plotting...")


def simulate_coin_toss_tails(trials, num_coins, k, tosses, p_tails):
    p_heads = 1-p_tails
    desired_result_count = 0
    for i in range(trials):
        tails_count = 0
        heads_count = 0
        # flip coin 'num_coins' times
        for j in range(num_coins):
            # toss 'tosses' number of times (only RE-toss on tails)
            for t in range(tosses):
                coin = random.random()
                if p_tails < coin:
                    # if tails, keep tossing
                    if t == tosses-1:
                        tails_count += 1
                else:
                    # if heads, stop tossing
                    heads_count += 1
                    break
        if tails_count == k:
            desired_result_count += 1
    final_result = desired_result_count / trials
    print("Result: {}".format(final_result))


def main():
    """
    This program will simulate the coin toss scenario above and will compare simulated results to theoretical results.
    """
    t = 3
    n = 10
    k = 3
    p_tails = 0.5
    result = binomial_pmf(n, k, p_tails, t)
    print("Theoretical probability with new formula: {}".format(result))

    num_trials = 10000
    args = (n, k, t, p_tails, num_trials)
    print("Simulating coin toss with n={}, k={}, t={}, p_tails={}, and trials={}".format(*args))
    simulate_coin_toss_tails(num_trials, n, k, t, p_tails)

    plot_coin_toss()


if __name__ == '__main__':
    main()
