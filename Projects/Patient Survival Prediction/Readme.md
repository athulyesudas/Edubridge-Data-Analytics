[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

Dataset Used: https://www.kaggle.com/datasets/sadiaanzum/patient-survival-prediction-dataset

### Objective:

Predict survival of patients based on their age and other important features.

### About Dataset:

Intensive Care Units (ICUs) often lack verified medical histories for incoming patients. A patient in distress or a patient who is brought in confused or unresponsive may not be able to provide information about chronic conditions such as heart disease, injuries, or diabetes. Medical records may take days to transfer, especially for a patient from another medical provider or system. Knowledge about chronic conditions can inform clinical decisions about patient care and ultimately improve patient's survival outcomes.

THE GLOBAL OPEN SOURCE SEVERITY OF ILLNESS SCORE (GOSSIS)

Raffa, Jesse1; Johnson, Alistair1; Celi, Leo Anthony2,,1; Pollard, Tom1; Pilcher, David3; Badawi, Omar4 33: THE GLOBAL OPEN SOURCE SEVERITY OF ILLNESS SCORE (GOSSIS), Critical Care Medicine: January 2019 - Volume 47 - Issue 1 - p 17
doi: 10.1097/01.ccm.0000550825.30295.dd

Copyright © 2018 by the Society of Critical Care Medicine and Wolters Kluwer Health, Inc. All Rights Reserved.

Source of the dataset: https://journals.lww.com/ccmjournal/Citation/2019/01001/33__THE_GLOBAL_OPEN_SOURCE_SEVERITY_OF_ILLNESS.36.aspx

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
- With the help of barplot(), lineplot(), kdeplot() using Seaborn & Matplotlib to visualize the data
- Analysis of Data with each feature

### Task 4: Machine Learning
- Data is split into two for training and testing.
- DecisionTreeClassifier, RandomForestClassifier, ExtraTreesClassifier, KNeighborsClassifier, GradientBoostingClassifier and GaussianNB is used for training and testing the dataset.
- Confusion_matrix is used for checking the accuracy.
- And the best model which has highest accuracy is selected for prediction.

## Results:

The tables bellow shows the accuracy for each model.

| ID | Model Name | Accuracy Percentage |
| :-: | :------------------------------------------: | :--------------------: |
|  1 | DecisionTreeClassifier | 88 |
|  2 | RandomForestClassifier | 92 |
|  3 | ExtraTreesClassifier | 92 |
|  4 | KNeighborsClassifier | 91 |
|  **5** | **GradientBoostingClassifier** | **93** |
|  6 | GaussianNB | 79 |

Gradient Boosting Classifier got the best accuracy. So, we will use this model for prediction.

