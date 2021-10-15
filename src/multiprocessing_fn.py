from geopy.distance import geodesic
import pandas as pd


def distance_method(latlong_values):
    """
    This method calculates the distance between 2 points. 
    
    **NB** It has been placed in this file to support MultiProcessing on a Jupyter Notebook
    
    :param latlong1:
    :param latlong2:
    :return: The number of listings that are below 500m away, those that are between 500m and 1.5 km and those between 1.5km and 4km
    """
    distances = pd.Series([geodesic(latlong_values[0], lat_long).kilometers for lat_long in latlong_values[1]])
    
    less_than_500 = ((distances < 0.5).values & latlong_values[2].values).sum()

    less_than_1500 = ((distances < 1.5).values & latlong_values[2].values).sum()

    less_than_4000 = ((distances < 4).values & latlong_values[2].values).sum()
    
    return less_than_500, less_than_1500, less_than_4000