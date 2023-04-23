from sklearn.linear_model import LinearRegression, Lasso, Ridge
from utils.data_utils import *


def predict_best_car_using_linear_regression(df, X, y, model):
    """
    Fits a linear regression model to the data, calculates the predicted prices, and extracts the best cars based on the
    difference between predicted and actual prices.

    Args:
        df (pandas.DataFrame): The original preprocessed data.
        X (pandas.DataFrame): The features to use for training the model.
        y (pandas.Series): The target variable to predict.
        model (class): The linear regression model class to use.

    Returns:
        None
    """

    # Create a linear regression model and fit it to the data
    reg = model().fit(X, y)

    # Calculate the predicted prices for all the cars
    y_pred = reg.predict(X)

    # Calculate the absolute difference between the predicted prices and the actual prices
    diff = y_pred - y

    # Extract the best cars based on the difference in descending order
    extract_best_cars_list(df, diff)


def main():
    # Preprocess the data
    df, X, y = preprocess_data()

    # Check if the data is valid
    if df is None or X is None or y is None:
        print("Error: Invalid data")
        return

    # Loop through the linear regression models to use
    for model in [LinearRegression, Lasso, Ridge]:
        print("Using model:", model.__name__)
        # Use the current model to predict the best cars
        predict_best_car_using_linear_regression(df, X, y, model)


if __name__ == '__main__':
    main()
