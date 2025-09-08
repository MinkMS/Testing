import pandas as pd

# Load your dataset
file_path = r"C:\Users\hoang\Downloads\wine+quality\winequality-white.csv"
wine_data = pd.read_csv(file_path)

# Calculate the statistics
mean_values = wine_data.mean()
variance_values = wine_data.var()
covariance_matrix = wine_data.cov()
correlation_matrix = wine_data.corr()

# Print results in a cleaner format
for feature in wine_data.columns:
    print(f"Feature: {feature}")
    print(f"  Mean: {mean_values[feature]:.4f}")
    print(f"  Variance: {variance_values[feature]:.4f}")
    print(f"  Covariance with Quality: {covariance_matrix[feature]['quality']:.4f}")
    print(f"  Correlation with Quality: {correlation_matrix[feature]['quality']:.4f}\n")
