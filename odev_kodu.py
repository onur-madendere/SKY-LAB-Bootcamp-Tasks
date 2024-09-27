import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
df=pd.read_csv('Housing.csv')

areas=df['area']
prices=df['price']
bedroom_number=df['bedrooms']
story_number=df['stories']

#price- area size
plt.figure(figsize=(8,5))
plt.bar(areas, prices, color='maroon', width=10)
ax1=plt.gca()
ax1.set_ylim([0, 15000000])
plt.title('Prices In Correlation to Area Sizes')
plt.xlabel('Area Size')
plt.ylabel('Prices')
plt.grid()
plt.show()

#price- bedroom count
plt.figure(figsize=(8,5))
plt.scatter(bedroom_number, prices, color='green')
plt.title('Prices In Correlation to Number of Bedrooms')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Prices')
plt.grid()
plt.show()


#price- story count
plt.figure(figsize=(8,5))
plt.scatter(story_number, prices, color='aqua')
plt.title('Prices In Correlation to Number of Stories')
plt.xlabel('Number of Stories')
plt.ylabel('Prices')
plt.grid()
plt.show()


#price- bathroom count
mean_price_for_bathrooms=df['price'].groupby(df['bathrooms']).mean()
bathroom_number=df['bathrooms'].value_counts()


plt.figure(figsize=(8,5))
plt.bar(bathroom_number.index, mean_price_for_bathrooms, color='black')
plt.title('Mean Value of Prices Based on Number of Bathrooms')
plt.xlabel('Number of Bathrooms')
plt.ylabel('Average Prices')
plt.grid()
plt.show()



#price- furnishing status graph
mean_price_for_furnishing=df['price'].groupby(df['furnishingstatus']).mean()
furnishing_status=df['furnishingstatus'].value_counts()

plt.figure(figsize=(8,5))
plt.bar(mean_price_for_furnishing.index, mean_price_for_furnishing, color='red')
plt.title('Mean Value of Prices Based on Furnishing Status')
plt.xlabel('Furnishing Status')
plt.ylabel('Average Prices')
plt.grid()
plt.show()






df['mainroad']=df['mainroad'].astype('category').cat.codes
df['guestroom']=df['guestroom'].astype('category').cat.codes
df['basement']=df['basement'].astype('category').cat.codes
df['hotwaterheating']=df['hotwaterheating'].astype('category').cat.codes
df['airconditioning']=df['airconditioning'].astype('category').cat.codes
df['prefarea']=df['prefarea'].astype('category').cat.codes
df['furnishingstatus']=df['furnishingstatus'].astype('category').cat.codes



corr_matrix=df.corr('kendall')
print(corr_matrix)
















