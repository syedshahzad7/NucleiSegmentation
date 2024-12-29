'''
In this module, we will download the raw dataset zip file, unzip that file and prepare the dataset for 
further processing in the pipeline. This module ensures that the data is available in the desired format 
and location.
'''

import os
import sys
import zipfile
import gdown
from NucleiSegmentation.exception import CustomException
from NucleiSegmentation.logger import logging
from NucleiSegmentation.entity.config_entity import DataIngestionConfig
from NucleiSegmentation.entity.artifacts_entity import DataIngestionArtifact

class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e, sys)
    
    def download_data(self)-> str:
        try:
            #Before actually downloading, lets make the directories first.
            dataset_url = self.data_ingestion_config.data_download_url  #url where the dataset is stored
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir    #this is the path where the .zip file will be saved -> artifacts/data_ingestion. In this path data.zip will be stored 
            os.makedirs(zip_download_dir, exist_ok = True)          #upar path banaye. Idhar directory banare
            data_file_name = "data.zip"                    #zip file ka naam data.zip rahinga.
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info(f"Downloading data from {dataset_url} into file {zip_file_path}")

            #We'll start the actual downloading logic now.
            file_id = dataset_url.split("/")[-2]        #extracting the id from the google drive link
            prefix = 'https://drive.google.com/uc?/export=download&id='     #This url combined with the id extracted above will be enough to download whatever was inside that link using the gdown.download() method
            gdown.download(prefix+file_id, zip_file_path)       #downloading the contents of that link to the path: artifact/data_ingestion/data.zip (given by zip_file_path)
            logging.info(f"Downloaded data from {dataset_url} into file {zip_file_path}")

            return zip_file_path
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def extract_zip_file(self,zip_file_path: str)-> str:            #The downloaded zip file will now be extracted and stored into artifacts/data_ingestion/feature_store
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """

        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok = True)        #creating the directory artifacts/data_ingestion/feature_store
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:       #unzipping data.zip into feature_store
                zip_ref.extractall(feature_store_path)
            logging.info(f"Extracted zip file: {zip_file_path} into dir: {feature_store_path}")

            return feature_store_path          # returning this newly created feature_store that contains the unzipped raw dataset.
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_ingestion(self)-> DataIngestionArtifact:      #Actual data ingestion happens when this method is called.
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")
        try:
            zip_file_path = self.download_data()        #Downloads the .zip file mentioned by the URL in the constants folder - DATA_DOWNLOAD_URL. Saves this .zip file in zip_file_path(artifact/data_ingestion/data.zip)
            feature_store_path = self.extract_zip_file(zip_file_path)   #Extracting data.zip into feature_store_path(artifacts/data_ingestion/feature_store)
            #That's it! Your data ingestion is done. You just have to return these 2 things. 
            #For returning the outputs(artifacts), we create an object of the DataIngestionArtifact and return that object
            
            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path = zip_file_path,
                feature_store_path = feature_store_path
            )

            logging.info("Exiting initiate_data_ingestion method of DataIngestion class")
            logging.info(f"Data Ingestion artifacts: {data_ingestion_artifact}")

            return data_ingestion_artifact
    
        except Exception as e:
            raise CustomException(e, sys)

        