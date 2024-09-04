from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Read data from the Excel file
data = pd.read_excel(r"C:\Users\hoang\Downloads\Loan_data.xlsx")

# Extract 'Salary', 'Working Time', and 'Loan Decision' columns
df = pd.DataFrame(data, columns=['Salary', 'Working Time', 'Loan Decision'])

# Convert 'Salary' and 'Working Time' to numpy arrays
X = df['Salary'].values.reshape(-1, 1)  # Reshape to a 2D array for sklearn
y = df['Working Time'].values.reshape(-1, 1)
loan_decision = df['Loan Decision'].values  # No need to reshape since it's 1D

# Initialize and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict y values using the model for the given X values
y_pred = model.predict(X)

# Plot the original data points with color based on loan decision
for i in range(len(loan_decision)):
    if loan_decision[i] == 1:
        plt.plot(X[i], y[i], 'ro')  # Red for "Loan"
    else:
        plt.plot(X[i], y[i], 'bo')  # Blue for "No Loan"

# Plot the linear regression line
plt.plot(X, y_pred, 'g-', label='Approximation line')

# Add labels, a legend, and a grid
plt.xlabel('Salary')
plt.ylabel('Working Time')
plt.legend(['Loan', 'No Loan', 'Approximation line'])
plt.grid(True)

# Show the plot
plt.show()