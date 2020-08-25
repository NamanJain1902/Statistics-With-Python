## Build cars DataFrame
```python
import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)
```
# Definition of row_labels
```python
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)
```

# Import the cars.csv data: cars
```python
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)
# Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print( cars[['country','drives_right']] )

# Print out first 3 observations
print(cars[:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])
```
> With loc and iloc you can do practically any data selection operation on DataFrames you can think of. loc is label-based, which means that you have to specify rows and columns based on their row and column labels. iloc is integer index based, so you have to specify rows and columns by their integer index.
```python
# Print out observation for Japan
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG']])

# Print out drives_right value of Morocco
print(cars.loc['MOR','drives_right'])
```
> loc and iloc also allow you to select both rows and columns from a DataFrame.
```python
# Print sub-DataFrame
print(cars.loc[['RU','MOR'],['country','drives_right']])

```