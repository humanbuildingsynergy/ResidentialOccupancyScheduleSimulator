""" This file contains the functions that ROSS utilizes.
"""

import pandas as pd
import numpy as np
import os, random, typing

def selectCluster(randomValue: float, portionDF: pd.DataFrame):
    """ Selects one of the clusters using the inverse function method
    
    Args:
    - randomValue: a random value for the inverse function method
    - portionDataframe: the dataframe that contains the portion of each cluster (e.g., Mon_portion.csv)

    Returns:
    - result (int): an integer indicating the selected cluster.
    """

    portionDF = portionDF[portionDF.columns[1:]].iloc[0] # get portions of each cluster
    nCluster = int(portionDF.index[-1])                                # get number of clusters
    for i in range(0,nCluster+1):                                             # perform an inverse function method
        randomValue = randomValue - portionDF[str(i)]
        if randomValue < 0:
            result = i
            break
        else:
            continue
    print('the selected cluster is ' + str(i))                                    # print out which cluster has been selected (this for the user)
    return result

def scheduleSaver(sch: pd.DataFrame, dir: str, name: str):
    """ Saves the final schedule csv file in the directory

    Args:
    - sch: the schedule dataframe
    - dir: directory where the schedule file will be saved.
    - name: the name of the file

    Returns: the csv file with a stochatically created schedule
    """

    csvName = name+'.csv'
    sch.to_csv(os.path.join(dir, 'result', csvName))
    print(csvName+' Saved successfully')

def stchatic_presence_sch_creator(new_sch: typing.List, ref_sch: typing.List, ini_state: int):
    """ Inverse Function Method with an inhomogeneous Markov Chain

    Args:
    - new_sch: the new presence schedule with the initial state.
    - ref_sch: the reference occupancy schedule (i.e., the representative occupancy schedule that is randomly selected).
    - ini_state: the initial state (either absence or presence)

    Returns: new_sch contains a stochastic presence schedule
    """

    digit = 4
    # mb: the parameter of mobility (from 0.0 to 1.0)
    # ROSS uses 1.0 as the default value as mb becomes near 0.0, the probabiliy of having 0 becomes considerably high,
    # , so the outcome of ROSS doesn't necessarily follow the reference schedule.
    mb = 1 
    for i in range(len(ref_sch) - 1):
        pt = ref_sch[i]
        pt_1 = ref_sch[i+1]
        T_01 = np.round((mb - 1) * (mb +1) * pt + pt_1, digit)                                  # T_00: no transition from vacancy to vacancy, T_01: transition from vacancy to presence,
        T_11 = np.round((pt - 1) / pt * ((mb - 1) / (mb + 1) * pt + pt_1) + pt_1 / pt, digit)   # T_10: transition from presence to vacancy, T_11: no transition from presence to presence
        temp_mb = mb
        # this is where mb gets updated until the probabilities become reasonable.
        if T_01 > 1:
            while True:
                temp_mb += 0.01
                T_01 = np.round((temp_mb - 1) * (temp_mb +1) * pt + pt_1, digit)
                if T_01 <= 1:
                    break
        if T_11 > 1:
            while True:
                temp_mb += 0.01
                T_11 = np.round((pt - 1) / pt * ((temp_mb - 1) / (temp_mb + 1) * pt + pt_1) + pt_1 / pt, digit)
                if T_11 <= 1:
                    break
        T_00 = np.round(1.00 - T_01, digit)
        T_10 = np.round(1.00 - T_11, digit)
        temp = np.round(np.random.uniform(0,1,1), digit)[0]
        # inverse transform function
        if ini_state == 0:                                      # currentState is 0 (absence)
            if temp <= T_00:
                ini_state = 0
            else:                                               # temp > T_00 means that T_01 happens
                ini_state = 1
        else:                                                   # currentState is 1 (presence)
            if temp <= T_10:
                ini_state = 0
            else:                                               # temp > T_10 means that T_11 happens
                ini_state  = 1
        new_sch.append(ini_state)
    return new_sch

def occupancySimulator(dir: str, files: typing.List, day: str, selectedCT, rep: int):
    """ Occupancy simulator, inspired by the paper Page, J., Robinson, et al. (2008) A generalized stochastic model for the simulation of occupant presence. Energy and Buildings 40(2), 83-98.
    Note: This simulator addressed several limitations of the original approach and the details can be found in the paper.

    Args:
    - dir: directory of where ROSS is located.
    - files: the csv files that contain the information of clusters
    - day: the selected day (e.g., 'Mon')
    - selectedCT: a randomly selected cluster
    - rep: the number of presence schedules considered in ROSS
    """
    
    fn = [i for i in files if (day in i) & ('_centerCluster' in i)]
    ndt = pd.read_csv(os.path.join(dir,fn[0]))
    ndt.set_index('DateTime', inplace=True)
    ndt = ndt[str(selectedCT)]
    ndt = pd.concat([ndt,ndt.iloc[0:24]])
    ref_sch = ndt.tolist()
    ini_st = 1                                                               # initial state; Starts the inhomogeneous Markov chain with presence.
    occStates = {'Time':ndt.index.tolist()}                                  # a dictionary where 
    for i in range(0,rep):
        new_sch = []                                                         # new_sch: the new presence schedule
        new_sch.append(ini_st)
        new_sch = stchatic_presence_sch_creator(new_sch, ref_sch, ini_st)
        occStates.update({i:new_sch})
    occdt = pd.DataFrame(occStates)
    occdt.set_index('Time', inplace=True)
    sch = occdt.mean(axis=1).iloc[24:].rename('StochasticOccupancySchedule')           # sch: the new occupancy schedule
    sch = pd.DataFrame(sch)
    sch = pd.concat([sch.iloc[-24:],sch.iloc[:-24]])
    return sch

def select_randomless(ipt: str):

    """ Returns the number of stochastic presence schedules that will be considered in ROSS

    Args:
    - ipt: either 'high', 'medium', and 'low', determined by the user

    Return: opt (int): returns 20, 200, 1000, or None (if the user provides unexpected value).
    """

    ipt = str(ipt).lower()
    if ipt == "high":
        opt = 20
    elif ipt == "medium":
        opt = 200
    elif ipt == "low":
        opt = 1000
    else:
        opt = None
    return opt

def get_input_from_user(
    msg: str,
    err_msg: str,
    psbl_answers: typing.List
):
    """ Gets an input from a user until it's valid.

    Args:
    - msg: the message that the user sees at first
    - err_msg: when invalid answers were given by the user, this message pops out.
    - psbl_answers: the list of possible answers.

    Returns: ipt (str): the input from the user.
    """

    while True:
        try:
            ipt = input(msg)
        except ValueError:
            print(err_msg)
            continue
        else:
            if ipt not in psbl_answers:
                print(err_msg)
                continue
            else:
                break
    return ipt