import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("celsius_fahrenheit.csv")

# Plot
#sns.scatterplot(data=df, x='Celsius', y='Fahrenheit', hue="Fahrenheit", palette="coolwarm")
#plt.show()

x = df['Celsius']
y = df['Fahrenheit']

x_processed = x.values.reshape(-1, 1)
y_processed = y.values.reshape(-1, 1)


from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_processed, y_processed)

prdicted = model.predict([[20]])

print(prdicted)

print("Score: ", model.score(x_processed, y_processed))