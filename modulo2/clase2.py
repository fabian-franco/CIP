import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

df = pd.read_csv("housingData.csv")

# Basic information
""" print(df.head())
print(df.info())        
print(df.describe()) """

# Histogram
""" df.hist()
df.hist("median_house_value")
df.hist(figsize=(10, 10), bins=50, edgecolor='black')
plt.show() """

# Scartter plot
""" sb.scatterplot(x="latitude", y="longitude", data=df, hue="median_house_value", palette="coolwarm")
plt.show()

sb.scatterplot(x="latitude", y="longitude", data=df[(df.median_income > 10)], hue="median_house_value", palette="coolwarm")
plt.show() """

# Clean data
cleaned_data = df.dropna()
""" print(cleaned_data.info())
print(cleaned_data['ocean_proximity'].value_counts()) """

#Dummies / One-Hot Encoding
dummies_ocean = pd.get_dummies(cleaned_data["ocean_proximity"], dtype=int)
cleaned_data = cleaned_data.join(dummies_ocean)
cleaned_data.drop("ocean_proximity", axis=1, inplace=True)

# Correlation
""" cleaned_data.corr()
sb.set_theme(rc={'figure.figsize': (15,8)})
sb.heatmap(cleaned_data.corr(), annot=True, cmap="YlGnBu")
cleaned_data.corr()["median_house_value"].sort_values(ascending=False)
plt.show() """

# Lineal Regression
x = cleaned_data.drop("median_house_value", axis=1)
y = cleaned_data["median_house_value"]

# divide data into training and testing
X_entrena, X_prueba, Y_entrena, Y_prueba = train_test_split(x, y, test_size=.2)

# Create model
model = LinearRegression()

# Train model
model.fit(X_entrena, Y_entrena)

# Predict
prediccion = model.predict(X_prueba)

compartaion = pd.DataFrame({"Real": Y_prueba, "Prediccion": prediccion})
print(compartaion)

# Score
print("Score: ", model.score(X_prueba, Y_prueba))
print("Score: ", model.score(X_entrena, Y_entrena))

mse = mean_squared_error(Y_prueba, prediccion)
print("MSE: ", mse)