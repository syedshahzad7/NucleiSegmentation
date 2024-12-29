#Here, we will be defining or encapsulating the outputs(artifacts) of each component
from dataclasses import dataclass



'''
Output of the data ingestion process: 1. The file path of the zip file containing the raw data after
it is downloaded. 2. file path of the directory where the unzipped (and maybe processed) data files 
are stored
'''
@dataclass                          
class DataIngestionArtifact:
    data_zip_file_path:str
    feature_store_path:str



'''
Output of the data validation process: 1. A boolean value inside status.txt. When it is true, it
means the artifacts/data_ingestion/feature_store has all the files required for training purpose
'''

@dataclass
class DataValidationArtifact:
    validation_status:bool