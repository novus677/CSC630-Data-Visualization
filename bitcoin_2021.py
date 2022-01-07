import numpy as np
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
price = [34622, 46643, 58734, 53260, 35750, 35946, 41157, 47663, 41413, 61374, 57834, 46195]


plt.scatter(months, price)
for i in range(len(months)-1):
    plt.plot([months[i], months[i+1]], [price[i], price[i+1]], color="green" if price[i+1] > price[i] else "red")
plt.title("Bitcoin price throughout 2021")
plt.ylabel("Price in USD")
plt.show()