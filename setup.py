"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import find_packages
from setuptools import setup

setup(
    name='manage_lunch',
    version='1.0',
    description='Buy Me Lunch',
    url='https://github.com/dgholz/manage_lunch',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'munch=manage_lunch.cli:main',
        ],
        'manage_lunch.command': [
            'pick=manage_lunch.command.pick:PickCommand',
        ],
        'manage_lunch.plugin': [
            'RandomPicker=manage_lunch.plugin.random_picker:RandomPicker',
            'LunchPlaces=manage_lunch.plugin.lunch_places:LunchPlaces',
        ],
    },
)
