import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('Housing.csv')

areas=df['area']
prices=df['price']
bedroom_number=df['bedrooms']
story_number=df['stories']

plt.figure(figsize=(8,5))
plt.bar(areas, prices, color='maroon', width=10)
ax1=plt.gca()
ax1.set_ylim([0, 15000000])
plt.title('Prices In Correlation to Area Sizes')
plt.xlabel('Area Size')
plt.ylabel('Prices')
plt.grid()
plt.show()


plt.figure(figsize=(8,5))
plt.bar(bedroom_number, prices, color='green', width=0.1)
plt.title('Prices In Correlation to Number of Bedrooms')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Prices')
plt.grid()
plt.show()

plt.figure(figsize=(8,5))
plt.bar(story_number, prices, color='aqua', width=0.1)
plt.title('Prices In Correlation to Number of Stories')
plt.xlabel('Number of Stories')
plt.ylabel('Prices')
plt.grid()
plt.show()











