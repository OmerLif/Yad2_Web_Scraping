import pandas as pd
from sklearn.linear_model import LinearRegression, Lasso, Ridge


# Read the CSV file into a pandas DataFrame
df = pd.read_csv('cars from Yad2 - all cars.csv')
df = df[df['Gir'] == 'אוטומט']

y = df['Price']
X = df[['Year', 'Kilometre', 'Engine Size', 'Car Model', 'Hand']]
X['Year'] = max(df['Year']) - min(df['Year']) / min(df['Year']) 
# Convert the 'Price' column to a numeric type
y = y.str.replace(',', '').str.replace('₪', '').astype(float)


# Convert the 'Kilometre' and 'Engine Size' columns to numeric types
X['Kilometre'] = X['Kilometre'].str.replace(',', '').astype(float)
X['Engine Size'] = X['Engine Size'].str.replace(',', '').astype(float)


# Drop rows with missing values
X = X.dropna()
y = y[X.index]
# One-hot encode the 'Year' and 'Car Model' column
X = pd.get_dummies(X, columns=['Year', 'Car Model'])


# Create a linear regression model and fit it to the data
reg = LinearRegression().fit(X, y)

# Calculate the predicted   prices for all the cars
y_pred = reg.predict(X)

# Calculate the absolute difference between the predicted prices and the actual prices
diff = (y_pred - y)

# Sort the cars based on the difference in descending order
sorted_cars = df.loc[diff.sort_values(ascending=False).index]

# Select the top 10 cars with the largest difference
best_cars = sorted_cars.head(10)

print(best_cars)
