from src.components.transformer import DataTransformer
from src.components.model_trainer import modelTrainer
from src.components.injestion import Injestion


if __name__=="__main__":
    injestion=Injestion()
    train_set,test_set=injestion.initiate_injestion()
    datatransformer=DataTransformer()
    train_array,test_array,transfomer_path=datatransformer.initiate_transformation(train_set,test_set)
    modeltrainer=modelTrainer()
    best_r2_score=modeltrainer.initiate_model_trainer(train_array,test_array)
    print(best_r2_score)
 