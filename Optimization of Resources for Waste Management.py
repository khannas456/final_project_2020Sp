import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
%matplotlib inline


def scenario_main():
    residents = 250
    trash_bin_size = 4  # 5 cubic yard trash
    print('Number of residents in Apartment Complex: ', residents)
    mc_stimulation = int(input('Number of MC stimulations:'))
    collections = int(input('Number of trash collection (suggestion 1 or 2):'))

    if collections == 1:
        bins = 11
        stimulate(mc_stimulation, bins, trash_bin_size, residents, collections)

    elif collections == 2:
        bins = 6
        stimulate(mc_stimulation, bins, trash_bin_size, residents, collections)

    elif collections > 2:
        print("Not a viable scenario")


def triangular(no_of_residents):
    wt=175
    triangular_values=list(np.random.triangular(1.5, 4.7, 8.1, no_of_residents))
    trash_residents= [x / wt for x in triangular_values]
    trash_weekly= [x*7 for x in trash_residents]
    complete_trash=sum(trash_weekly)
    return(complete_trash)


def stimulate(N, No_bins, bin_size, persons, collect):
    output_data = []
    for i in range(N):
        per_stimulation = []
        total_trash = 0

        capacity = bin_size * No_bins

        if collect == 1:
            total_trash = triangular(persons)
        if collect == 2:
            total_trash = triangular(persons)
            total_trash = total_trash / 2

        per_stimulation.append(persons)
        per_stimulation.append(No_bins)
        per_stimulation.append(capacity)
        per_stimulation.append(total_trash)

        value = threshold(total_trash, capacity)

        if value[2] == 1:
            per_stimulation.append(value[0])
            per_stimulation.append(0)
            per_stimulation.append("No")
            per_stimulation.append(value[1])


        elif value[2] == 2:
            per_stimulation.append(0)
            per_stimulation.append(value[0])
            per_stimulation.append("No")
            per_stimulation.append(value[1])

        elif value[2] == 3:
            per_stimulation.append(0)
            per_stimulation.append(0)
            per_stimulation.append(value[0])
            per_stimulation.append(value[1])

        output_data.append(per_stimulation)

    conclusions(output_data)