""" ROSS: Residential Occupancy Schedule Simulator
"""

import ROSS_functions as ft
import pandas as pd
import os, random

# random level - high, medium, low
rdmn_lvl = ft.get_input_from_user(
    "How much randomness do you want in your outcome? Select high, medium, or low: ",
    "Please input high, medium, or low",
    ['high', 'medium', 'low']
)
rdmn_lvl_int = ft.select_randomless(rdmn_lvl)  # converts the selected rdmn_lvl to an pre-defined integer

md = ft.get_input_from_user(
    "Do you want your occupancy schedule to be more motion-based? or schedule-based? Select 0 (motion-based) or 1 (schedule-based): ",
    "Please input 0 or 1",
    ['0', '1']
)
md = int(md)                               # converts str to int

day = ft.get_input_from_user(
    "Which day are you considering? Select Mon, Tue, Wed, Thu, Fri, Sat, or Sun: ",
    "Please input Mon, Tue, Wed, Thu, Fri, Sat, or Sun (case-sensitive)",
    ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
)

cwd = os.getcwd()
ndir = os.path.join(cwd, 'resource', 'rep_schs', 'method_0'+str(md))
files = os.listdir(ndir)
ptfn = [i for i in files if (day in i) & ('portion' in i)]
ptdt = pd.read_csv(os.path.join(ndir,ptfn[0]))
rv = random.random()                                                              # this value is to select a cluster
selectedCT = ft.selectCluster(rv,ptdt)                                            # get the selected cluster using selectCluster function
occ_schedule = ft.occupancySimulator(ndir, files, day, selectedCT, rdmn_lvl_int)
name = day+'_method'+str(md)+'_cluster'+str(selectedCT)+'_'+str(rdmn_lvl)         # the output file name
ft.scheduleSaver(occ_schedule,cwd,name)
