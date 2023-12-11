# Create folders and files autometically

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "backorder"  # name specific name to your project

list_of_files = [
    # since it's an empty folder we need a file to commit to github
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/component/__init__.py",
    f"{project_name}/component/training/__init__.py",
    f"{project_name}/component/training/data_ingesion.py",
    f"{project_name}/component/training/data_validation.py",
    f"{project_name}/component/training/data_transformation.py",
    f"{project_name}/component/training/model_evaluation.py",
    f"{project_name}/component/training/model_pusher.py",
    f"{project_name}/component/training/model_trainer.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/mongo_client.py",
    f"{project_name}/config/pipeline/training.py",
    f"{project_name}/config/pipeline/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline_config/__init__.py",
    f"{project_name}/constant/training_pipeline_config/data_ingesion.py",
    f"{project_name}/constant/training_pipeline_config/data_validation.py",
    f"{project_name}/constant/training_pipeline_config/data_transformation.py",
    f"{project_name}/constant/training_pipeline_config/model_evaluation.py",
    f"{project_name}/constant/training_pipeline_config/model_pusher.py",
    f"{project_name}/constant/training_pipeline_config/model_trainer.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/schema.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/pipeline/training.py",
    f"{project_name}/pipeline/prediction.py",
    f"{project_name}/logging/__init__.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

for filepath in list_of_files:
    filepath = Path(filepath)  # to avoid confusion between linux and windows
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already present.")