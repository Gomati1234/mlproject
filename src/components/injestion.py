import os
import sys  
from src.logger import logging
from src.exception import CustomException

from sklearn.model_selection import train_test_split
import pandas as pd
from dataclasses import dataclass

from src.components.transformer import DataTransformer

@dataclass
class InjestionConf:
    train_data_path:str= os.path.join('artifacts',"train_data")
    test_data_path:str=os.path.join('artifacts',"test_data")
    raw_data_path:str=os.path.join('artifacts','raw_data')

class Injestion:    
    def __init__(self):
        self.injestion=InjestionConf()

    def initiate_injestion(self):
        logging.info("data injestion initiated")
        try:
            df=pd.read_csv('dataset/study.csv')
            logging.info("dataset converted to dataframe")

            df.to_csv(self.injestion.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            logging.info("train and test data set splitted")
            train_set.to_csv(self.injestion.train_data_path,index=False,header=True)
            test_set.to_csv(self.injestion.test_data_path,index=False,header=True)
            logging.info("data injestion Completed")  

            return(
                self.injestion.train_data_path,
                self.injestion.test_data_path
            )  
        except Exception as e:
             raise CustomException(e,sys)


if __name__=="__main__":
    obj=Injestion()
    train_set,test_set=obj.initiate_injestion()
    datatransformer=DataTransformer()
    train_array,test_array,transfomer_path=datatransformer.initiate_transformation(train_set,test_set)
  
 

