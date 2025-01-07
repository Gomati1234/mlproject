import os 
import sys

import numpy as np
import pandas as pd
import dill

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