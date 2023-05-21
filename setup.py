from setuptools import setup, find_packages
from src.metadata import (
    __author__,
    __description__,
    __email__,
    __license__,
    __project__,
    __version__,
)

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('LICENSE') as f:
    license = f.read()

setup(
    name=__project__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    license='MIT License',
    license_files=('LICENSE',),
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Prog-in/{__project__}",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    #python_requires="~=3.11",  # não testado em outros
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            f'{__project__} = src.main:main'
        ]
    }
)
