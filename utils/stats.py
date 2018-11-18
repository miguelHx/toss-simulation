"""
Helper functions.
"""
import random


def factorial(k):
    """
    Computes the factorial value of a number k.
    :param k: an integer
    :return: the factorial of k
    """
    if k == 0:
        return 1
    # k * k - 1 * k - 2 * ... * 1
    output = 1  # start at 1
    for _k in range(1, k+1):
        output *= _k
    return output


def n_choose_k(n, k):
    """
    Computes the number of 'k' combinations of a set of 'n' elements
    :param n: the size of the set
    :param k: number of items that we choose from the set
    :return: the value of the binomial coefficient.
    """
    return factorial(n) / (factorial(k) * factorial(n-k))


def binomial_pmf(n, k, p, t):
    """
    Computes the probability of getting 'k' of some random event with probability 'p'
    out of 'n' trials assuming that the outcome of each trial is independent.  Also, the catch to this one is that
    if we get tails, we must toss 't' times
    :param n: the number of trials
    :param k: number of successes
    :param p: the probability of an individual desired outcome
    :param t: the number of tosses to make when getting tails
    :return: the theoretical probability of getting k successes out of n trials
    """
    return n_choose_k(n, k) * (p**t)**k * (1-(p**t))**(n-k)


def simulated_binomial_pmf(n, k, p, t, simulations):
    """
    Same as binomial_pmf, except now we are running the actual simulation.
    :param n: the number of trials (in our case, coins to toss)
    :param k: number of successes out of n trials
    :param p: the probability of an individual desired outcome
    :param t: the number of tosses to make when getting tails
    :param simulations: the number of simulations to run.
        the bigger the value for simulations, the more accurate the result
    :return: Out of all simulations,
        the probability of getting k successes out of n trials
    """
    desired_result_count = 0
    for s in range(simulations):
        tails_count = 0
        heads_count = 0
        # flip coin 'n' times
        for _n in range(n):
            # toss 't' number of times (only RE-toss on tails)
            for _t in range(t):
                coin = random.random()
                if coin < p:
                    # if tails, keep tossing, unless we are at last toss
                    if _t == t-1:
                        tails_count += 1
                else:
                    # heads, stop RE-tossing, move to next coin toss
                    heads_count += 1
                    break
        # if this simulation gave a desired outcome ('k' tails), then inc counter
        if tails_count == k:
            desired_result_count += 1
    # Probability = # of desired outcomes / # of total outcomes
    return desired_result_count / simulations


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
