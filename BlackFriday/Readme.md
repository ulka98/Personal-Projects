# BlackFriday

I practiced on the Black Friday Dataset as part of a recurring practice Machine Learning Competition held on AnalyticsVidhya.com (https://datahack.analyticsvidhya.com/contest/black-friday/#ProblemStatement). 

## Quoting the brief of the Dataset from the website:

A retail company “ABC Private Limited” wants to understand the customer purchase behaviour (specifically, purchase amount) against various products of different categories. They have shared purchase summary of various customers for selected high volume products from last month. The data set also contains customer demographics (age, gender, marital status, city_type, stay_in_current_city), product details (product_id and product category) and Total purchase_amount from last month.
Now, they want to build a model to predict the purchase amount of customer against various products which will help them to create personalized offer for customers against different products.

## Data
| Variable |	Definition |
| ---------| ------------|
| User_ID	 |  User ID    |
| Product_ID|	Product ID |
| Gender    | 	Sex of User|
| Age       |	Age in bins|
| Occupation|	Occupation (Masked)|
| City_Category|	Category of the City (A,B,C)|
|Stay_In_Current_City_Years|	Number of years stay in current city|
|Marital_Status|	Marital Status|
|Product_Category_1|	Product Category (Masked)|
|Product_Category_2|	Product may belongs to other category also (Masked)|
|Product_Category_3|	Product may belongs to other category also (Masked)|
|Purchase|	Purchase Amount (Target Variable)|

## Approach:

Initial analysis of the target variable is done at the beginning using ‘matplotlib’ and ‘seaborn’ libraries. Moreover, I have created several new columns from the existing data (Feature Engineering) to get more information to be used by the models. It will increase the efficiency of our models. The preprocessing and EDA of the dataset remain the same in every model notebook. Before using different algorithms I have fitted the training set into a DummyRegressor which will serve as a baseline model. I have tried different Bagging, Boosting, and Regression algorithms for prediction. You will see some notebooks have used hyperparameter tuning using RandomizedSearchCV, GridSearch, and BayesSearchCV. 
I have also used Kfold cross-validation approach to divide the dataset in 3-ways to increase the model prediction by defining a model_cv_score and LOO_score function.
These functions does the cross-validation and prints the train and test score of each fold.
