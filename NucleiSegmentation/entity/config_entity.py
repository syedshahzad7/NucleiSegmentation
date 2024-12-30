#This file defines all the configuration classes (dealing with inputs given to various components)
import os
from dataclasses import dataclass
from datetime import datetime
from NucleiSegmentation.constant.training_pipeline import *

@dataclass
class TrainingPipelineConfig:                   #The input that shall be given to the TrainingPipeline. We shall only give the directory of where the artifacts(outputs) of the Training pipeline needs to be stored
    artifacts_dir: str = ARTIFACTS_DIR


training_pipeline_config:TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:                      #The input that shall be given to the data ingestion component is: the path for data_ingestion sub-directory which is inside the "artifacts" directory. This is basically the path where the output(artifacts) of the data_ingestion component will be saved. artifacts/data_ingestion. Iske andar artifacts rahinge. 2nd input is feature_store ka path (where unzipped raw data will be stored.) artifacts/data_ingestion/feature_store. Finally, third input is the url jahan se data ko download karna hai.
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME)

    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR)

    data_download_url: str = DATA_DOWNLOAD_URL


@dataclass
class DataValidationConfig:                     #The input that is given to the data validation component: 1. path where the data_validation sub directory needs to be created inside artifacts directory. 2) path inside this subdirectory where status.txt is saved which says whether the format of the data is correct or not. 3) list of files that needs to be present in artifacts/data_ingestion/feature_store so that status.txt says 'valid'
    data_validation_dir: str = os.path.join(training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME)   #artifacts/data_validation

    valid_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)     #artifacts/data_validation/status.txt

    required_file_list = DATA_VALIDATION_ALL_REQUIRED_FILES     


@dataclass
class ModelTrainerConfig:           #Input to model_trainer: 1) path of model_trainer inside artifacts folder. 2)Model/Weight name. 3)No. of epochs to train the model.
    model_trainer_dir: str = os.path.join(training_pipeline_config.artifacts_dir, 
                                          MODEL_TRAINER_DIR_NAME)
    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME
    no_epochs = MODEL_TRAINER_NO_EPOCHS