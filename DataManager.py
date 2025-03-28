import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # 3D plot
import matplotlib.pyplot as plt
from sklearn import preprocessing

# データの前処理をするクラス
class RegressionDataManager:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path, sep=';')
        self.x = self.df[['wind_speed', 'distance']]
        self.y = self.df[['time']]
        self.x1 = self.df[['wind_speed']]
        self.x2 = self.df[['distance']]
    
    def standardize_data(self):
        sscaler = preprocessing.StandardScaler()
        sscaler.fit(self.x)
        self.xss_sk = sscaler.transform(self.x)
        sscaler.fit(self.y)
        self.yss_sk = sscaler.transform(self.y)
        return self.xss_sk, self.yss_sk

    def plot_data(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        fig.add_axes(ax)
        ax.scatter3D(self.x1, self.x2, self.y)
        ax.set_xlabel("x1")
        ax.set_ylabel("x2")
        ax.set_zlabel("y")
        plt.show()