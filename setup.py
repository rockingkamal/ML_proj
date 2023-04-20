from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT= '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirments
    '''
    requirements=[]
    with open(file_path) as file_obj: #file path is requirments.txt
        requirements=file_obj.readlines()
        requirements=[reg.replace("/n", " ")  for reg in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='ML_proj',
    version='0.0.1',
    author="Kamal",
    author_email='vayalpatikamalthej@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)

