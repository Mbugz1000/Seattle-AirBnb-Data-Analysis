# Seattle AirBNB Data
## Installation

```
conda create --name project_1_udacity python==3.7.3 && conda activate project_1_udacity && conda install pandas jupyterlab altair "pandas-profiling>2.0" geopy sklearn
```

## Project Motivation
Business Questions:
1. Is there a significant difference between the returns of verified and non-verified host's listings?
1. What factors most strongly contribute to high occupancy rates/ high income per month or high nights per year in Seattle?
1. Does proximity to competition/ certain kinds of competition affect returns of surrounding AirBnB listings?

Suggestions
1. Build an ML model (regression)

NB:
1. AirBnb reviews can be used as an indicator for activity
1. Income per month for each listing can be estimated using the minimum stay, price and number of reviews are used to estimate
   occupancy rate and estimated income per month 
1. Location information for listings are anonymized by Airbnb. In practice, this means the location for a listing on the
   map, or in the data will be from 0-450 feet (150 metres) of the actual address.
1. instant_bookable: When this value is true, it's an indicator of a commercial listing.

Refer to InsideAirBnB's [Disclaimer](http://insideairbnb.com/about.html#disclaimers) for more details

TODO:
- [ ] Calculate Occupancy & Income Per Month and Nights per year
- [ ] Systematically answer each question one by one


Interesting fields:
1. Name of Listing: (Add Length of title & most common words)
1. Host reponse time
1. Host acceptance rate
1. Host is super host
1. ~~Host Verifications. Anything interesting to be gleaned here?~~
1. Whether the host has a picture. Whether there is an image for the listing


## How to Interact with Project



## Licensing, Authors & Acknowledgements

