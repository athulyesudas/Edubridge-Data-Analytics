## Objective:
 - ### You are provided with daily historical sales data. The task is to forecast the total amount of products sold in every shop for the test set.

## File descriptions
 - sales_train.csv - the training set. Daily historical data from January 2013 to October 2015.
 - test.csv - the test set. You need to forecast the sales for these shops and products for November 2015.
 - sample_submission.csv - a sample submission file in the correct format.
 - items.csv - supplemental information about the items/products.
 - item_categories.csv  - supplemental information about the items categories.
 - shops.csv- supplemental information about the shops.


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
