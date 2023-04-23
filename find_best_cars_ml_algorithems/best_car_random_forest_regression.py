from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, KFold
from utils.data_utils import *


def predict_best_cars_using_random_forest(df, X, y, model):
    """
      This function trains a random forest regression model using grid search
      and cross-validation, and extracts the best cars.

      :param df: DataFrame containing the original data
      :param X: DataFrame containing the input features
      :param y: Series containing the target variable
      :param model: random forest model class
    """
    # Define the hyper-parameters to search
    print("Performing hyperparameter tuning...")
    grid_search = hyper_parameters_tunning(X, model, y)
    # Train the model with the best hyperparameters on the full dataset
    best_rf = grid_search.best_estimator_
    best_rf.fit(X, y)
    # Evaluate the model on the training set
    y_train_pred = best_rf.predict(X)
    diff = y_train_pred - y
    extract_best_cars_list(df, diff)


def hyper_parameters_tunning(X, model, y):
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [5, 10, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
    }
    # Define the cross-validation strategy
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    # Define the model
    rf = model(random_state=42)
    # Search for the best hyperparameters using grid search and cross-validation
    grid_search = GridSearchCV(rf, param_grid=param_grid, cv=kf, scoring='neg_mean_squared_error')
    grid_search.fit(X, y)
    # Print the best hyperparameters and score
    print("Best hyperparameters: ", grid_search.best_params_)
    print("Best score: ", grid_search.best_score_)
    return grid_search


def main():
    df, X, y = preprocess_data()
    print("Starting random forest regression algorithm...")
    predict_best_cars_using_random_forest(df, X, y, RandomForestRegressor)


if __name__ == '__main__':
    main()
