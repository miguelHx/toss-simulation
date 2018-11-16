"""
You toss n coins, each showing heads with probability p, independently of the other tosses.
Each coin that shows tails is tossed again (once more).  Let X be the total number of tails
What is the probability mass function of the total number of tails?  Start at main() function.
"""
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from helper_methods.stats import simulated_binomial_pmf
from helper_methods.stats import get_theoretical_probabilities, get_simulated_probabilities


def plot_coin_toss(n, k, p, t, simulations):
    start, end = 1, k
    x = range(start, end+1)

    width = 10
    height = 7
    plt.figure(figsize=(width, height))  # window size

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

    theoretical_binomial_pmf_equation = r"$P(X=k)=\binom{n}{k}((1-p)^t)^k(1-(1-p)^t)^{(n-k)}$"  # laTex
    plt.title("Binomial Dist. Simulation: {}".format(theoretical_binomial_pmf_equation))
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
    t = 2
    n = 25
    k = 25
    p_tails = 0.5
    # result = binomial_pmf(n, k, p_tails, t)
    # print("Theoretical probability with new formula: {}".format(result))
    #
    num_simulations = 500
    args = (n, k, p_tails, t, num_simulations)
    # print("Simulating coin toss with n={}, k={}, p_tails={}, t={}, and trials={}".format(*args))
    # simulate_coin_toss_tails(*args)
    plot_coin_toss(*args)


if __name__ == '__main__':
    main()
