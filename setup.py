from setuptools import setup, find_packages

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str):
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="myproject",
    version="0.1.0",
    author="Faisal datatech",
    author_email="faisalshahyasinzai444@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
