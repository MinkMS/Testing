from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data: Area (m2) and Price (VND in millions)
X = np.array([[30, 32.4138, 34.8276, 37.2414, 39.6552, 42.069, 44.4828, 46.8966, 49.3103,
               51.7241, 54.1379, 56.5517, 58.9655, 61.3793, 63.7931, 66.2069, 68.6207,
               71.0345, 73.4483, 75.8621, 78.2759, 80.6897, 83.1034, 85.5172, 87.931,
               90.3448, 92.7586, 95.1724, 97.5862, 100]]).T
y = np.array([[448.524, 509.248, 535.104, 551.432, 623.418, 625.992, 655.248, 701.377,
               748.918, 757.881, 831.004, 855.409, 866.707, 902.545, 952.261, 995.531,
               1069.78, 1074.42, 1103.88, 1138.69, 1153.13, 1240.27, 1251.9, 1287.97,
               1320.47, 1374.92, 1410.16, 1469.69, 1478.54, 1515.28]]).T

# Initialize and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Function to predict house price based on the area (space)
def predict_price(area):
    area_reshaped = np.array([[area]])  # Reshape for prediction
    predicted_price = model.predict(area_reshaped)
    return predicted_price[0][0]

# Visualize data and the regression line
y_pred = model.predict(X)

plt.plot(X, y, 'ro', label='Data points')
plt.plot(X, y_pred, 'b-', label='Approximation line')
plt.xlabel('Area (m²)')
plt.ylabel('Price (VND million)')
plt.legend()
plt.grid(True)
plt.show()

area = float(input("Enter the area of the house in square meters: "))
predicted_price = predict_price(area)
print(f"The predicted price for a house with {area} m² is: {predicted_price:.2f} million VND")