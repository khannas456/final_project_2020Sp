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

