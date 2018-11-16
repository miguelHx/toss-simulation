"""
Helper helper_methods functions.
"""


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


# def binomial_pmf(n, k, p):
#     """
#     Computes the probability of getting 'k' of some random event with probability 'p'
#     out of 'n' trials assuming that the outcome of each trial is independent.
#     :param n: the number of trials
#     :param k: number of successes
#     :param p: the probability of an individual successful outcome
#     :return: the probability of getting k successes out of n trials
#     """
#     return n_choose_k(n, k) * (p**k) * (1-p)**(n-k)


def binomial_pmf(n, k, p, t):
    """
    Computes the probability of getting 'k' of some random event with probability 'p'
    out of 'n' trials assuming that the outcome of each trial is independent.  Also, the catch to this one is that
    if we get tails, we must toss 't' times
    :param n: the number of trials
    :param k: number of successes
    :param p: the probability of an individual successful outcome
    :param t: the number of tosses to make when getting tails
    :return: the probability of getting k successes out of n trials
    """
    return n_choose_k(n, k) * (p**t)**k * (1-(p**t))**(n-k)
