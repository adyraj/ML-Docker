# Import required libraries
import pandas
import joblib
from sklearn.linear_model import LinearRegression

# Load dataset
dataset = pandas.read_csv('SalaryData.csv')

dataset.columns
y = dataset['Salary']
x = dataset['YearsExperience']
type(x)
x = x.values
type(x)
x.shape

# Reshape the feature
x = x.reshape(-1, 1)
x.shape

# Create model
model = LinearRegression()

# Train the model
model.fit(x,y)

# Save the trained model
joblib.dump(model , 'salary.pk1')