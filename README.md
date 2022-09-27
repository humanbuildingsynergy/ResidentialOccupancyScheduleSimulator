# ResidentialOccupancyScheduleSimulator

## Objective
Residential Occupancy Schedule Simulator (ROSS) creates a stochastic residential occupancy schedule by referencing occupancy schedules, extracted from a large smart thermostat dataset (over 90,000 thermostat data). Through ROSS, the Building Energy Modeling (BEM) community will have better access to a data-driven residential occupancy schedule.

## Methodology
ROSS references the occupancy schedules, identified through the time-series K-means clutering method using the ecobee Donate Your Data (DYD) dataset, to stochastically create a residential occupancy schedule. 

The stochastic nature of ROSS comes from an inhomogeous Markov chain, where the transitional probabilities are calculated using the representative occupancy schedules, and the inverse function method, which selected the occupancy status of the next step. The representative schedules were found through the time-series K-means clustering method using over 90,000 thermostat data at a five-minute interval in the DYD dataset.

More details can be found in a journal paper, which is soon to be submitted to Energy and Buildings.

## Instruction.
1. Clone this repository
2. execute ROSS.py
3. Follow the instruction.
    - ROSS requests several inputs from users to customize the results upon their needs
4. Once success, check out the result folder to see the csv file you created!

## Key reference
- ecobee, Donate Your Data, https://ecobee.com/donate-your-data/, accessed 09.2022.
- J. Page, D. Robinson, N. Morel, and J. L. Scartezzini, A generalised stochastic model for the simulation of occupant presence. Energy and Buildings, 2008. 40(2): p. 83-98.
