[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

Dataset Used: https://www.kaggle.com/competitions/competitive-data-science-predict-future-sales/data

## Objective:
 - ### You are provided with daily historical sales data. The task is to forecast the total amount of products sold in every shop for the test set.

## Data Description:

You are provided with daily historical sales data. The task is to forecast the total amount of products sold in every shop for the test set. Note that the list of shops and products slightly changes every month. Creating a robust model that can handle such situations is part of the challenge.

## File descriptions:

 - sales_train.csv - the training set. Daily historical data from January 2013 to October 2015.
 - test.csv - the test set. You need to forecast the sales for these shops and products for November 2015.
 - sample_submission.csv - a sample submission file in the correct format.
 - items.csv - supplemental information about the items/products.
 - item_categories.csv  - supplemental information about the items categories.
 - shops.csv- supplemental information about the shops.

## Data fields:

 - ID - an Id that represents a (Shop, Item) tuple within the test set
 - shop_id - unique identifier of a shop
 - item_id - unique identifier of a product
 - item_category_id - unique identifier of item category
 - item_cnt_day - number of products sold. You are predicting a monthly amount of this measure
 - item_price - current price of an item
 - date - date in format dd/mm/yyyy
 - date_block_num - a consecutive month number, used for convenience. January 2013 is 0, February 2013 is 1,..., October 2015 is 33
 - item_name - name of item
 - shop_name - name of shop
 - item_category_name - name of item category

This dataset is permitted to be used for any purpose, including commercial use.


## Libraries Used:

![alt text](https://github.com/athulyesudas/Edubridge-Data-Analytics/blob/main/Projects/Predicting%20Future%20Sales/Screenshots/libraries.png?raw=true)

## Translation Using GoogleTrans:

![alt text](https://github.com/athulyesudas/Edubridge-Data-Analytics/blob/main/Projects/Predicting%20Future%20Sales/Screenshots/google.png?raw=true)

## Barchart:

![alt text](https://github.com/athulyesudas/Edubridge-Data-Analytics/blob/main/Projects/Predicting%20Future%20Sales/Screenshots/barchart.png?raw=true)

## WordCloud:

![alt text](https://github.com/athulyesudas/Edubridge-Data-Analytics/blob/main/Projects/Predicting%20Future%20Sales/Screenshots/wordcloud.png?raw=true)

## Training Model:

![alt text](https://github.com/athulyesudas/Edubridge-Data-Analytics/blob/main/Projects/Predicting%20Future%20Sales/Screenshots/training.png?raw=true)

## Conclusion:

| Model                     | Accuracy    | Runtime     |  
| ------------------------- | ----------- | ----------- |
| RandomForestRegressor     | 94.29 %     | 3 min         |
| DecisionTreeRegressor     | 93.10 %     |    5 sec         |
| ExtraTreesRegressor       | 94.15 %     |    5 min         |

- When we consider accuracy <b>RandomForestRegressor</b> is more suitable.
- And if we consider speed then <b>DecisionTreeRegressor</b> is the more suitable.

And in this case as runtime is not very high with <b>RandomForestRegressor</b> so i used it as my final model for prediction.
