# using linera regression we can predict the home prices 
# linear regression single variable 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import linear_model 

# data frame

df = pd.read_csv("homeprice.csv")

 



#linear regresiion from sklearn 

reg = linear_model.LinearRegression()
reg.fit(df[['Area']],df.value)


#reg.predict([[9600]])

m=float(reg.coef_)
b=reg.intercept_
area = int(input("Enter the area for price : "))
price = m*area + b 
print('Predicted price in dwarka is :', float(price),' Cr' )

# distrbuition of data point 


plt.xlabel ('area (sq. ft)', fontsize=20)
plt.ylabel ('price (in .cr )', fontsize=20)
plt.scatter(df.Area,df.value, color = 'red', marker = '+')
plt.plot(df.Area,reg.predict(df[['Area']]), color = 'blue')
plt.show()

#making model for per capita income 
