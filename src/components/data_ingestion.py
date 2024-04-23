import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation 
from src.components.data_transformation import DataTransformationConfig
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts","train.csv")
    test_data_path: str = os.path.join("artifacts","test.csv")
    raw_data_path: str = os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    def initial_data_ingestion(self):
        logging.info("Data Ingestion has Began!")
        try:
            # first we want to read in our data.... Now this can be from any source. 
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Read data as dataframe")

            # used as a confirmation. 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,header=True,index=False)

            logging.info("Train test split")
            train_set, test_set = train_test_split(df,test_size=.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,header=True,index=False)
            test_set.to_csv(self.ingestion_config.test_data_path,header=True,index=False)

            logging.info("Ingestion done!!")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        # we are returning this for data transformation. 
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initial_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)
        
