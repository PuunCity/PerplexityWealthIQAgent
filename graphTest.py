import matplotlib.pyplot as plt
import numpy as np

# Simulate XRP price variations over the last 24 hours
hours = np.linspace(0, 24, 100)
prices = 0.5 + 0.1 * np.sin(2 * np.pi * hours / 24) + np.random.normal(0, 0.02, len(hours))

# Create the graph with annotations
plt.figure(figsize=(12, 6))
plt.plot(hours, prices, label='XRP Price (USD)', color='green', marker='o', markersize=4)
plt.title('XRP Price Variations in the Last 24 Hours', fontsize=16)
plt.suptitle('Data is simulated for illustrative purposes', fontsize=10, color='gray')
plt.xlabel('Time (hours)', fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)
plt.axhline(y=np.mean(prices), color='red', linestyle='--', label='Average Price')
plt.annotate('Highest Price', xy=(hours[np.argmax(prices)], max(prices)), xytext=(hours[np.argmax(prices)] + 2, max(prices) + 0.02),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('Lowest Price', xy=(hours[np.argmin(prices)], min(prices)), xytext=(hours[np.argmin(prices)] - 2, min(prices) - 0.02),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.legend()
plt.grid(True)
plt.show()
