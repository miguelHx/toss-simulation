"""
You toss n coins, each showing heads with probability p, independently of the other tosses.
Each coin that shows tails is tossed again (once more).  Let X be the total number of tails
What is the probability mass function of the total number of tails?  Start at main() function.
"""
import random
import matplotlib.pyplot as plt
from helper_methods.stats import binomial_pmf


def get_theoretical_probabilities(start, finish, n, p, t):
    """
    Compute the theoretical probabilities and return a list of them for each
    integer between start and finish with n coins, p probability, and t tosses
    :param start: integer
    :param finish: integer
    :param n: integer
    :param p: float
    :param t: integer
    :return: list of theoretical probabilities
    """
    output = []
    for i in range(start, finish+1):
        output.append(binomial_pmf(n, i, p, t))
    return output


def plot_coin_toss(n, k, p, t):
    start, end = 1, 10
    x = range(start, end+1)

    y_theoretical = get_theoretical_probabilities(start, end, n, p, t)
    y_theoretical_line, = plt.plot(x, y_theoretical, 'b--', label='Theoretical')

    plt.legend(handles=[y_theoretical_line])

    plt.title("Probability distribution for getting k tails out of n coin tosses")
    plt.xlabel("Number of Tails in Simulation")
    plt.ylabel("Probability")
    plt.show()


def simulate_coin_toss_tails(simulations, num_coins, k, tosses, p_tails):
    # p_heads = 1-p_tails
    desired_result_count = 0
    for i in range(simulations):
        tails_count = 0
        heads_count = 0
        # flip coin 'num_coins' times
        for j in range(num_coins):
            # toss 'tosses' number of times (only RE-toss on tails)
            for t in range(tosses):
                coin = random.random()
                if p_tails < coin:
                    # if tails, keep tossing, unless at last toss
                    if t == tosses-1:
                        tails_count += 1
                else:
                    # if heads, stop tossing, move to next coin toss
                    heads_count += 1
                    break
        if tails_count == k:
            desired_result_count += 1
    final_result = desired_result_count / simulations
    print("Result: {}".format(final_result))


def main():
    """
    This program will simulate the coin toss scenario above and will compare simulated results to theoretical results.
    """
    t = 2
    n = 10
    k = 3
    p_tails = 0.5
    result = binomial_pmf(n, k, p_tails, t)
    print("Theoretical probability with new formula: {}".format(result))

    num_simulations = 10000
    args = (n, k, t, p_tails, num_simulations)
    print("Simulating coin toss with n={}, k={}, t={}, p_tails={}, and trials={}".format(*args))
    simulate_coin_toss_tails(num_simulations, n, k, t, p_tails)
    plot_coin_toss(n, k, p_tails, t)


if __name__ == '__main__':
    main()
