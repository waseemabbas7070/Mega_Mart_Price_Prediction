from src.dataspliter import DataSpliter
from pipelines.model import Models
from sklearn.metrics import r2_score
import joblib as j
spliter = DataSpliter()
x_train, x_test, y_train, y_test=spliter.data_spliter()
model = Models()
grid_search=model.randomforest()
print('Starting Training')
grid_search.fit(x_train, y_train)
print('Got the Best Model')
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_
predictions = best_model.predict(x_test)
r2 = r2_score(y_test, predictions)
print(r2)
j.dump(best_model,"models/model.pkl")
print("model saved ")