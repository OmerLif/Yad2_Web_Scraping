import pandas as pd


def data_preprocess():
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('../resources/cars from Yad2 - all cars.csv')
    df = df.loc[df['Gir'] == 'אוטומט']

    y = df['Price']
    X = df[['Year', 'Kilometre', 'Engine Size', 'Car Model', 'Hand']]
    # Convert the 'Price' column to a numeric type
    y = y.str.replace(',', '').str.replace('₪', '').astype(float)

    # Convert the 'Kilometre' and 'Engine Size' columns to numeric types
    X.loc[:, 'Kilometre'] = X['Kilometre'].str.replace(',', '').astype(float)
    X.loc[:, 'Kilometre_2'] = X['Kilometre'] * X['Kilometre']
    X.loc[:, 'Year_Kilometre'] = X['Kilometre'] * X['Year']
    X.loc[:, 'Engine Size'] = X['Engine Size'].str.replace(',', '').astype(float)

    X = pd.get_dummies(X, columns=['Year', 'Car Model'])

    X = X.dropna()
    y = y[X.index]
    return df, X, y


def extract_best_cars_list(df, diff):
    # Sort the cars based on the difference in descending order
    sorted_cars = df.loc[diff.sort_values(ascending=False).index]
    # Select the top 10 cars with the largest difference
    best_cars = sorted_cars.loc[df['Car Model'] == 'קיה פיקנטו'].head(10)
    print(best_cars)