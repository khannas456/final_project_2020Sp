'''
Libraries Used for the project
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math


def scenario_main(residents, trash_bin_size, mc_stimulation, collections):
    '''
    For this mc stimulation we are using fixed residents in the complex "250" along with that the trash bin size is 4 cubic yards.
    This will also ask for the input for number of collections
    :return:This will return the stimulations, number of residents, trash bin size and the number of collections each week
    >>>scenario_main(250, 4, 1000, 7)
    Not a viable scenario
    '''
    if collections == 1:
        bins = 11
        stimulate(mc_stimulation, bins, trash_bin_size, residents, collections)

    elif collections == 2:
        bins = 6
        stimulate(mc_stimulation, bins, trash_bin_size, residents, collections)

    elif collections > 2:
        print("Not a viable scenario")


def triangular(no_of_residents):
    '''
    This will generate the amount of trash produced by a person through triangular distribution and produce the total trash for total number of residents weekly
    :param no_of_residents: The total number of residents in an apartment complex
    :return:The amount of trash produced weekly by all residents
    >>>triangular(250)
    >>>if complete_trash >= 42 and complete_trash <= 53
    ...print(True)
    >>>else:
    ...print(False)
    True
    '''
    wt=175
    triangular_values=list(np.random.triangular(1.5, 4.7, 8.1, no_of_residents))
    trash_residents= [x / wt for x in triangular_values]
    trash_weekly= [x*7 for x in trash_residents]
    complete_trash=sum(trash_weekly)
    return(complete_trash)


def stimulate(N, No_bins, bin_size, persons, collect):
    '''
    This will apply the monte carlo stimulation. We check the number of collection over which we see how much trash is produced and create output for each simulation and a end result for all stimulations.
    :param N:Input the number of stimulations
    :param No_bins:Number of dustbins required in the apartment complex
    :param bin_size:The Dustbin size as required for the apartment complex
    :param persons:The number of residents in the apartment complex
    :param collect:Input of Number of weekly collections, 1 or 2
    :return:This will produce results for all the stimulations
    >>>
    '''
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


def threshold(trash, cap):
    '''
    :param trash:
    :param cap:
    :return:
    '''
    if trash < cap:
        Underfull = 100 - (trash / cap * 100)
        Underfull = round(Underfull, 3)
        return ([Underfull, "Underfull", 1])

    elif trash > cap:
        overfull = (trash - cap) / cap * 100
        overfull = round(overfull, 3)
        return ([overfull, "Overfull", 2])

    elif int(trash) == cap:
        full = "YES"
        return ([full, "Full", 3])


def conclusions(data):
    '''
    :param data:
    :return:
    '''
    final_data = pd.DataFrame(data)
    final_data = final_data.rename(
        columns={0: 'Number of Residents', 1: "Number of Bins", 2: "Trash Capacity", 3: "Total Trash per week",
                 4: "Percent Empty", 5: "Percent Over Fill", 6: "Is Full?", 7: "Status of Bins"})
    report = final_data.describe()
    display(final_data)
    display(report)

    final_data["Clean"] = final_data["Status of Bins"] == 'Underfull'
    values = []
    for i in range(len(final_data)):
        if final_data["Percent Empty"][i] != 0.0:
            values.append(final_data["Percent Empty"][i])
        elif final_data["Percent Over Fill"][i] != 0.0:
            values.append(-(final_data["Percent Over Fill"][i]))
        else:
            values.append(0)

    final_data["Percentage Clean"] = values

    fig = plt.figure(figsize=(10, 18))
    final_data["Percentage Clean"].plot(kind='barh', color=final_data.Clean.map({True: 'g', False: 'r'}))
    plt.title("The Percentage of Status and Cleanliness of the Bins")
    plt.xlabel('Percentage Empty or Overfull')
    plt.ylabel('Number of Stimulations')
    plt.show()

    plt.hist(final_data["Total Trash per week"], bins="auto")
    plt.ylabel('Number of Bins')
    plt.xlabel('Status of Bins')
    plt.title("Histogram for Total Trash")
    plt.show()

    final_data["Status of Bins"].value_counts().plot(kind="bar")
    plt.title("Number of Bins under each Status")
    plt.show()



# View of triangular distributions
def triangular_stimulations(no_of_residents):
    '''
    :param no_of_residents:
    :return:
    '''
    plt.hist(np.random.triangular(1.5, 4.7, 8.1, no_of_residents), bins=200)
    plt.title("The Triangular Distribution Graph")
    plt.show()

triangular_stimulations(20000)


#I am yet to upload the doctest and docstrings i.e. the final version

if __name__ == '__main__':
    total_residents = 250
    trash_size = 4  # 4 cubic yard trash
    print('Number of residents in Apartment Complex: ', total_residents)
    stimulations = int(input('Number of MC stimulations:'))
    collect = int(input('Number of trash collection (suggestion 1 or 2):'))

    scenario_main(total_residents, trash_size, stimulations, collect)