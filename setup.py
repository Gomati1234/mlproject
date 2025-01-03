from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    hyphen_e_dot="-e ."
    with open(file_path) as file_obj:
          requirements=file_obj.readlines()
          print(requirements)
          requirements=[req.replace('\n','') for req in requirements]
    
    if hyphen_e_dot in requirements:
          requirements.remove(hyphen_e_dot)
    print(requirements)
    return requirements
        

setup(
    name='mlproject',
    version='0.0.1',
    author='Sangram',
    author_email='sangramsahu2703@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)