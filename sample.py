import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  #3Dplot
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import preprocessing

df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

x = df[['density', 'volatile acidity']]
y = df[['alcohol']]
x1 = df[['density']]
x2 = df[['volatile acidity']]

print(x.shape)
print(y.shape)

fig=plt.figure()
ax=Axes3D(fig)
fig.add_axes(ax)
 
ax.scatter3D(x1, x2, y)
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("y")
 
plt.show()

sscaler = preprocessing.StandardScaler()
sscaler.fit(x)
xss_sk = sscaler.transform(x) 
sscaler.fit(y)
yss_sk = sscaler.transform(y)

#正規化なし
model_lr = LinearRegression()
model_lr.fit(x, y)

#正規化あり
model_lr_std = LinearRegression()
model_lr_std.fit(xss_sk, yss_sk)

print(model_lr_std.coef_)
print(model_lr_std.intercept_)
print(model_lr_std.score(xss_sk, yss_sk))
