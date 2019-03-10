## Coin Toss Simulation
This program is based off of a practice midterm problem for my Engineering Prob & Stats class.
Here is the problem:
> You toss _n_ coins, each showing heads with probability p, independently of other tosses.
Each coin that shows tails is tossed again (once more).  Let X be the total number of tails.
What is the probability mass function of the total number of tails X?

My good friend Max and I came up with the following formula:
![Alt text](/img/formula.png?raw=true "Formula image in img/formula.png")

Where X represents the number of tails, n represents the number of coins tossed, k is the number of tails that we choose, p is the probability of getting heads,
and t is the number of total maximum tosses we make.  For example, if t = 1, then we toss each coin only once, regardless of whether or not we land tails.  However, if t = 2, then after the first toss, if we have a tails, then we toss once more.
If t = 3, then on tails, we toss twice more (1 for initial toss + 2 extra tosses on tails = 3 total tosses).

## Motivation
I became a little obsessed with this problem. I came up with the theoretical formula which calculates the probability of
getting 'k' tails out of 'n' coins tossed with the caveat that, on tails, you must flip the coin again with a maximum of 't' tosses.
I wanted to verify that my formula was correct, since my TA disagreed.  In order to verify, one must compare the theoretical probabilities with the 
experimental ones.  By the law of big numbers, the experimental results of many random simulations of a scenario will get you close to the 
true theoretical proabability value.  Since we did similar simulations using R, I thought "why not come up with a new simulation
in python?"

## Code style
* [Python PEP8](https://www.python.org/dev/peps/pep-0008/)
 
## Screenshots
![Alt text](/img/plot-t-1.png "Plot 1 image in img/plot-t-1.png")
![Alt text](/img/plot-t-2.png "Plot 2 image in img/plot-t-2.png")
![Alt text](/img/plot-t-3.png "Plot 3 image in img/plot-t-3.png")


## Tech/framework(s) used
<b>Built with</b>
- [Python 3.7.0](https://www.python.org/downloads/)
- [MatPlotLib](https://matplotlib.org)

## Features
* Plots theoretical vs. simulated probabilities
* See how graph changes with changes in 't' tosses

## Installation
(Mac)
To get this program up and running on your machine, make sure you have python3 and PIP installed.
Clone/Fork this repo, cd into the directory, and create a virtual env for python3:
```
python3 -m venv venv
```
Activate the virtual environment
```
source venv/bin/activate
```
Install project dependencies:
```
pip install -r requirements.txt
```
Run the program:
```
python toss_simulation.py
```
Feel free to play around with different values of n.
Increase the number of simulations to have a more accurate plot.
