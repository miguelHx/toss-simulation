"""
You toss n coins, each showing heads with probability p, independently of the other tosses.
Each coin that shows tails is tossed again (once more, or when t=2).  Let X be the total number of tails
What is the probability mass function of the total number of tails?  Start at main() function.
"""
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from utils.PageSlider import PageSlider
from utils.stats import simulated_binomial_pmf
from utils.stats import get_theoretical_probabilities, get_simulated_probabilities


def plot_coin_toss(n, p, t, simulations):
    start, end = 1, n
    x = range(start, end+1)

    width = 10
    height = 7
    fig, ax = plt.subplots(figsize=(width, height))
    fig.subplots_adjust(bottom=0.2)

    theoretical_binomial_pmf_equation = r"$P(X=k)=\binom{n}{k}((1-p)^t)^k(1-(1-p)^t)^{(n-k)}$"  # laTex
    plt.title("Binomial Dist. Simulation: {}".format(theoretical_binomial_pmf_equation))
    plt.xlabel("K tails")
    plt.ylabel("Probability")

    # plot theoretical y
    y_theoretical = get_theoretical_probabilities(start, end, n, p, t)
    [y_theoretical_line] = ax.plot(x, y_theoretical, 'b-', label='Theoretical', marker='o')
    # plot simulated y
    y_simulated = get_simulated_probabilities(start, end, n, p, t, simulations)
    [y_simulated_line] = ax.plot(x, y_simulated, 'r--', label='Simulated (Experimental)', marker='o')

    # custom legend items
    legend_item1 = mpatches.Patch(color='red', label="simulations = {}".format(simulations))
    legend_item2 = mpatches.Patch(color='black', label="t = {}".format(t))
    handles, labels = ax.get_legend_handles_labels()
    plt.legend(handles=[*handles, legend_item1, legend_item2])

    # description (under xlabel)
    txt = "'k' tails out of 'n' coins, with a max of 't' tosses (RE-toss on tails)"
    plt.figtext(0.5, 0.015, txt, wrap=True, horizontalalignment='center', fontsize=12)

    # setup sliders
    num_pages = 10
    tosses_slider_ax = fig.add_axes([0.1, 0.07, 0.8, 0.04])  # dimensions for slider
    toss_slider = PageSlider(tosses_slider_ax, 't', num_pages, activecolor="orange")

    # callback function
    def update(val):
        # set t label
        legend_item2.set_label("t = {}".format(int(val)+1))
        ax.legend(handles=[*handles, legend_item1, legend_item2])
        # compute new theoretical y
        new_theoretical_y = get_theoretical_probabilities(start, end, n, p, int(val)+1)
        y_theoretical_line.set_ydata(new_theoretical_y)
        # compute new simulated y
        new_simulated_y = get_simulated_probabilities(start, end, n, p, int(val)+1, simulations)
        y_simulated_line.set_ydata(new_simulated_y)
        # recompute the ax.dataLim
        ax.relim()
        # update ax.viewLim using the new dataLim
        ax.autoscale_view()
        fig.canvas.draw()
    toss_slider.on_changed(update)
    plt.show()


def simulate_coin_toss_tails(num_coins, k, p_tails, tosses, simulations):
    final_result = simulated_binomial_pmf(num_coins, k, p_tails, tosses, simulations)
    print("Result: {}".format(final_result))


def main():
    """
    This program will simulate the coin toss scenario above and compare simulated results to theoretical results.
    """
    t = 1
    n = 25
    # k = 4
    p_tails = 0.5
    # result = binomial_pmf(n, k, p_tails, t)
    # print("Theoretical probability with new formula: {}".format(result))

    num_simulations = 1000
    args = (n, p_tails, t, num_simulations)
    # print("Simulating coin toss with n={}, k={}, p_tails={}, t={}, and trials={}".format(*args))
    # simulate_coin_toss_tails(*args)
    plot_coin_toss(*args)


if __name__ == '__main__':
    main()
