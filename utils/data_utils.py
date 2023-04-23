import pandas as pd


def preprocess_data():
    """
    This function reads the cars data from the CSV file, preprocesses the data,
    and returns the target variable and features.

    :return: df, X, y
    """
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv('../resources/cars from Yad2 - all cars.csv')
    except FileNotFoundError:
        print("Error: File not found")
        return None, None, None

    # Filter only cars with automatic transmission
    df = df.loc[df['Gir'] == 'אוטומט']

    # Extract the target variable and features
    y = df['Price']
    X = df[['Year', 'Kilometre', 'Engine Size', 'Car Model', 'Hand']]

    # Convert the 'Price' column to a numeric type
    y = y.str.replace(',', '').str.replace('₪', '').astype(float)

    # Convert the 'Kilometre' and 'Engine Size' columns to numeric types
    X.loc[:, 'Kilometre'] = X['Kilometre'].str.replace(',', '').astype(float)
    X.loc[:, 'Kilometre_2'] = X['Kilometre'] ** 2
    X.loc[:, 'Year_Kilometre'] = X['Kilometre'] * X['Year']
    X.loc[:, 'Engine Size'] = X['Engine Size'].str.replace(',', '').astype(float)

    # One-hot encode the categorical features
    X = pd.get_dummies(X, columns=['Year', 'Car Model'])

    # Remove any rows with missing values
    X = X.dropna()
    y = y[X.index]

    return df, X, y


def extract_best_cars_list(df, diff):
    """
    This function sorts the cars based on the difference in descending order and
    selects the top 10 cars with the largest difference.

    :param df: DataFrame containing the original data
    :param diff: array containing the difference between predicted and actual prices
    """
    # Sort the cars based on the difference in descending order
    sorted_cars = df.loc[diff.sort_values(ascending=False).index]
    # Select the top 10 cars with the largest difference
    best_cars = sorted_cars.loc[df['Car Model'] == 'קיה פיקנטו'].head(10)
    print("10 Best cars:")
    print(best_cars)
