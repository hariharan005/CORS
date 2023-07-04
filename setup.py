from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="CORS-Analyzer",
    version= '1.0.4',
    author= 'Hariharan',
    description= 'The cors-analyzer package is used to find the vulnerable CORS domains',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords= ['cors', 'cors-finder', 'cors-analyzer', 'cors misconfiguration', 'cors exploit', 'cors vulnerability'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cors-analyzer = lib.cors:main',
        ]
    },
    install_requires=[
        'requests',
        'colorama',
    ],
    
    
)