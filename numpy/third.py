import numpy as np
import matplotlib.pyplot as plt

# Format: [restaurant_id, 2021_sales, 2022_sales, 2023_sales, 2024_sales]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])

print("==== Zomato Sales Data ====")
print(sales_data.shape)
print(sales_data[:, 1:])

# Total sales per year
print(np.sum(sales_data[:, 1:], axis=0))
yearly_total = np.sum(sales_data[:, 1:], axis=0)
print(yearly_total)

# Minimum seles per restorant
print(np.min(sales_data[:, 1:], axis=1))

# Maximum sales per year
print(np.max(sales_data[:, 1:], axis=0))

# Average sales per restaurant
print(np.mean(sales_data[:, 1:], axis=1))

# cumulative sales
cumsum = np.cumsum(sales_data[:, 1:], axis=1)
print(np.cumsum(sales_data[:, 1:], axis=1))

# Plotting the sales data
plt.figure(figsize=(10, 6))
plt.plot(np.mean(cumsum, axis=0))
plt.title("Cumulative Sales Data")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

