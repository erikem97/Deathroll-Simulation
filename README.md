# Deathroll simulation

Deathroll.py simulates the execpted value of the net profit of the second player in the dice game Deathroll. The input argument is the roll_number which ranges from 2-infinity. 
The output of deathroll is a file called "checkpoint_Deathroll(rollnumber).pkl". This file contains a dictionary containing: roll_number, EV, std_mean, number_simulation, r2_win.
roll_number = Highest number of the dice being used, EV = expexcted value of the net profit, std_mean = confidence intervall, number_simulations = Number of simulations,
r2 = number of wins for second player.

Run_Deathroll.py can be used to run and plot the results of Deathroll.py
DeathRoll_Calculation.py calculates the analytical value of Deathroll




Deatroll rules for World of warcraft:

To start, the player who goes first will have to roll the death-roll number that is 5,000 in our example. Therefore, type in /roll 5000. The game will get you a random number. Let’s say that you got 3138. The other player then has to roll using that number. In our case, they would type /roll 3138. The game will then roll the number between 1 and 3138 and give, let’s say, 447, at which point you will have to type /roll 447.

The procedure repeats until someone rolls a 1 and the first person to do so loses and has to pay up. That’s an endless source of fun right there!

Source: https://ragezone.com/2019/10/25/how-to-gamble-in-world-of-warcraft/


