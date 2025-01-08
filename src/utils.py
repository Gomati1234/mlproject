import os 
import sys

import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score

#dump() is a method provided by dill (or pickle) that serializes a Python object 
#(i.e., converts it into a binary format) and writes it to a file.
from src.exception import CustomException
def save_object(file_path,obj):
  try:
    file_paths=os.path.dirname(file_path)
    os.makedirs(file_paths,exist_ok=True)
    
    with open(file_path,'wb') as file_obj:
        dill.dump(obj,file_obj)
  except Exception as e:
     raise CustomException(e,sys)

def evaluate_model(x_train,y_train,x_test,y_test,models):
      
   try:   
      model_report={}
      
      for i in range(len(list(models.keys()))):
         model=list(models.values())[i]
         model.fit(x_train,y_train)

         predict_y_train=model.predict(x_train)
         predict_y_test=model.predict(x_test)

         train_r2_score=r2_score(y_train,predict_y_train)
         test_r2_score=r2_score(y_test,predict_y_test)

         model_report[list(models.keys())[i]]= test_r2_score

      return model_report
   except Exception as e:
      CustomException(e,sys)