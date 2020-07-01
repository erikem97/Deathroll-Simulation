import random
import math
import argparse
import pickle
from os import path

def death_sim(roll_number, EV, std_mean, number_simulation, r2_win):
    gold = roll_number*0.1
    while std_mean > abs(0.01*EV) or number_simulation < 10**6:
        x = roll_number
        r1 = roll_number
        r2 = roll_number
        while r1 > 1 and r2 > 1:
            r1 = random.randint(1, x)
            x = r1
            if r1 > 1:
                r2 = random.randint(1, x)
                x = r2
            else:
                r2_win += 1
        number_simulation += 1
        win_rate = r2_win / number_simulation
        EV = (win_rate * (gold * 2) - gold)
        std_mean = (gold * math.sqrt(win_rate - (win_rate ** 2)) / math.sqrt(number_simulation))  # std EV gold
        if number_simulation % 10**5 == 0:
            cp = dict(roll_number=roll_number, EV=EV, std_mean=std_mean, number_simulation=number_simulation, r2_win=r2_win)
            print(cp)
            with open("checkpoint_Deathroll"+str(roll_number)+".pkl", "wb") as cp_file:
                pickle.dump(cp, cp_file)

    cp = dict(roll_number=roll_number, EV=EV, std_mean=std_mean, number_simulation=number_simulation, r2_win=r2_win)
    print(cp)
    with open("checkpoint_Deathroll" + str(roll_number) + ".pkl", "wb") as cp_file:
        pickle.dump(cp, cp_file)

def main():
    parser = argparse.ArgumentParser(description='Deathroll simulation')
    parser.add_argument('roll_number', help="Number between 2-100", type=int)
    args = parser.parse_args()
    file_name = "checkpoint_Deathroll"+str(args.roll_number)+".pkl"
    if path.exists(file_name):
        # A file name has been given, then load the data from the file
        with open(file_name, "rb") as cp_file:
            cp = pickle.load(cp_file)
        roll_number = cp["roll_number"]
        EV = cp["EV"]
        std_mean = cp["std_mean"]
        number_simulation = cp["number_simulation"]
        r2_win = cp["r2_win"]
        if number_simulation < 10**6 or std_mean > 0.01*EV:
            death_sim(roll_number, EV, std_mean, number_simulation, r2_win)

    else:
        death_sim(args.roll_number, 0, 0, 0, 0)


if __name__ == '__main__':
    main()