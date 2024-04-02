import pandas as pd

# a. Create a data frame from CSV file
df_from_csv = pd.read_csv("empData.csv")

# b. Operations on Data Frame Shape, head, tail
# Display shape of the data frame
print("Shape of the data frame:")
print(df_from_csv.shape)

# Display first few rows of the data frame
print("\nFirst few rows of the data frame:")
print(df_from_csv.head())

# Display last few rows of the data frame
print("\nLast few rows of the data frame:")
print(df_from_csv.tail())

# Create a data frame from dictionary
data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df_from_dict = pd.DataFrame(data_dict)

# Create a data frame from list of tuples
data_tuples = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
df_from_tuples = pd.DataFrame(data_tuples, columns=['A', 'B', 'C'])

# Display the data frames
print("\nData Frame from dictionary:")
print(df_from_dict)

print("\nData Frame from list of tuples:")
print(df_from_tuples)
