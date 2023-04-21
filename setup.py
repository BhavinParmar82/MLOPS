from typing import List

from setuptools import find_packages, setup

hypen_const = "-e ."


def get_requires(file_path: str) -> List[str]:
    """
    This function will return all package requirements as a list
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if hypen_const in requirements:
            requirements.remove(hypen_const)
    return requirements


setup(
    name="src",
    packages=find_packages(),
    version="0.1.0",
    description="MLOPs testing purpose",
    author="Bhavin Parmar",
    license="",
    install_requires=get_requires("requirements.txt"),
)
