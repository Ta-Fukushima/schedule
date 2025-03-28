from DataManager import RegressionDataManager
from ModelManager import RegressionModelManager

# データの前処理
preprocessor = RegressionDataManager('training_data.csv')
preprocessor.plot_data()
xss_sk, yss_sk = preprocessor.standardize_data()

# 正規化なしのモデル
model_lr = RegressionModelManager(preprocessor.x, preprocessor.y)
model_lr.train()
print("Coefficients (no standardization):", model_lr.get_coefficients())
print("Score (no standardization):", model_lr.get_score())
model_lr.save_model("model_lr_std_off.pkl")

# 正規化ありのモデル
model_lr_std = RegressionModelManager(xss_sk, yss_sk)
model_lr_std.train()
print("Coefficients (standardized):", model_lr_std.get_coefficients())
print("Score (standardized):", model_lr_std.get_score())
model_lr.save_model("model_lr_std_on.pkl")