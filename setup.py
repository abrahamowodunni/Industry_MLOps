from setuptools import setup, find_packages
from typing import List


E_DOT = '-e .' ## this is used in the development stage.

# creating a function that helps us get the required libraries 
def get_requirments(file_path:str)->List[str]:
    """
    Reads the specified requirements file and returns a list of requirements.
    Args:
        file_path (str): The path to the requirements file.
    Returns:
        List[str]: A list of requirements extracted from the file.
    """
    requirments = []
    with open(file_path) as f:
        requirments = f.readlines()
        requirments = [req.replace("\n","") for req in requirments]

        if E_DOT in requirments:
            requirments.remove(E_DOT)

    return requirments


setup(
    name = 'Industry MLOps',
    version= '0.0.1',
    author= 'Abraham Owodunni',
    author_email= 'abrahamowodunni@gmail.com',
    packages=find_packages(),
    install_requires = get_requirments('requirements.txt')
)