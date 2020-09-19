# Cuisine-Prediction-using-Food-Ingredients

Machine Learning Project using a Kaggle dataset

The 2 datasets are as follows :-
submission.csv - cuisine id and the cuisine columns
train.csv - cuisine, respective id, and the ingredients used in that cuisine

The dataset was cleaned and processed

A number of graphs are also generated while the processing. These graphs include :-
Top 25 ingredients used (when all cuisines are considered)
Networkx graph to show the connection between 2 random ingredients
Cuisine with most number of ingredients
Cuisine with non-vegetarian ingredients (lamb, egg, chicken, or salmon) - Chinese cuisine has the maximum number of non-vegetarian ingredients
Cuisine with vegetarian ingredients - Japanese cuisine has the maximum number of vegetarian ingredients

top 10 ingredient in each cuisine was also calculated

A classification report was created to find the accuracy level for each cuisine (maximum for thai cuisine)

Various models were implemented for the Training portion
Some of the accuracy scores are as follows :-
Logistic Regression : 78%
K Neighbour Classifier : 63%
Random Forest Classifier : 75%
Ada Boost Classifier : 56%

Since the best score was of Logistic Regression, hence the model was further implemented and results dumped into a pickle file, which was later used in app.py of Flask to predict the results.
