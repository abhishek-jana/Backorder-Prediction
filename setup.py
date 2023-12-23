from setuptools import setup, find_packages
from typing import List

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

    __version__ = "0.0.0"
    REPO_NAME = "Backorder-Prediction"
    AUTHOR_USER_NAME = "abhishek-jana"
    SRC_REPO = "backorder"
    AUTHOR_EMAIL = "abhishekjana6@gmail.com"
    DESCRIPTION="A solution that should able to predict backorder",

    REQUIREMENT_FILE_NAME = "requirements.txt"

    HYPHEN_E_DOT = "-e ."


    setup(
        name=SRC_REPO,
        version=__version__,
        author=AUTHOR_USER_NAME,
        author_email=AUTHOR_EMAIL,
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content="text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        project_urls={
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        },
        packages=find_packages(),
        install_requires=get_requirements_list()
        )