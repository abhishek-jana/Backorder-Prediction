import pymongo
import pandas as pd 
import json
from pathlib import Path
from dotenv import load_dotenv

from backorder.config.mongo_client import MongodbClient


TEST_DATA_FILE_PATH = Path("research/dataset/Kaggle_Test_Dataset_v2.csv")
TRAIN_DATA_FILE_PATH = Path("research/dataset/Kaggle_Training_Dataset_v2.csv")
DATABASE_NAME = "backorder-prediction"
TEST_COLLECTION_NAME = "backorder_test"
TRAIN_COLLECTION_NAME = "backorder_train"
CHUNK_SIZE = 1000

def insert_bulk_data(df_path,collection_name,db_name = DATABASE_NAME,chunk_size=CHUNK_SIZE):
    mongoclient = MongodbClient(db_name)
    #insert it into mongo db
    collection = mongoclient.database[collection_name]
    # Read CSV file in chunks and insert into MongoDB
    print(f"Reading data from {df_path}")
    for chunk in pd.read_csv(df_path,low_memory=False, chunksize=chunk_size):
        # Convert the chunk to a list of dictionaries
        records = chunk.to_dict(orient="records")
        # Insert the records into MongoDB
        collection.insert_many(records)
    print(f"Data inserted successfully to {collection_name}.")  

if __name__ == "__main__":
    load_dotenv()

    #insert it into mongo db
    try:
        insert_bulk_data(df_path = TRAIN_DATA_FILE_PATH, collection_name=TRAIN_COLLECTION_NAME)
        insert_bulk_data(df_path = TEST_DATA_FILE_PATH, collection_name=TEST_COLLECTION_NAME)

    except Exception as e:
        print(f"Error during insertion: {e}")