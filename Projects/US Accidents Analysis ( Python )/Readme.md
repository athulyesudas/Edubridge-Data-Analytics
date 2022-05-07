[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

Dataset Used: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

### Objective:

Explore the dataset provided and find the reasons that causing accidents and other insights about accidents in US.

### Description:

This is a countrywide car accident dataset, which covers 49 states of the USA. The accident data are collected from February 2016 to Dec 2021, using multiple APIs that provide streaming traffic incident (or event) data. These APIs broadcast traffic data captured by a variety of entities, such as the US and state departments of transportation, law enforcement agencies, traffic cameras, and traffic sensors within the road-networks. Currently, there are about 2.8 million accident records in this dataset. Check here to learn more about this dataset.

### Acknowledgements:

Please cite the following papers if you use this dataset:

Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. “A Countrywide Traffic Accident Dataset.”, 2019.

Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, Radu Teodorescu, and Rajiv Ramnath. "Accident Risk Prediction based on Heterogeneous Sparse Data: New Dataset and Insights." In proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, ACM, 2019.

### Content:

This dataset has been collected in real-time, using multiple Traffic APIs. Currently, it contains accident data that are collected from February 2016 to Dec 2021 for the Contiguous United States. Check here to learn more about this dataset.

### Inspiration:

US-Accidents can be used for numerous applications such as real-time car accident prediction, studying car accidents hotspot locations, casualty analysis and extracting cause and effect rules to predict car accidents, and studying the impact of precipitation or other environmental stimuli on accident occurrence. The most recent release of the dataset can also be useful to study the impact of COVID-19 on traffic behavior and accidents.

### Usage Policy and Legal Disclaimer:

This dataset is being distributed only for Research purposes, under Creative Commons Attribution-Noncommercial-ShareAlike license (CC BY-NC-SA 4.0). By clicking on download button(s) below, you are agreeing to use this data only for non-commercial, research, or academic applications. You may need to cite the above papers if you use this dataset.

## Structure :

### Task 1: Load the Data and Import Libraries
- Load the dataset using pandas.
- Import essential modules and helper functions from NumPy and Matplotlib & sklearn.
- Explore the dataframe using the head().

### Task 2: Inspect the Data
- Explore the dataframe using the shape, info() functions.
- Check the null values
- Get Statistical Overview using describe()
- Check skewness, kurtosis and range to get some idea about graph

### Task 3: Exploratory Data Analysis
- With the help of histogram, scatterplot, barplot(), histplot(), piechart, countplot() using Seaborn & Matplotlib to visualize the data
- Analysis of Data with each feature

## Insights:

 - California State has the most number of accidents.
 - Miami has the highest accidents amongst any city
 - Most of the accidents happen between 6am and 10am also between 12pm and 7pm
 - Accidents are more on weekdays than the weekends
 - Degree 2 severity of accidents is more common than the other three
 - Accidents are common at a junction, crossing or a traffic signal
