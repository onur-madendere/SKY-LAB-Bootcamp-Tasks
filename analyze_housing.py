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





#assigning numbers to string values for evaluation
df['mainroad']=df['mainroad'].map({'yes': 1, 'no':0})
df['guestroom']=df['guestroom'].map({'yes': 1, 'no':0})
df['basement']=df['basement'].map({'yes': 1, 'no':0})
df['hotwaterheating']=df['hotwaterheating'].map({'yes': 1, 'no':0})
df['airconditioning']=df['airconditioning'].map({'yes': 1, 'no':0})
df['prefarea']=df['prefarea'].map({'yes': 1, 'no':0})
df['furnishingstatus']=df['furnishingstatus'].map({'unfurnished': 0, 'semi-furnished': 1, 'furnished':2})


#printing the matrix on terminal
corr_matrix=df.corr('spearman')
print(corr_matrix)

#generating heatmap
plt.matshow(corr_matrix)
plt.title('Correlation Matrix Heatmap')
plt.show()
















