from setuptools import setup

setup(
    name='CSVProcessor',
    packages=['Models', 'Utilities'],
    entry_points={
        'console_scripts': [
            'CSVProcessor = CSVProcessor:main',
        ]
    }
)