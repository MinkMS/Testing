from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

data = pd.read_excel(r"C:\Users\hoang\Downloads\Loan_data.xlsx")

df = pd.DataFrame(data, columns=['Salary', 'Working Time', 'Loan Decision'])

X = df[['Salary', 'Working Time']].values
y = df['Loan Decision'].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression()
model.fit(X_scaled, y)

x1_range = np.linspace(df['Salary'].min(), df['Salary'].max(), 100)
x2_range = np.linspace(df['Working Time'].min(), df['Working Time'].max(), 100)
xx, yy = np.meshgrid(x1_range, x2_range)
grid = np.c_[xx.ravel(), yy.ravel()]
grid_scaled = scaler.transform(grid)
probs = model.predict_proba(grid_scaled)[:, 1].reshape(xx.shape)

plt.scatter(df['Salary'], df['Working Time'], c=y, cmap='bwr', marker='o', label='Loan Decision')
plt.xlabel('Salary (mil VND)')
plt.ylabel('Working Time (years)')

plt.contour(xx, yy, probs, levels=[0.5], cmap="Accent", linewidths=2)

salary_input = float(input("Enter the salary (in million VND): "))
working_time_input = float(input("Enter the working time (in years): "))

new_data = np.array([[salary_input, working_time_input]])
new_data_scaled = scaler.transform(new_data)
prediction = model.predict(new_data_scaled)
probability = model.predict_proba(new_data_scaled)

print(f"Loan Decision: {'Granted' if int(prediction[0]) == 1 else 'Not Granted'}")
print(f"Probability of Loan Approval: {probability[0][1]:.2f}")

plt.scatter(salary_input, working_time_input, color='yellow', edgecolor='black', label='New Guy', zorder=5)

plt.grid(True)
plt.legend()
plt.show()