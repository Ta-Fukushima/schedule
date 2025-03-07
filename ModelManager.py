from sklearn.linear_model import LinearRegression
import pickle

# 回帰分析をするクラス
class RegressionModelManager:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.model = LinearRegression()
    
    # 学習モデルを作成する関数
    def train(self):
        self.model.fit(self.x, self.y)
    
    # 係数を取得する関数
    def get_coefficients(self):
        return self.model.coef_
    
    # 切片を取得する関数
    def get_intercept(self):
        return self.model.intercept_

    # スコアを取得する関数
    def get_score(self):
        return self.model.score(self.x, self.y)
    
    # モデルを保存する関数
    def save_model(self,model_name):
        with open(model_name, mode='wb') as f:
            pickle.dump(self.model, f, protocol=2)

    # モデルを読み込む関数
    def load_model(self,model_name):
        with open(model_name, mode='rb') as f:
            self.model = pickle.load(f)