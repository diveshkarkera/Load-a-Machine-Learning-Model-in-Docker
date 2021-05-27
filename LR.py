import pandas
from sklearn.linear_model import LinearRegression
ds = pandas.read_csv('Salary_Data.csv')
x=ds['YearsExperience'].values.reshape(30,1)
y=ds['Salary']
mind= LinearRegression()
mind.fit(x , y)
print(mind.coef_)
years = int(input('Enter the Years Experience you want to predict'00
y = mind.predict([[years]])
print(y)
