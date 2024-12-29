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