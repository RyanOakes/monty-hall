#Monty Hall Simulation

##Synopsis Of Monty Hall Experiment

The eponymous gameshow host, Monty Hall, tempts contestants with a big prize, hidden behind one of three doors. The contestant begins by choosing a door but not opening it. Then, Monty steps forward and opens one of the other doors. He reveals a goat (!). Then the contestant has the choice of either sticking with the door they have already chosen, or switching to the other unopened door. Whichever door the contestant decides on will be opened, and if they find the prize, they get to keep it. I’m not sure what happens if they get the second goat!

People are biased towards sticking with what they’ve chosen, and the vast majority of people keep the door they originally picked. Intuitively, there should be an equal chance of the prize being behind any of the three doors, so it shouldn’t matter if you stick or switch. However, in this case, your intuition is wrong. You are twice as likely to win the prize if you switch to the other unopened door.

##Programming Objectives

1. Understand randomness
2. Understand the Monty Hall problem
3. Be able to use the Python random module
4. Be able to use randomness to perform a simulation

The primary task for this program is to run a Monty Hall-type simulation. It'll prove that switching doors is the best strategy by simulating 1000 games using each approach (keep or switch doors) and comparing the winning percentage.

##Running The simulation

There are two versions of the game here. The first (monty_hall.py) will run a 1,000 simulations of the game and NOT change doors after the initial goal reveal. The second (switch_doors_version.py) will run a 1,000 simulations of the game and SWITCH doors after the initial goal reveal.

Since each version shows a statistical output of victories at the end of the simulation, its quite apparent (although somewhat counterintuitive!) that switching doors results in twice the likelihood of winning!

This program was written in Python 3.5.1 and requires no additional installs. 
