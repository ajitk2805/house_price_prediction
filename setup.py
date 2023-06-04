from setuptools import setup, find_packages
from typing import List

hypen_e_dot = "-e ."

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_object:
        requirement = file_object.readlines()
        requirements = [i.replace("\n","") for i in requirement]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements

setup(
    name='house-price-predictor',
    version='0.0.1',
    author='Ajit',
    description='This is a ML (linear regression) project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)