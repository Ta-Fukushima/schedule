from DataManager import RegressionDataManager
from ModelManager import RegressionModelManager
import app_param

# データの前処理
preprocessor = RegressionDataManager(app_param.REGRESSION_MODEL_PARAM["TRAINING_DATA_PATH"])
# preprocessor.plot_data()
xss_sk, yss_sk = preprocessor.standardize_data()

# 正規化なしのモデル
model_lr = RegressionModelManager(preprocessor.x, preprocessor.y)
model_lr.train()
print("Coefficients (no standardization):", model_lr.get_coefficients())
print("Score (no standardization):", model_lr.get_score())

# 正規化ありのモデル
model_lr_std = RegressionModelManager(xss_sk, yss_sk)
model_lr_std.train()
print("Coefficients (standardized):", model_lr_std.get_coefficients())
print("Score (standardized):", model_lr_std.get_score())
model_lr.save_model(app_param.REGRESSION_MODEL_PARAM["MODEL_PATH"])