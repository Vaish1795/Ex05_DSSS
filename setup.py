from setuptools import find_packages
from setuptools import setup

setup(
    name='snowflake',
    version='1.0.0',
    description='This project creates random colour snowflakes',
    author='Vaishnavi Umesh',
    author_email='vaishnavi.umesh@fau.de',
    url='https://github.com/Vaish1795/Ex05_DSSS',
    packages=find_packages(),
    install_requires=["numpy", "turtles"]
)
