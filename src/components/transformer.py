
import sys
from dataclasses import dataclass
import os

import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object


# A dataclass is a way to easily create classes that store data without writing extra code.
#   You use fit_transform on the training data to learn and apply transformations. 
#   For the test data, you use transform to apply the same learned transformation without re-learn again it.
#   np.c_[]: It is used to concatenate the arrays column-wise.
#In Python, self is used to refer to the current object of a class. It helps you access the object's properties and methods.
@dataclass
class transformer_details:
     transfomer_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformer:
     def __init__(self):
          self.transform=transformer_details()
     def  get_transformer_object(self):
        try:
           num_columns=["writing_score", "reading_score"]
           cat_columns= [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

           num_pipeline=Pipeline(
                steps=[
                   ("imputer", SimpleImputer(strategy='median')),
                   ('scaler', StandardScaler(with_mean=False))
                ]
           )
           cat_pipeline=Pipeline(
               steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('encoder',OneHotEncoder()),
                ('scaler',StandardScaler(with_mean=False)) 
               ]
           )

           transformer=ColumnTransformer(
               [
                 ("numerical",num_pipeline,num_columns),
                 ("categorical",cat_pipeline,cat_columns)
                 
               ]
           )
           return  transformer   
        except Exception as e:
            raise CustomException(e,sys)
        
     def  initiate_transformation(self,train_set,test_set):
        logging.info("data transformation inititated")
        try:
           train_df=pd.read_csv(train_set)
           test_df=pd.read_csv(test_set)
           logging.info("train and test data set converted to dataframe")
           transformer_obj=self.get_transformer_object()
           target_feature="math_score"
           train_input_features=train_df.drop(columns=[target_feature],axis=1)
           train_target_feature=train_df[target_feature]
           logging.info("splitted train data into input and target features")

           test_input_features=test_df.drop(columns=[target_feature],axis=1)
           test_target_feature=test_df[target_feature]
           logging.info("splitted test data into input and target features")

           train_input_features_array=transformer_obj.fit_transform(train_input_features)
           test_input_features_array=transformer_obj.transform(test_input_features)
           logging.info("applied fit_transform to train data and transfrom to test data")

           train_array=np.c_[train_input_features_array,np.array(train_target_feature)]
           test_array=np.c_[test_input_features_array,np.array(test_target_feature)]
           logging.info("made the  train data array and test data array")

           save_object(
               file_path=self.transform.transfomer_path,
               obj=transformer_obj
           )
           logging.info("saving the transformer object in artifacts folder")
#: A function used to save Python objects (e.g., transformers, models, etc.) to a file, usually using libraries like pickle or joblib.
           
           return train_array,test_array,self.transform.transfomer_path
        
        except Exception as e:
            raise CustomException(e,sys)
           
