import pandas as pd

# Load the Titanic training and test datasets
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# Print the first few rows of the training data to check if it's loaded correctly
print(train_data.head())


