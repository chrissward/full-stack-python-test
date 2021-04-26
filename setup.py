from setuptools import setup

setup(
    name='fsa',
    version='0.0.1',
    description='Tech test skeleton',
    install_requires=[
        'flask',
        'requests'
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
