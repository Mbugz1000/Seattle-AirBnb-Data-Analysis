# Seattle AirBNB Data
## Installation
Run the following command to set up the environment for this project. 

```
conda create --name project_1_udacity python==3.7.3 && conda activate project_1_udacity && conda install pandas jupyterlab altair "pandas-profiling>2.0" geopy sklearn lightgbm
```

Download the datasets used in this project here:
- [reviews.csv.gz](http://data.insideairbnb.com/united-states/wa/seattle/2021-09-25/data/reviews.csv.gz)
- [calendar.csv.gz](http://data.insideairbnb.com/united-states/wa/seattle/2021-09-25/data/calendar.csv.gz)
- [listings.csv.gz](http://data.insideairbnb.com/united-states/wa/seattle/2021-09-25/data/listings.csv.gz)

Once downloaded, dump this data in _/data/raw_


## Project Motivation
This is the first of several Udacity projects in the Data Science Nano-degree program. The primary aim of this project 
is therefore to complete the course-work of the mentioned program. 

The secondary aim of this project was to answer the 4 business questions related to AirBnB Seattle listings:
1. Does becoming a verified host positively impact your monthly income or occupancy rate in Seattle?
1. Does becoming a Super-Host positively impact your monthly income or occupancy rate in Seattle?
1. Does close proximity to competition negatively impact your monthly income?
1. What factors should influence the rate you set for your listing?

## How to Interact with Project
This project is has 2 primary folders: 
- **data** : Data Folder. It contains 2 folders
    - **processed**: Output of the analysis
    - **raw**: The raw data downloaded from InsideAirBnb
- **src**: Source code folder. It contains 2 files:
    - **Analysis Notebook**: Jupyter notebook where the analysis was performed
    - **multiprocessing_fn**: A python module that is imported by the notebook

To interact with the project, take the following steps:
1. Activate the _project_1_udacity_ environment on the Anaconda console
1. Navigate to the directory of the project on the Anaconda Console
1. Start up Jupyter Lab using the command `jupyter lab`
1. Open the Analysis notebook from the jupyter notebook page

## Results Summary
The results of this analysis were as follows: 
1. Does becoming a verified host positively impact your monthly income or occupancy rate in Seattle? 
   - No. It does not positively impact your monthly AirBnb income in Seattle
1. Does becoming a Super-Host positively impact your monthly income or occupancy rate in Seattle? 
   - Yes. It positively impacts your monthly income by $900 on average in Seattle
1. Does close proximity to competition negatively impact your monthly income? 
   - Yes. It negatively impacts your monthly income by $300 on average in Seattle
1. What factors should influence the rate you set for your listing? 
   - The top 5 listing based factors that should be considered are as follows: 
        1. No. of guests that you can accommodate
        1. Location of your listing
        1. Competition in your area
        1. Kitchen appliances that you offer
        1. Type of property

## Licensing, Authors & Acknowledgements
- [Think Stats: Exploratory Data Analysis by Allen B. Downey](https://www.amazon.com/gp/product/1491907339/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1491907339&linkCode=as2&tag=greenteapre01-20&linkId=JVSYKQHYSUIEYRHL)
- [Statistical Significance with the help of Python by Jeremiah Lutes](https://towardsdatascience.com/statistical-significance-with-the-help-of-python-1fbb318ce216)
- [Inside AirBnb Project by Murray Cox](http://insideairbnb.com/about.html)

