from sklearn.datasets import load_boston
from sympy import true
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
X, Y = load_boston(return_X_Y=true)
mod = LinearRegression()
mod.fit(X, Y)
mod.predict(X)
