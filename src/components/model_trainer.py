import os
import sys
from dataclasses import dataclass
# from catboost import CatBoostRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from  src.logger import logging
from src.exception import CustomException
from src.utils import evaluate_model,save_object

from dataclasses import dataclass
@dataclass
class modelTrainerConf:
    model_trainer_path=os.path.join('artifacts',"model.pkl")
      
class modelTrainer:
    def __init__(self):
        self.model_trainer_obj=modelTrainerConf()
    def initiate_model_trainer(self,train_array,test_array):
        try:
            x_train,y_train,x_test,y_test=train_array[:,:-1],train_array[:,-1],test_array[:,:-1],test_array[:,-1]

            models={
                "Linear regression":LinearRegression(),
                "K neighbors regressor":KNeighborsRegressor(),
                "Decision tree regressor":DecisionTreeRegressor(),
                "XGBregressor":XGBRegressor(),
                # "Cat boost regressor": CatBoostRegressor(),
                "Ada boost regressor":AdaBoostRegressor(),
                "Gradient boosting regressor":GradientBoostingRegressor(),
                "Random forest regressor":RandomForestRegressor()
            }
            
            model_report:dict=evaluate_model(x_train,y_train,x_test,y_test,models)
            model_maximum_score=max(sorted(model_report.values()))

            model_name= list(models.values())[list(model_report.values()).index(model_maximum_score)]  
            save_object(
                file_path=self.model_trainer_obj.model_trainer_path,
                obj=model_name
            )
            return model_maximum_score 

        except Exception as e:
            raise CustomException(e,sys)