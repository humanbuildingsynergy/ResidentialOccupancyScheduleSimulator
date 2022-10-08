# Residential Occupancy Schedule Simulator (ROSS)

## Objective
ROSS creates a stochastic residential occupancy schedule by referencing occupancy schedules, extracted from a large smart thermostat dataset (over 90,000 thermostat data). Through ROSS, the Building Energy Modeling (BEM) community will have better access to a data-driven residential occupancy schedule.

## Methodology
ROSS references the occupancy schedules, identified through the time-series K-means clutering method using the ecobee Donate Your Data (DYD) dataset, to stochastically create a residential occupancy schedule. 

The stochastic nature of ROSS comes from an inhomogeous Markov chain, where the transitional probabilities are calculated using the representative occupancy schedules, and the inverse function method, which selected the occupancy status of the next step. The representative schedules were found through the time-series K-means clustering method using over 90,000 thermostat data at a five-minute interval in the DYD dataset.

More details will be shared once the paper below gets published.
- W. Jung, Z. Wang, T. Hong, F. Jazizadeh (2022) Smart Thermostat Data-driven Residential Occupancy Schedules and Development of a Residential Occupancy Schedule Simulator. TBD.

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

## Contributors
- [Wooyoung Jung]: Assistant Professor at the University of Arizona,
- [Zhe (Walter) Wang]: Assistant Professor at the Hong Kong University of Science and Technology,
- [Tianzhen Hong]: Senior Scientist at Lawrence Berkeley National Laboratory,
- [Farrokh Jazizadeh]: Associate Professor at Virginia Tech.

## Key references
- ecobee, Donate Your Data, https://ecobee.com/donate-your-data/, accessed 09.2022.
- J. Page, D. Robinson, N. Morel, and J. L. Scartezzini, A generalised stochastic model for the simulation of occupant presence. Energy and Buildings, 2008. 40(2): p. 83-98.

[Wooyoung Jung]: https://hubs.engr.arizona.edu/director.html
[Zhe (Walter) Wang]: https://facultyprofiles.hkust.edu.hk/profiles.php?profile=zhe-wang-cezhewang
[Tianzhen Hong]: https://eta.lbl.gov/people/tianzhen-hong
[Farrokh Jazizadeh]: https://www.inform-lab.org/farrokh-jazizadeh