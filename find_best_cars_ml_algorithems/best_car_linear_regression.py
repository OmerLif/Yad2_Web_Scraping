from sklearn.linear_model import LinearRegression, Lasso, Ridge
from utils.data_utils import *


def find_best_car_using_linear_regression(df, X, y, model):
    # Create a linear regression model and fit it to the data
    reg = model().fit(X, y)

    # Calculate the predicted   prices for all the cars
    y_pred = reg.predict(X)

    # Calculate the absolute difference between the predicted prices and the actual prices
    diff = (y_pred - y)

    extract_best_cars_list(df, diff)


def main():
    df, X, y = data_preprocess()
    for model in [LinearRegression, Lasso, Ridge]:
        find_best_car_using_linear_regression(df, X, y, model)
