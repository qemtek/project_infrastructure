import os

project_dir = os.getcwd()
model_dir = os.path.join(project_dir, 'models')

available_models = ['LogisticRegression', 'XGBClassifier', 'XGBRegressor']
