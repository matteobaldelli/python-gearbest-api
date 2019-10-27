from setuptools import setup

setup(
    name='gearbest_api',
    version='0.0.1',
    description='Retrieve info from gearbest api.',
    url='https://github.com/matteobaldelli/python-gearbest-api',
    license='MIT',
    author='Matteo Baldelli',
    author_email='baldelli.matteo2@google.com',
    packages=['gearbest_api'],
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
