## Week 2

 - people cluster: population cluster scales linearly with innovation, wealth and creativity.
 - evolution of transport: reinforcement of networks (original roads get bigger)

what zonal definition for modelling: MSOA good starting point (less coarse that ward - eg. Clifton).

Origin and Destination travelling for each zone.
- Origin number limited roughly by number of people that live in that zone.
- No clear trend for O vs D.
- O increases linearly (gradient of employment rate) with population of that zone
- more course zones for D reveales more single use areas for jobs.

Social Media data: can use eg twitter for location of where a tweets are posted for the same users as a journey.
 - smaller sample size
 - bias
 - live stream
 - uncontrolled


## Week 3

Distance. How do we calculate distance?
 - approxomate the planet as a sphere with `r=6371 km`. This takes into x,y,z cartisiean space. Calculate the Euclidean distance straight line from This
 - Geodesic takes into account the curvature on the surface of a sphere, which is more accurate for long range.
 - Isochrome map is a map of equal time (old fashioned)

What is distance?
 - Euclidean
 - shortest
 - quickest
 - cheapest
 - etc

Flow data. Standard to show adjacency OD matrix, but this doesn't show much.

`Gravity model`. populations between two points divided by distance. - look at example in the slides.

`Intervening opportunities model`. Takes into account how many 'opportunities' there are during the journey.

`Radiation model`. Sum the opportunities in the radius from the distance along the journey not just the journey itself.

We can compare these models against the empirical data sets using e.g. the F1 score.

What model is best? (look at slide for full reasons?) parameter free vs black-box.


## Week 4
* try question 12 on the worksheet.
* Q 14 extension, but is hard.
Optimisation always constrained to x_{i} >= 0 and sum of all x_{i} = d.

User Equilibrium
  - model for real life decision
  - users take the lowest cost path for themselves
  - Transferred to optimisation problem using Beckman's formula


System Optimal
  - Best cost for all users as a total
  - Theoretical


## Week 5
Beckman trick works even without the routes.
x are the links. y are the routes. -> `x = Ay`.
