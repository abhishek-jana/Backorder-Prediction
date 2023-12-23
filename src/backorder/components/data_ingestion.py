import os
import urllib.request as request
# import rarfile
from rarfile import RarFile
from backorder.logging import logger
from backorder.utils.common import get_size
from pathlib import Path
from backorder.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")


    def extract_rar_file(self):
        """
        Extracts the RAR file into the data directory.
        Function returns None.
        """
        unrar_path = self.config.unrar_dir
        os.makedirs(unrar_path, exist_ok=True)

        with RarFile(self.config.local_data_file, 'r') as rar_ref:
            rar_ref.extractall(unrar_path)

    def remove_rar_file(self):
        """
        removes the downloaded rar file
        """
        os.remove(self.config.local_data_file)
  