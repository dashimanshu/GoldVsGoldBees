import matplotlib.pyplot as plt

# Data
gold_prices = [
    26343.50, 28006.50, 28623.50, 29667.50, 31438.00, 35220.00, 48651.00,
    48720.00, 52670.00, 63820.00
]  # Prices in Rs per 10 grams
goldbees_prices = [
    24.5, 24.06, 26.80, 26.31, 27.36, 31.06, 42.10, 40.99, 43.98, 50.68
]  # Prices in Rs
years = range(2014, 2024)  # Assuming these are the last 10 years

# Create a figure and a set of subplots
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting gold prices on the primary Y-axis
ax1.set_xlabel('Years')
ax1.set_ylabel('Gold Prices (Rs per 10 grams)', color='tab:blue')
ax1.plot(years, gold_prices, color='tab:blue', marker='o', label='Gold Prices')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Creating a secondary Y-axis for GOLDBEES prices
ax2 = ax1.twinx()
ax2.set_ylabel('GOLDBEES Prices (Rs)', color='tab:orange')
ax2.plot(years,
         goldbees_prices,
         color='tab:orange',
         marker='s',
         label='GOLDBEES Prices')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# Adding a title and a grid
plt.title('Gold Prices vs GOLDBEES Prices Over 10 Years')
ax1.grid()

# Show the plot
plt.show()
