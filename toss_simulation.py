"""
You toss n coins, each showing heads with probability p, independently of the other tosses.
Each coin that shows tails is tossed again (once more).  Let X be the total number of tails
What is the probability mass function of the total number of tails?  Start at main() function.
"""
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from helper_methods.stats import binomial_pmf, simulated_binomial_pmf


def get_simulated_probabilities(start, finish, n, p, t, simulations):
    """
    Runs simulations to get experimental probabilities for the coin toss problem for
    each integer between start and finish.
    By the law of big numbers, the more simulations we do, the closer we will get
    to the true theoretical probability
    :param start: integer
    :param finish: integer
    :param n: integer - number of coins/trials
    :param p: float - probability of outcome of interest
    :param t: integer - number of tosses (in case we get tails, up to t tosses)
    :param simulations - the number of times we want to simulate
    :return: list of simulated probabilities
    """
    output = []
    for i in range(start, finish+1):
        output.append(simulated_binomial_pmf(n, i, p, t, simulations))
    return output


def get_theoretical_probabilities(start, finish, n, p, t):
    """
    Compute the theoretical probabilities and return a list of them for each
    integer between start and finish
    :param start: integer
    :param finish: integer
    :param n: integer - number of coins/trials
    :param p: float - probability of outcome of interest
    :param t: integer - number of tosses (in case we get tails, up to t tosses)
    :return: list of theoretical probabilities
    """
    output = []
    for i in range(start, finish+1):
        output.append(binomial_pmf(n, i, p, t))
    return output


def plot_coin_toss(n, p, t, simulations):
    start, end = 1, 10
    x = range(start, end+1)

    plt.figure(figsize=(8, 8))  # window size

    # plot theoretical y
    y_theoretical = get_theoretical_probabilities(start, end, n, p, t)
    y_theoretical_line, = plt.plot(x, y_theoretical, 'b-', label='Theoretical', marker='o')

    # plot simulated y
    y_simulated = get_simulated_probabilities(start, end, n, p, t, simulations)
    y_simulated_line, = plt.plot(x, y_simulated, 'r--', label='Simulated (Experimental)', marker='o')

    # custom legend items
    legend_item1 = mpatches.Patch(color='red', label="simulations = {}".format(simulations))
    legend_item2 = mpatches.Patch(color='black', label="t = {}".format(t))
    plt.legend(handles=[y_theoretical_line, y_simulated_line, legend_item1, legend_item2])

    # description (under xlabel)
    txt = "'k' tails out of 'n' coins, with a max of 't' tosses (RE-toss on tails)"
    plt.figtext(0.5, 0.015, txt, wrap=True, horizontalalignment='center', fontsize=12)

    plt.title("Coin Toss Simulation")
    plt.xlabel("K tails")
    plt.ylabel("Probability")
    plt.show()


def simulate_coin_toss_tails(num_coins, k, p_tails, tosses, simulations):
    final_result = simulated_binomial_pmf(num_coins, k, p_tails, tosses, simulations)
    print("Result: {}".format(final_result))


def main():
    """
    This program will simulate the coin toss scenario above and compare simulated results to theoretical results.
    """
    t = 1
    n = 10
    k = 3
    p_tails = 0.5
    result = binomial_pmf(n, k, p_tails, t)
    print("Theoretical probability with new formula: {}".format(result))

    num_simulations = 1000
    args = (n, k, p_tails, t, num_simulations)
    print("Simulating coin toss with n={}, k={}, p_tails={}, t={}, and trials={}".format(*args))
    simulate_coin_toss_tails(*args)
    plot_coin_toss(n, p_tails, t, num_simulations)


if __name__ == '__main__':
    main()
