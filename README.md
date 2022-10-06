# Residential Occupancy Schedule Simulator (ROSS)

## Objective
ROSS creates a stochastic residential occupancy schedule by referencing occupancy schedules, extracted from a large smart thermostat dataset (over 90,000 thermostat data). Through ROSS, the Building Energy Modeling (BEM) community will have better access to a data-driven residential occupancy schedule.

## Methodology
ROSS references the occupancy schedules, identified through the time-series K-means clutering method using the ecobee Donate Your Data (DYD) dataset, to stochastically create a residential occupancy schedule. 

The stochastic nature of ROSS comes from an inhomogeous Markov chain, where the transitional probabilities are calculated using the representative occupancy schedules, and the inverse function method, which selected the occupancy status of the next step. The representative schedules were found through the time-series K-means clustering method using over 90,000 thermostat data at a five-minute interval in the DYD dataset.

More details can be found in a journal paper, which is soon to be submitted to Energy and Buildings.

## Instruction
1. Clone this repository,
2. Execute ROSS.py,
3. Follow the instruction: ROSS requests three inputs from users to customize the results upon their needs.
    - Level of randomness: low, medium, and high
    - Occupancy identification approach: 0 (motion-based) or 1 (schedule-based).
        - motion-based: the occupancy schedule is more relied on motion data
        - schedule-based: the occupancy schedule is more relied on user-inputted schedules (e.g., the Home schedule)
    - Day of the week: from Mon to Sun
4. Once success, check out the result folder to see the csv file you created!

## Key references
- ecobee, Donate Your Data, https://ecobee.com/donate-your-data/, accessed 09.2022.
- J. Page, D. Robinson, N. Morel, and J. L. Scartezzini, A generalised stochastic model for the simulation of occupant presence. Energy and Buildings, 2008. 40(2): p. 83-98.
