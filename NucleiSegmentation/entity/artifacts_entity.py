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