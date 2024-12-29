ARTIFACTS_DIR: str = "artifacts"   #A string constant specifying the base directory ("artifacts") where all generated files and outputs (artifacts) of the training pipeline will be stored.

'''
Here, we mention the 'constant variables' related or used in the data_ingestion component and also throughout the project
'''

DATA_INGESTION_DIR_NAME: str = "data_ingestion"         #A string constant that names the subdirectory ("data_ingestion") where the data ingestion component's output will be stored.

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"     #A string constant that specifies the subdirectory ("feature_store") inside the data ingestion directory where the unzipped dataset files will be stored.


DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1aPcVcFm0obYkgLIDEs0M7chphP-n_wG9/view?usp=drive_link"            #URL pointing to the location from where the raw dataset can be downloaded.








'''
Constant variables related to or used in the data_validation component and also throughout the project
'''

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "test", "data.yaml"]