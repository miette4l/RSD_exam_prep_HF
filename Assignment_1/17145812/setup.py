from setuptools import setup, find_packages

setup(
    name="alchemist",
    version="0.1.0",
    author="Holly Farler",
    packages=find_packages(exclude=['*tests']),
    install_requires=['pyyaml'],
    entry_points={
        'console_scripts': [
            'abracadabra = alchemist.command:process'
        ]})
